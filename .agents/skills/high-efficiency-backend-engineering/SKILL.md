---
name: high-efficiency-backend-engineering
description: >-
  Playbook rekayasa Backend hemat resource (RAM/CPU rendah), arsitektur Modular Monolith yang
  mudah dirawat jangka panjang, penegakan mesin status birokrasi & RBAC/ABAC anti-bocor,
  pencegahan kueri N+1, konkurensi atomik/idempotency, serta pemrosesan asinkron untuk Divisi 05.
---

# Metodologi Rekayasa Backend Efisiensi Tinggi & Mudah Dirawat

Skill ini memastikan server aplikasi tidak membengkak pemakaian RAM/CPU-nya, bebas dari *bug* balapan transaksi (*race condition*), kedap terhadap manipulasi alur birokrasi, dan tetap rapi dipelihara bertahun-tahun.

---

## Tahap 1: Penataan Struktur Modular Kedap Air (*Zero-Spaghetti Setup*)

Wajib baca [arsitektur-modular-dan-mudah-maintenance.md](./references/arsitektur-modular-dan-mudah-maintenance.md) sebelum membuat struktur folder proyek:
1. Susun direktori berdasarkan **Modul Domain Bisnis** sesuai `01-ADR-DAN-TOPOLOGI-RINGAN.md`.
2. Di dalam setiap modul, pisahkan 4 tanggung jawab secara disiplin:
   - **Pintu Masuk (*Handler / Controller*)**: Hanya memvalidasi bentuk skema input dasar, mengekstrak konteks sesi, memanggil *Use-Case*, dan memetakan hasil/error ke kode status HTTP. **Maksimal ~50 baris per handler; dilarang menaruh logika bisnis atau SQL di sini!**
   - **Layanan Aplikasi (*Use-Case / Command-Query*)**: Mengatur batas transaksi database (`BEGIN ... COMMIT`), memverifikasi otorisasi jabatan + cakupan data, mengecek kunci *Idempotency*, memanggil aturan domain, dan menulis *Audit Trail*.
   - **Inti Domain & Mesin Status (*Domain & Policy*)**: Fungsi/objek murni yang menegakkan aturan transisi status birokrasi, rumus perhitungan uang/SLA, dan membaca nilai dari *Configurable Policy* (`CFG-XX`). Sangat mudah diuji unit tanpa database!
   - **Akses Data (*Repository / Query*)**: Berisi kueri terindeks yang eksplisit, bebas `SELECT *`, dan terbebas dari jebakan *lazy-loading* tersembunyi.

---

## Tahap 2: Migrasi Database Aman, Indeks & Mesin Kebijakan

1. Tulis file migrasi berurutan yang dapat dilacak versi perubahannya untuk membangun seluruh tabel, *foreign key*, *check constraint*, dan **seluruh indeks komposit ESR** yang telah dirancang di `02-SKEMA-DATABASE-DAN-INDEKS.md`.
2. Sediakan pengisi data awal (*seed*) yang bersih untuk struktur parameter kebijakan (`CFG-XX` dari SRS) dan daftar peran/unit contoh untuk pengujian tanpa mencampur data sampah ke mode produksi.
3. Validasi konfigurasi lingkungan (`ENV`) secara ketat pada detik aplikasi dinyalakan (*Fail-Fast Startup Validation*): jika kunci enkripsi, koneksi DB, atau parameter wajib kosong/salah format, server harus langsung menolak menyala dengan pesan jelas—jangan meledak di tengah transaksi pengguna!

---

## Tahap 3: Rekayasa Performa Server, Zero N+1 & Konkurensi Atomik

Wajib baca dan patuhi seluruh aturan teknis di [efisiensi-server-zero-n1-dan-konkurensi.md](./references/efisiensi-server-zero-n1-dan-konkurensi.md):
1. **Audit Kueri Ketat**: Setiap endpoint daftar wajib memakai *Batch Load / JOIN terukur* dan *Cursor Pagination* (atau batas `LIMIT` maksimum keras, misal `MAX_LIMIT = 100`—jangan pernah mengizinkan klien mengirim `?limit=999999` yang menumbangkan RAM server!).
2. **Keamanan Mutasi Konkuren**:
   - Gunakan pemeriksaan `version` (*Optimistic Locking*) atau `SELECT ... FOR UPDATE` terarah untuk transisi status birokrasi.
   - Gunakan pembaruan bersyarat atomik (`UPDATE budgets SET used = used + $amount WHERE id = $id AND (total - used) >= $amount`) untuk pemotongan kuota/stok/pagu agar **mustahil bernilai minus** walau dihantam 500 permintaan bersamaan!
3. **Idempotency Nyata**: Simpan sidik jari `Idempotency-Key` + `user_id` + rute endpoint beserta kode hasil transaksi sehingga pengiriman ulang akibat jaringan terputus ditangani mulus tanpa duplikasi data.

---

## Tahap 4: Keamanan Berlapis Sejak Baris Pertama (*Secure-by-Construction*)

1. **Parameterisasi Kueri 100%**: Dilarang keras merangkai string input pengguna ke dalam kueri SQL, perintah shell (`exec`), atau jalur sistem berkas (*path traversal*).
2. **Penyaringan Output (*DTO Projection — Zero Over-Posting/Leakage*)**: Jangan pernah mengembalikan objek baris tabel mentah langsung ke JSON respons API (yang bisa membocorkan `password_hash`, token internal, atau kolom `PII_SENSITIF`!). Selalu petakan ke struktur DTO respons sesuai kontrak API, dan samarkan kolom PII bagi peran yang tidak berhak melihat utuh.
3. **Penyamaian Waktu & Pembatasan Laju**: Gunakan perbandingan waktu konstan untuk verifikasi sandi/token (`argon2id` / `bcrypt` kuat), terapkan *rate limiter* pada endpoint sensitif, dan pastikan pesan galat `500` ke klien tidak pernah membocorkan *stack trace* internal atau struktur tabel database!
4. **Log Terstruktur Bersih Rahasia**: Cetak log berformat JSON terstruktur yang menyertakan `trace_id`, `user_id`, `mandate_id`, `duration_ms`, dan kode status—namun **saring ketat** agar sandi, token sesi, NIK, dan nomor rekening tidak pernah tertulis di log!

---

## Tahap 5: Verifikasi Mandiri Sebelum Menyerahkan ke Gate 3

Jalankan pengujian nyata menggunakan `run_command`:
1. Kompilasi / pemeriksaan tipe statis dan linter bersih tanpa peringatan.
2. Tulis dan jalankan **tes unit mesin status birokrasi** (memastikan transisi sah berhasil, lompatan status ilegal ditolak, dan pembuat tidak bisa menyetujui berkasnya sendiri).
3. Verifikasi rencana eksekusi kueri utama (`EXPLAIN` bila database aktif tersedia) dan lengkapi bagian backend pada `docs/project/04-quality-gates/GATE-3-ZERO-BLOAT.md`.

