# Standar Audit Entropi Kode & Operasi Server Hemat Sumber Daya

Dokumen ini menjadi daftar periksa teknis Divisi SRE & Maintainability Steward (D-08) sebelum mengizinkan sebuah proyek dinyatakan lulus paripurna dari M-AEOS.

---

## 1. Lima Indikator Proyek "Mudah Dirawat" vs "Mimpi Buruk Maintenance"

| Aspek Pemeliharaan | Tanda Proyek Sehat M-AEOS (LULUS) | Tanda Proyek Beracun (WAJIB TOLAK / RAPIDKAN) |
| :--- | :--- | :--- |
| **Peta Perubahan Bisnis** | Menambah 1 status baru atau mengubah plafon persetujuan hanya menyentuh 1 modul terpusat / tabel kebijakan | Harus mencari & mengedit `if-else` string status yang tersebar di 18 file FE dan BE |
| **Ukuran & Fokus File** | Rata-rata file 80–220 baris; nama file mencerminkan tanggung jawab bisnisnya secara instan | Ada file `utils.ts`, `helper.go`, atau `Dashboard.tsx` sepanjang 1.400 baris berisi segala macam hal |
| **Konfigurasi Lingkungan** | Semua variabel `ENV` divalidasi skemanya saat nyala pertama & terdaftar lengkap beserta penjelasannya di `.env.example` | `process.env.XYZ` / `os.Getenv` tersebar acak di tengah fungsi dalam tanpa daftar dokumentasi |
| **Skrip Otomasi Proyek** | Perintah baku seragam (`dev`, `build`, `test`, `lint`, `migrate`) terdokumentasi jelas dan langsung jalan | Harus menjalankan 9 perintah manual dengan urutan rahasia yang hanya diketahui pembuat awal |
| **Ketergantungan Eksternal** | Sedikit, beralasan kuat, versi terkunci pasti (`lockfile` bersih), dan dibungkus adaptor tipis | Puluhan paket tumpang tindih (misal ada 2 library tanggal & 3 library tabel sekaligus!) |

---

## 2. Resep Menjalankan Produksi Mulus di Server Kecil (1–2 vCPU / 2 GB RAM)

Banyak instansi daerah, UMKM, dan startup awal menjalankan sistem di VPS hemat biaya. Gunakan alokasi anggaran memori berikut agar server tetap dingin dan responsif:
1. **Sistem Operasi + Reverse Proxy (Caddy / Nginx)**: ~60–100 MB RAM (aktifkan kompresi `zstd`/`gzip`, HTTP/2-3, dan header *cache* panjang `immutable` untuk aset statis ber-hash!).
2. **Proses Aplikasi Utama + Worker Ringan**: ~50–250 MB RAM (batasi memori maksimum runtime agar tidak bocor liar, misal `GOMEMLIMIT` pada Go atau `--max-old-space-size` wajar pada Node, serta batasi jumlah worker paralel pembuatan PDF).
3. **PostgreSQL Terkalibrasi Ramping**: `shared_buffers = 256MB–512MB`, `work_mem = 4MB–8MB`, `effective_cache_size = 1GB`, dengan ukuran *connection pool* aplikasi terbatasi rapi (`10–25` koneksi)—menyisakan ruang lega bagi *OS Page Cache* sehingga pembacaan indeks berlangsung dari RAM dalam hitungan mikrodetik!
4. **Rotasi Log Otomatis**: Batasi ukuran maksimal file log lokal/Docker (`max-size: 20m`, `max-file: 5`) agar hardisk server tidak pernah penuh diam-diam tengah malam setelah berjalan 6 bulan!

---

## 3. Wajib Ada: "Peta Modifikasi Cepat" untuk Developer Masa Depan

Di dalam `MAINTAINABILITY_AUDIT.md`, Anda **WAJIB** menyertakan tabel contekan praktis bagi engineer yang akan merawat sistem ini kelak:
- *"Jika ingin mengubah aturan syarat/alur persetujuan birokrasi → buka file `[...]`"*
- *"Jika ingin menambah kolom baru pada formulir & database → ikuti 4 langkah di `[...]`"*
- *"Jika ingin mengubah warna merek atau jarak komponen → ubah satu file token di `[...]`"*
- *"Jika pengguna melapor gagal memproses berkas → lacak dengan perintah log `[...]`"*

