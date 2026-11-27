# Katalog Vektor Serangan Birokrasi, Finansial & Aplikasi Modern

Gunakan daftar periksa serangan ini sebagai senjata pemeriksaan baris demi baris saat menyidang kode di Gate 4.

---

## 1. Sepuluh Celah Mematikan pada Sistem Pemerintahan, BUMN & Enterprise

| No | Nama Serangan | Cara Penyerang Mengeksploitasi | Bukti Kode Aman yang Wajib Anda Temukan |
| :--- | :--- | :--- | :--- |
| **1** | **IDOR Unduh Lampiran** | Mengubah ID lampiran pada `/api/attachments/9921/download` untuk mengunduh KTP/SK/kontrak milik pemohon lain | Endpoint unduh memverifikasi hak akses pengguna terhadap **dokumen induk** lampiran tersebut sebelum mengalirkan byte file |
| **2** | **Edit Dokumen Pasca-Ajukan (*Time-of-Approval Swap*)** | Saat Kepala Dinas sedang membuka layar pratinjau pengajuan Rp10 Juta, staf pembuat mengirim `PATCH` mengubah isi menjadi Rp100 Juta sedetik sebelum tombol `Setujui` ditekan | Endpoint edit memblokir keras perubahan ketika `status != 'DRAF' AND status != 'PERLU_REVISI'`, ditambah cek `expected_version` pada saat `Setujui` |
| **3** | **Penyalahgunaan Mandat Kedaluwarsa** | Pejabat yang masa `Plh`-nya berakhir pukul 23:59 tadi malam masih memakai sesi login aktifnya pagi ini untuk menyetujui surat | Kueri validasi mandat memeriksa `valid_until >= NOW() AND is_active = true` langsung di setiap aksi tulis, bukan dari klaim JWT basi |
| **4** | **SQL Injection lewat `sort_by` / `filter`** | Mengirim `?sort=created_at;DROP TABLE--` karena developer merangkai string `ORDER BY ${req.query.sort}` | Kolom `ORDER BY` divalidasi ketat menggunakan peta daftar putih (*strict allowlist map*), tidak pernah dirangkai mentah |
| **5** | **Manipulasi Angka Negatif / Nol** | Mengirim jumlah barang `-5` atau nilai transfer `-1000000` sehingga rumus pengurangan saldo justru **menambah** saldo penyerang! | Skema validasi input + constraint domain mewajibkan kuantitas/nominal `> 0` dengan batas atas masuk akal |
| **6** | **SVG / Filename XSS pada Lampiran** | Mengunggah berkas bernama `"><script>...pdf` atau berkas gambar `.svg` berisi JavaScript yang tereksekusi saat dibuka admin | Nama berkas asli disanitasi & tidak dipakai sebagai path penyimpanan; unduhan diberi header `Content-Disposition: attachment` & `X-Content-Type-Options: nosniff` |
| **7** | ** Manipulasi Jejak Audit** | Admin aplikasi mencoba menghapus baris jejak pelanggaran lewat endpoint internal atau kueri aplikasi | Tidak ada satu pun fungsi `UPDATE` atau `DELETE` terhadap tabel `audit_logs` di seluruh repositori kode! |
| **8** | **Serangan Enumerasi Akun & Brute-Force** | Mencoba ribuan sandi atau kode OTP 6 digit tanpa batas percobaan | *Rate limit* ketat per IP + per akun target, penguncian tunda eksponensial, dan pesan gagal login yang tidak membocorkan daftar akun |
| **9** | **Pemalsuan Identitas Proxy (`X-Forwarded-For` Spoofing)** | Mengirim header `X-Forwarded-For: 127.0.0.1` palsu untuk melewati pembatas laju (*rate limiter*) dan memalsukan IP di log audit | Server hanya memercayai header proxy dari daftar IP *reverse-proxy* internal tepercaya (*Trusted Proxies*) |
| **10** | **DoS Ekspor Laporan / Pencarian Regex** | Memicu 10 permintaan ekspor laporan 5 tahun sekaligus untuk membuat server kehabisan RAM (`OOM Kill`) | Pembatasan rentang tanggal maksimal, antrean asinkron terbatasi per pengguna, dan kueri pencarian aman |

---

## 2. Kriteria Penilaian Keparahan Temuan (Severity Rubric)

- **`KRITIS` (Wajib Blokir Rilis)**: Pembobolan autentikasi, IDOR lintas unit/tenant pada data rahasia/uang, eksekusi kode/SQL injection, lompatan pengesahan birokrasi tanpa wewenang, korupsi saldo/pagu karena *race condition*, kunci rahasia produksi bocor di repo.
- **`TINGGI` (Wajib Blokir Rilis)**: Kebocoran kolom `PII_SENSITIF` di respons API atau log server, XSS tersimpan, ketiadaan *rate-limit* pada pintu login/OTP, dokumen terkunci masih bisa diedit sebagian, jejak audit tidak terekam pada aksi penting.
- **`SEDANG` (Wajib Diperbaiki Sebelum Gate 6 atau Diterima dengan Mitigasi)**: Header keamanan HTTP kurang lengkap, pesan error terlalu teknis, batas ukuran payload belum diketatkan pada rute non-kritis.
- **`RENDAH` (Penyempurnaan Pertahanan Mendalam)**: Saran penguatan konfigurasi tambahan tanpa dampak eksploitasi langsung.

