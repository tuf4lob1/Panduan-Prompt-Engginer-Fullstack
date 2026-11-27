---
dokumen: Profil Skala, Tata Kelola & Anggaran Beban Projek
divisi_pembuat: D-00 (Chief Engineering Orchestrator)
gerbang_terkait: Gate 0
status: DRAF
versi: 1.0.0
terakhir_diperbarui: -
---

# Profil Skala & Anggaran Rekayasa Projek (Scale Profile)

## 1. Klasifikasi Utama Projek
- **Nama Sistem**: `[Isi nama projek]`
- **Domain Industri / Sektor**: `[Misal: SaaS Kesehatan / E-Government Pemda / ERP Logistik / Marketplace B2B]`
- **Tingkat Skala M-AEOS**: `[Pilih satu: S1-Startup | S2-Enterprise | S3-Gov-Birokrasi]`
- **Ringkasan Tujuan Utama (1 Paragraf)**:
  `[Jelaskan masalah nyata yang diselesaikan dan ukuran keberhasilan terukur]`

## 2. Profil Pengguna & Lingkungan Penggunaan
- **Kelompok Pengguna Primer**: `[Siapa yang paling sering memakai, tingkat melek digital, frekuensi harian]`
- **Kelompok Pengguna Sekunder / Penyetuju / Pengawas**: `[Manajer, Kepala Dinas, Auditor, Masyarakat Umum, dll.]`
- **Perangkat & Jaringan Dominan**: `[Desktop kantor layar lebar / HP Android kelas menengah / Lapangan sinyal tidak stabil]`

## 3. Kompleksitas Birokrasi & Kepatuhan Regulasi
- **Pola Persetujuan**: `[Tunggal / Maker-Checker / Berjenjang Multi-Eselon + Disposisi + Plt/Plh]`
- **Klasifikasi Data Tertinggi**: `[Publik / Internal / Rahasia Bisnis / Data Pribadi Spesifik UU PDP / Dokumen Negara]`
- **Regulasi / Standar Acuan**: `[Misal: UU PDP No. 27/2022, SPBE, ISO 27001, Standar Akuntansi, atau Kebijakan Internal]`
- **Kebutuhan Jejak Audit**: `[Standar / Ketat sebelum-sesudah tidak dapat dihapus]`

## 4. Anggaran Keringanan Infrastruktur & Performa (Hard Budgets)
- **Target Lingkungan Server**: `[Misal: VPS Linux 2 vCPU 2 GB RAM / On-Premise VM / Cloud Container]`
- **Batas Maksimal Pemakaian RAM Idle Backend**: `[Misal: <= 250 MB]`
- **Batas Ukuran Bundle JS Awal Frontend (Gzip)**: `[Misal: <= 120 KB untuk layar utama]`
- **Target Waktu Respons API P95**: `[Misal: <= 150 ms baca, <= 300 ms tulis transaksi]`
- **Tim Pemelihara Pasca-Rilis**: `[Solo Fullstack Engineer / Tim Kecil 2-5 Orang / Tim IT Instansi]`

## 5. Batasan Keras (*Hard Constraints*) dari Pemilik Projek
- **Preferensi / Kewajiban Teknologi (Jika Ada)**: `[Kosongkan bila diserahkan ke riset Divisi Arsitek]`
- **Integrasi Pihak Ketiga Wajib**: `[Misal: WhatsApp Gateway, Payment Gateway, SSO/LDAP, TTE BSrE, API Eksternal]`
- **Hal yang Dilarang Muncul**: `[Misal: Dilarang desain penuh teks, dilarang biaya cloud mahal, dilarang ketergantungan vendor terkunci]`

