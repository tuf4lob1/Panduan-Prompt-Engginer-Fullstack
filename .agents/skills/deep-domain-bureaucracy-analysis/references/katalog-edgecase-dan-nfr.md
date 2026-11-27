# Katalog Skenario Edge-Case Lintas Domain & Standar NFR

Gunakan daftar periksa ini saat menyusun `03-SRS-DAN-KONTRAK-LOGIKA.md` agar sistem tahan banting sejak hari pertama diluncurkan.

---

## 1. Tujuh Kategori Edge-Case yang Paling Sering Melumpuhkan Produksi

### A. Konkurensi, Klik Ganda & Balapan Data (*Race Conditions*)
1. **Klik Ganda pada Koneksi Lambat**: Pengguna menekan tombol *"Bayar"*, *"Setujui"*, atau *"Kirim Pengajuan"* 3 kali karena layar terasa diam. **Aturan Wajib**: Setiap aksi mutasi penting wajib bersifat *idempotent* (menggunakan kunci unik permintaan atau penguncian status optimis/pesimis).
2. **Dua Pejabat Menindaklanjuti Berkas yang Sama Bersamaan**: Dua verifikator di satu tim membuka berkas yang sama; satu klik *Setuju*, satu detik kemudian rekannya klik *Kembalikan Revisi*. **Aturan Wajib**: Validasi versi status terbaru (*Optimistic Concurrency Control / `version` check*); tolak aksi kedua dengan pesan jelas bahwa berkas baru saja diproses rekan kerja.
3. **Perebutan Kuota / Stok / Sisa Anggaran Terakhir**: Sisa kuota tinggal 1 kursi atau sisa anggaran tinggal Rp5.000.000, lalu ada 10 pengajuan masuk serentak. **Aturan Wajib**: Pemeriksaan dan pengurangan saldo wajib terjadi secara atomik di dalam satu transaksi database dengan penguncian baris/syarat batas (`WHERE sisa >= nilai_diminta`).

### B. Uang, Kuantitas & Perhitungan Matematika
1. **Haram Menggunakan `Float` untuk Uang**: Bilangan pecahan biner (`float`/`double`) menyebabkan selisih Rp0,01 yang merusak rekonsiliasi keuangan. **Aturan Wajib**: Seluruh nilai mata uang wajib disimpan sebagai bilangan bulat satuan terkecil (`BIGINT`) atau desimal presisi tetap (`NUMERIC/DECIMAL`), lengkap dengan aturan pembulatan resmi (misal *Half-Even* atau pembulatan ke bawah sesuai aturan pajak).
2. **Selisih Pembulatan Diskon/Pajak per Baris vs Total Akhir**: Tentukan secara eksplisit di SRS apakah PPN/potongan dihitung per item lalu dijumlahkan, atau dijumlahkan subtotalnya dulu baru dikali tarif pajak.

### C. Waktu, Tanggal, Batas Akhir (*Cut-off*) & Zona Waktu
1. **Multi-Zona Waktu Indonesia (WIB, WITA, WIT)**: Jika batas akhir pengumpulan berkas adalah *"30 November pukul 23:59"*, zona waktu mana yang menjadi acuan hukum (WIB pusat atau waktu lokal cabang)? **Aturan Wajib**: Simpan seluruh waktu dalam UTC di server, dan nyatakan zona waktu aturan batas akhir secara tegas di SRS.
2. **Tanggal Mundur (*Backdating*) & Tahun Anggaran Tutup Buku**: Bolehkan staf menginput transaksi tertanggal bulan/tahun lalu yang laporannya sudah ditutup? Tetapkan aturan penguncian periode (*Period Closing Lock*).
3. **Perhitungan SLA Hari Kerja vs Hari Kalender**: Jika SLA verifikasi adalah 3 hari kerja dan berkas masuk Jumat sore menjelang libur nasional, kapan tenggat eskalasinya?

### D. Integrasi Eksternal, Unggah Berkas & Proses Massal
1. **Layanan Pihak Ketiga Mati / Lambat**: Apa yang terjadi pada transaksi utama jika layanan kirim email/WhatsApp, tanda tangan elektronik (TTE), atau sinkronisasi API luar sedang *timeout*? **Aturan Wajib**: Pisahkan pencatatan transaksi inti dari pengiriman notifikasi/sinkronisasi eksternal menggunakan pola antrean ulang (*Retryable Outbox/Queue*) dengan status tunggu yang transparan bagi pengguna.
2. **Keamanan & Batas Unggah File**: Jangan hanya mengecek ekstensi `.pdf` atau `.jpg`! Tetapkan batas ukuran maksimal per file, validasi tipe konten asli (*Magic Bytes*), penggantian nama file acak yang aman (mencegah *path traversal*), dan izin unduh berautentikasi (file dokumen internal/pribadi **dilarang keras** ditaruh di folder publik yang bisa ditebak URL-nya!).
3. **Impor / Ekspor Data Ribuan Baris**: Impor Excel 20.000 baris harus mendefinisikan aturan: apakah *All-or-Nothing* (batal semua bila ada 1 baris salah, disertai laporan baris ke berapa yang salah) atau *Partial Import* (proses yang valid, unduh daftar baris gagal)? Ekspor besar wajib dibatasi atau diproses di latar belakang agar tidak menghabiskan RAM server (*Out of Memory*).

### E. Siklus Hidup Data & Jebakan Penghapusan (*Deletion Traps*)
1. **Penghapusan Data Master yang Sudah Dipakai Transaksi**: Jika sebuah Unit Kerja, Kategori Biaya, Produk, atau Akun Pegawai pernah terkait dengan 1 saja transaksi historis, penghapusan fisik (`DELETE`) wajib dilarang! Gunakan status aktif/nonaktif (`is_active = false` / `archived_at`) dan pastikan laporan lama tetap menampilkan nama historis yang benar.
2. **Perubahan Harga / Tarif / Nama Jabatan Seiring Waktu**: Jika harga barang atau nama dinas berubah tahun ini, faktur atau SK tahun lalu **tidak boleh ikut berubah nilainya** saat dibuka kembali! Tandai atribut mana yang harus disalin sebagai *historical snapshot* pada tabel transaksi.

---

## 2. Standar Kebutuhan Non-Fungsional (NFR) yang Wajib Terukur

Hindari kalimat NFR palsu seperti *"Sistem harus cepat, aman, dan mudah digunakan"*. Gunakan metrik terukur berikut:

- **Kapasitas & Beban**: Perkiraan jumlah pengguna terdaftar, pengguna aktif bersamaan (*concurrent active users*) pada jam puncak (misal: akhir bulan / penutupan pendaftaran), serta estimasi pertumbuhan baris tabel terbesar per tahun.
- **Anggaran Respons**: Target latensi halaman utama, pencarian/filter tabel besar, dan penyimpanan formulir.
- **Ketersediaan & Pemulihan**: Toleransi kehilangan data maksimal jika server mati mendadak (*RPO*) dan target waktu pulih (*RTO*).
- **Matriks Klasifikasi Privasi Data**:
  - `PUBLIK`: Boleh tampil tanpa login.
  - `INTERNAL`: Hanya pengguna terautentikasi sesuai unit/peran.
  - `RAHASIA_TERBATAS`: Hanya jabatan spesifik; wajib dicatat di log setiap kali dibuka/diunduh.
  - `PII_SENSITIF`: Wajib dienkripsi/di-hash secara tepat, disamarkan di layar daftar (*misal: `3201********0001`*), dan **dilarang keras** tercetak di log aplikasi.

