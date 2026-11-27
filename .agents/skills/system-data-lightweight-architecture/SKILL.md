---
name: system-data-lightweight-architecture
description: >-
  Playbook riset arsitektur sistem ringan, pemilihan tech stack objektif lintas bahasa/platform,
  desain skema database & indeks komposit anti-lambat, arsitektur birokrasi/audit, serta
  perancangan kontrak API & topologi keamanan untuk Divisi 02 (Principal Architect).
---

# Metodologi Arsitektur Sistem Ringan, Data Presisi & Kontrak API

Skill ini memastikan fondasi teknis projek mampu berjalan sangat ringan di server hemat biaya sekalipun, tetap aman untuk birokrasi kompleks, dan memiliki batas modul bersih untuk pemeliharaan jangka panjang.

---

## Tahap 1: Riset Pemilihan Tech Stack Secara Objektif (Bebas Fanatisme)

1. Baca [matriks-pemilihan-techstack-ringan.md](./references/matriks-pemilihan-techstack-ringan.md).
2. Periksa apakah pengguna menetapkan **Batasan Keras Teknologi** di `SCALE_PROFILE.md`:
   - Jika **YA**, hormati pilihan tersebut, gunakan `search_web` untuk memastikan versi LTS/stabil terkini, dan fokuskan arsitektur pada cara paling ringan & bersih menjalankan stack tersebut.
   - Jika **TIDAK**, bandingkan minimal **2 kandidat stack terbaik** menggunakan tabel skor objektif berdasarkan: *(a) Konsumsi RAM/CPU server, (b) Kecepatan eksekusi & ukuran bundle klien, (c) Kecocokan dengan kompleksitas domain/birokrasi, dan (d) Kemudahan pemeliharaan oleh tim target*.
3. Catat setiap keputusan arsitektur besar dalam format **ADR (Architecture Decision Record)** di `01-ADR-DAN-TOPOLOGI-RINGAN.md` lengkap dengan alasan memilih dan konsekuensi yang diterima.

---

## Tahap 2: Dekomposisi Modul Internal (*Clean Bounded Contexts*)

Rancang struktur folder dan batas modul internal yang mencegah kode bercampur menjadi *Spaghetti*:
- Bagi sistem berdasarkan **Domain Bisnis** (misal: `modules/identitas-jabatan`, `modules/pengajuan`, `modules/anggaran`, `modules/audit`), **BUKAN** sekadar menumpuk 100 file di dalam satu folder `controllers/` dan `models/` raksasa!
- Tetapkan aturan komunikasi antar-modul: Modul A dilarang melakukan `UPDATE/INSERT` langsung ke tabel milik Modul B; ia harus memanggil antarmuka layanan publik Modul B agar aturan bisnis tetap terjaga di satu pintu.
- Pisahkan kode logika bisnis murni (*Domain & Policy Engine*) dari detail framework HTTP/ORM sehingga aturan birokrasi yang rumit dapat diuji unit dalam hitungan milidetik tanpa menyalakan server penuh.

---

## Tahap 3: Rekayasa Skema Database, Hierarki & Indeks Anti-Lambat

Wajib baca [rekayasa-database-indeks-dan-kontrak-api.md](./references/rekayasa-database-indeks-dan-kontrak-api.md) sebelum menulis `02-SKEMA-DATABASE-DAN-INDEKS.md`:
1. **Pemodelan Tabel Presisi**:
   - Tentukan kunci utama (`UUIDv7` berurutan waktu atau `BIGINT` — hindari `UUIDv4` acak murni pada indeks berklaster besar yang memecah halaman B-Tree!).
   - Gunakan tipe `BIGINT` (satuan terkecil) atau `NUMERIC(19,2)` untuk uang; `TIMESTAMPTZ` (UTC) untuk seluruh waktu.
   - Terapkan `version INTEGER NOT NULL DEFAULT 1` pada entitas transaksi/birokrasi untuk mencegah bentrokan edit bersamaan (*Optimistic Locking*).
2. **Dukungan Birokrasi, Kebijakan Dinamis & Jejak Audit**:
   - Jika profil `S2`/`S3`, sediakan struktur pohon organisasi efisien (misal *Materialized Path* / *Closure Table*), tabel penugasan jabatan berperiode (`Plt/Plh`), tabel parameter kebijakan (`system_policies`), dan tabel `audit_logs` yang hanya mengenal operasi `INSERT`.
3. **Peta Indeks Wajib (Zero Full-Table-Scan Law)**:
   - Setiap kolom kunci asing (`FOREIGN KEY`), filter antrean per status/unit, dan pencarian nomor/nama wajib dipetakan ke indeks spesifik dengan urutan kolom mengikuti hukum **ESR (Equality → Sort → Range)**.

---

## Tahap 4: Arsitektur Tugas Latar Belakang, File & Efisiensi Server

Cegah server membeku atau kehabisan memori (*OOM*) dengan aturan pemisahan beban berikut:
- **Apa yang Harus Sinkron (< 200 ms)**: Validasi input, perubahan status mesin birokrasi, pencatatan mutasi database, dan pembacaan data terindeks.
- **Apa yang WAJIB Asinkron (Antrean Pekerja / Background Worker)**: Pembuatan dokumen PDF resmi ber-QR/TTE, pengiriman email/WhatsApp/notifikasi keluar, rekapitulasi laporan besar, dan pemrosesan impor ribuan baris.
- **Manajemen Memori Streaming**: Untuk unduh/ekspor data besar atau unggah lampiran, wajib merancang pemrosesan berbasis aliran (*stream/chunk*)—dilarang memuat file 50 MB utuh ke dalam variabel RAM aplikasi!

---

## Tahap 5: Perancangan Kontrak API & Topologi Keamanan Berlapis

Tuangkan kontrak penghubung antara Backend dan Frontend secara tuntas di `03-KONTRAK-API-DAN-KEAMANAN.md`:
1. **Keselarasan Layar ke API (*Screen-Aligned Payloads*)**: Pastikan setiap layar utama di `03-design` bisa mendapatkan data awalnya secara efisien tanpa *waterfall request* beruntun, namun tetap bersih dan terstandar.
2. **Kontrak Mutasi Tahan Klik Ganda**: Wajibkan header `Idempotency-Key` atau pemeriksaan versi status pada seluruh *endpoint* pembuatan transaksi, pembayaran, persetujuan, dan disposisi.
3. **Kontrak Respons Error Terstandar**: Bedakan dengan tegas kode error validasi per kolom (`422`), konflik status birokrasi/versi (`409`), sesi habis (`401`), larangan wewenang jabatan (`403`), dan pembatasan laju permintaan (`429`).
4. **Benteng Keamanan Arsitektural**:
   - Mekanisme sesi/token, rotasi, dan pencabutan akses seketika (*instant revocation* saat pegawai diberhentikan/mutasi!).
   - *Rate Limiting* berlapis pada pintu login, lupa sandi, unggah berkas, dan ekspor data.
   - Penyimpanan berkas lampiran di luar folder publik web dengan akses terotorisasi per jabatan.

