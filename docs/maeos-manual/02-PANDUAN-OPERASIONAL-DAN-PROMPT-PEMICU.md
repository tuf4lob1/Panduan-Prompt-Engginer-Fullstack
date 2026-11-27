# Panduan Operasional Harian & Contekan Prompt Pemicu M-AEOS

Dokumen ini adalah buku saku praktis bagi Anda (sebagai *Fullstack Engineer / Product Owner / System Architect*) saat menggunakan template M-AEOS di Google Antigravity untuk berbagai jenis proyek.

---

## 1. Memulai Projek Baru dari Nol (Otomatis Masuk Gate 0)

Salin repositori template ini ke folder projek baru Anda, buka di Google Antigravity, lalu kirimkan brief awal sesuai skenario berikut:

### Skenario A: Sistem Pemerintahan / BUMN / Birokrasi Berlapis (`S3-Gov-Birokrasi`)
> *"Kita mulai projek baru menggunakan M-AEOS. Saya ingin membangun Sistem Pengajuan, Verifikasi, Disposisi, dan Pencairan Anggaran Kegiatan untuk Pemerintah Daerah. Aktornya mulai dari Staf Pelaksana di tiap Seksi, Kasubbag/Verifikator, Kepala Bidang, hingga Kepala Dinas (termasuk kondisi pejabat Plt/Plh), serta Inspektorat sebagai pemeriksa audit. Harus ringan dijalankan di VPS internal 2 vCPU 4 GB RAM, tampilannya sangat mudah dipahami staf segala usia tanpa banyak teks membingungkan, dan keamanannya super ketat. Jalankan Gate 0 sekarang."*

### Skenario B: Produk Startup / SaaS Komersial Cepat & Tajam (`S1-Startup` / `S2-Enterprise`)
> *"Kita mulai projek baru menggunakan M-AEOS. Saya ingin membuat platform SaaS manajemen operasional klinik & rekam medis multi-cabang. Fokus utamanya kecepatan kasir/dokter menginput data dalam hitungan detik, desain UI berkelas tinggi tidak generik AI, kode super ringan hemat biaya server, dan sangat mudah saya maintenance sendiri ke depannya. Jalankan Gate 0 sekarang."*

---

## 2. Perintah Kendali Cepat Saat Berkolaborasi per Gerbang

Anda memegang kendali penuh sebagai pemilik proyek pada titik keputusan strategis:

- **Menyetujui Gate 0 & Memicu Riset Mendalam Sistem A–Z**:
  > *"Profil skala di SCALE_PROFILE.md sudah tepat. Sahkan Gate 0, lalu kerahkan Divisi Analis (`principal-analyst`) untuk meriset sistem A–Z sampai tuntas ke edge-case dan birokrasinya."*
- **Menjalankan Pipeline Otomatis Analisis -> Arsitektur + Desain UI/UX**:
  > *"Gunakan workflow `workflows/blueprint_discovery_pipeline.wf` untuk menuntaskan spesifikasi analisis dilanjutkan perancangan arsitektur ringan dan desain UI/UX anti-generik secara paralel."*
- **Membekukan Desain & Memulai Eksekusi Koding (Membuka Kunci Gate Guard)**:
  > *"Saya menyetujui seluruh kontrak analisis (Gate 1), arsitektur ringan, dan spesifikasi desain UI/UX 7-kondisi (Gate 2). Tandai Gate 1 dan Gate 2 sebagai DISETUJUI/FROZEN di PROJECT_STATE.md, lalu kerahkan `principal-backend` dan `principal-frontend` untuk membangun sistem sesuai kontrak."*
- **Memicu Sidang Penguji Adversarial (Red-Team + QA Chaos + SRE)**:
  > *"Konstruksi selesai. Jalankan sidang penguji paralel menggunakan `workflows/adversarial_gate_tribunal.wf` untuk menguji pembobolan keamanan birokrasi, chaos QA, dan audit kemudahan maintenance."*

---

## 3. Menambah Fitur Baru pada Projek yang Sudah Berjalan

Ketika proyek sudah rilis (lulus Gate 6) dan bulan depan ada penambahan modul/fitur baru, jangan merusak kerapian kode dengan langsung menyuruh koding! Gunakan perintah ini:
> *"Saya ingin menambah modul baru: [jelaskan fitur]. Buka iterasi baru di PROJECT_STATE.md: minta `principal-analyst`, `principal-architect`, dan `principal-ux-designer` memperbarui bagian terkait di kontrak `docs/project/` terlebih dahulu agar tetap konsisten, ringan, dan aman sebelum kode diubah."*

---

## 4. Perbaikan Cepat Bug Darurat (*Hotfix Mode*)

Sesuai Pasal 1 Ayat 3 `AGENTS.md`, untuk proyek yang sudah lulus Gate 6 dan membutuhkan perbaikan *bug* terisolasi:
> *"Aktifkan Hotfix Mode untuk memperbaiki masalah spesifik berikut: [jelaskan gejala bug]. Lacak akar masalahnya, tulis tes regresi pembukti di QA, perbaiki secara bersih tanpa menambah bloat, dan pastikan tidak melanggar kontrak keamanan."*

