# Standar Rekayasa Database, Indeks ESR & Kontrak API Presisi

Dokumen ini menjadi acuan teknis Divisi Arsitek (D-02) dan tolok ukur audit bagi Divisi Backend (D-05) di Gate 3.

---

## 1. Hukum Desain Indeks Komposit ESR (*Equality, Sort, Range*)

90% kelambatan server aplikasi fullstack bukan karena bahasa pemrogramannya lambat, melainkan karena database melakukan **Sequential / Full Table Scan** pada ratusan ribu baris!

Saat merancang indeks komposit untuk setiap kueri halaman utama/antrean, urutkan kolom di dalam indeks menggunakan rumus **E → S → R**:
1. **E — Equality (Persamaan Eksak `=`)**: Letakkan paling depan! Contoh: `tenant_id`, `unit_kerja_id`, `status`.
2. **S — Sort (Pengurutan `ORDER BY`)**: Letakkan di urutan kedua agar database tidak perlu melakukan *filesort / memory sort* berat! Contoh: `created_at DESC` atau `sla_deadline_at ASC`.
3. **R — Range (Rentang `<, >, BETWEEN`)**: Letakkan paling belakang.

> **Contoh Nyata Sistem Birokrasi**:
> Halaman antrean verifikator selalu menjalankan kueri:
> `SELECT ... FROM submissions WHERE unit_id = $1 AND status = 'MENUNGGU_VERIFIKASI' ORDER BY sla_deadline_at ASC LIMIT 25;`
> Maka indeks yang **WAJIB** tertulis di dokumen arsitektur adalah:
> `CREATE INDEX idx_submissions_unit_status_sla ON submissions (unit_id, status, sla_deadline_at ASC);`
> *(Untuk tabel raksasa di mana 95% baris sudah berstatus `SELESAI`, gunakan **Partial Index** pada PostgreSQL: `WHERE status NOT IN ('SELESAI', 'DIBATALKAN')` agar ukuran indeks 20x lebih ramping di RAM!).*

---

## 2. Pola Skema Referensi untuk Organisasi, Jabatan & Audit (Skala S2/S3)

1. **Pohon Hierarki Unit Kerja Cepat Tanpa Rekursi Lambat**:
   Simpan kolom `hierarchy_path VARCHAR` (contoh: `/01/0104/010402/`) pada tabel `org_units` dengan indeks prefix. Mencari seluruh pengajuan di satu Dinas beserta seluruh Bidang dan Seksi di bawahnya cukup dengan satu operasi kilat `WHERE unit_path LIKE '/01/0104/%'` tanpa kueri rekursif berlapis!
2. **Tabel Penugasan Mandat Jabatan (`position_mandates`)**:
   Memiliki kolom `user_id`, `position_id`, `mandate_type` (`DEFINITIF | PLT | PLH`), `valid_from`, `valid_until`, `decree_number` (Nomor SK), dan `is_active`. Pemeriksaan otorisasi selalu mengecek apakah pengguna memegang mandat aktif pada `NOW()` untuk jabatan yang berwenang.
3. **Kunci Utama Berurutan Waktu (`UUIDv7` atau `BIGINT`)**:
   Jika memakai UUID agar ID tidak mudah ditebak dari luar (mencegah enumerasi IDOR), gunakan **UUIDv7** (berurutan berdasarkan stempel waktu) sehingga penyisipan baris baru pada indeks B-Tree selalu rapi di ujung akhir dan tidak menyebabkan pembengkakan memori database (*index bloat*).
4. **Larangan Mutlak `OFFSET` Besar pada Tabel Transaksi**:
   Kueri `LIMIT 20 OFFSET 100000` memaksa database membaca dan membuang 100.000 baris setiap klik halaman! Gunakan **Keyset / Cursor Pagination**: `WHERE (created_at, id) < ($last_created_at, $last_id) ORDER BY created_at DESC, id DESC LIMIT 20`.

---

## 3. Standar Kontrak API, Idempotency & Konkurensi

### A. Amplop Respons & Galat Konsisten
Setiap respons galat wajib memiliki struktur mesin yang dapat langsung dipetakan oleh UI (termasuk menandai kolom formulir mana yang salah pada Kondisi ke-5 Layar):
```json
{
  "error": {
    "code": "BUREAUCRACY_STATE_CONFLICT",
    "message": "Berkas ini baru saja diparaf oleh pejabat lain 12 detik yang lalu.",
    "trace_id": "req_01J9XYZ...",
    "field_errors": {}
  }
}
```

### B. Perlindungan Klik Ganda & Konflik Edit
1. **Header `Idempotency-Key`**: Pada endpoint `POST` krusial (buat pengajuan, pencairan dana, terbitkan SK), klien mengirim UUID unik per niat klik. Jika jaringan putus dan klien mengirim ulang kunci yang sama dalam 24 jam, server mengembalikan hasil pertama tanpa mengeksekusi ulang transaksi!
2. **Parameter `expected_version`**: Pada endpoint perubahan status/edit (`PATCH`/`POST` aksi birokrasi), klien mengirimkan nomor `version` terakhir yang dilihat pengguna di layar. Server menjalankan `UPDATE ... SET status = $1, version = version + 1 WHERE id = $2 AND version = $expected_version`. Jika baris terpengaruh = `0`, kembalikan `409 Conflict` secara aman!

### C. Keamanan Otorisasi di Kontrak API
- **Jangan Pernah Percaya `user_id`, `role`, atau `unit_id` dari Body JSON Klien untuk Menentukan Hak Akses!** Identitas pelaku wajib diekstrak dari sesi/token terverifikasi di sisi server, dan untuk pengguna multi-jabatan (`Plt/Plh`), header/parameter `X-Acting-Mandate-Id` wajib divalidasi kepemilikannya terhadap tabel `position_mandates` aktif pada setiap permintaan!

