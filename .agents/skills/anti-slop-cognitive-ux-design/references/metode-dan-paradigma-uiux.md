# Ensiklopedia Metode Psikologi UX & 8 Paradigma Tampilan Non-Generik

Dokumen ini menjadi landasan ilmiah Divisi Desain UI/UX M-AEOS dalam meriset dan memilih konsep antarmuka yang paling tepat bagi setiap projek.

---

## Bagian A: 10 Metode & Hukum Ergonomi Kognitif yang Wajib Diterapkan

1. **Jobs-to-be-Done (JTBD)**: Pengguna tidak "ingin memakai fitur filter tabel"; mereka ingin *"menemukan 3 berkas yang tenggat SLA-nya habis sore ini agar tidak ditegur pimpinan"*. Rancang pintasan filter satu klik (`Jatuh Tempo Hari Ini (3)`) alih-alih menyuruh mereka merakit 4 dropdown pencarian setiap pagi!
2. **Object-Oriented UX (OOUX)**: Pastikan satu objek bisnis (misal `Berkas Pengajuan`) selalu tampil dengan anatomi pengenal yang konsisten di mana pun ia muncul (di tabel antrean, di notifikasi, di layar detail, maupun di riwayat audit).
3. **Hukum Hick (*Hick's Law*)**: Waktu mengambil keputusan meningkat drastis seiring bertambahnya jumlah pilihan yang setara di layar. Batasi pilihan aksi utama di satu waktu; kelompokkan aksi jarang pakai ke dalam menu sekunder (`...`).
4. **Hukum Fitts (*Fitts's Law*)**: Waktu menjangkau tombol bergantung pada ukuran tombol dan jaraknya dari posisi kursor/jempol. Letakkan tombol aksi berurutan dekat dengan area baca terakhir; beri ukuran sentuh minimal `44x44px` (ideal `48px`) di perangkat bergerak.
5. **Hukum Pengelompokan Miller (*Chunking*)**: Memori kerja manusia hanya nyaman memindai **4 hingga 6 kelompok informasi** sekaligus. Formulir 35 kolom wajib dikelompokkan menjadi blok-blok logis berisi 4–6 kolom per blok, bukan daftar panjang tak berujung.
6. **Hukum Tesler (*Conservation of Complexity*)**: Setiap proses punya kerumitan bawaan yang tak bisa dihapus, hanya bisa dipindahkan—antara dipikul sistem atau dipikul pengguna. **Pindahkan ke sistem**: isi otomatis nama unit kerja dari sesi login, hitung pajak/total otomatis secara instan, deteksi kode pos ke kelurahan/kecamatan otomatis.
7. **Prinsip Gestalt (*Proximity & Common Region*)**: Gunakan jarak ruang kosong (*whitespace*) untuk mengelompokkan elemen yang berhubungan, alih-alih membungkus setiap potongan kecil informasi dengan garis kotak di dalam kotak di dalam kotak (*Nested Box Hell*).
8. **Hukum Jakob (*Jakob's Law*)**: Berinovasilah pada kejelasan alur kerja dan estetika bersih, namun jangan mengubah letak elemen standar yang sudah mendarah daging (kolom cari, keluar akun, tombol kembali, navigasi utama) hingga membuat pengguna tersesat.
9. **Poka-Yoke (Desain Anti-Kesalahan Tak Sengaja)**: Cegah kesalahan sebelum terjadi. Nonaktifkan atau pisahkan jauh tombol `Tolak Permanen` dari tombol `Setujui`; minta konfirmasi khusus hanya untuk aksi yang **tidak dapat dibatalkan**.
10. **Uji Sipit 3 Detik (*3-Second Squint Test*)**: Jika layar diburamkan atau dilihat dengan mata menyipit, apakah satu titik fokus utama, pengelompokan bagian, dan status dokumen langsung terlihat kontras? Jika semua elemen tampak sama tebal dan sama besar, hierarki gagal!

---

## Bagian B: 8 Paradigma Tampilan UI/UX Kelas Dunia (Pilih Sesuai Karakter Sistem)

Jangan pernah memakai satu gaya tampilan untuk semua jenis aplikasi! Pilih kombinasi paradigma berikut berdasarkan hasil riset pengguna:

### 1. *Precision Operational Workbench* (Inspirasi: Linear, Raycast, GitHub Issues Baru)
- **Cocok Untuk**: Aplikasi kerja staf harian intensitas tinggi, SaaS B2B produktivitas, manajemen tiket/tugas/inventaris, admin panel modern.
- **Ciri Khas Visual & Interaksi**: Garis batas super tipis (`1px hairline`), tipografi ringkas nan tajam (`13px–14px` untuk data tabel), pemakaian warna sangat hemat (netral monokrom tenang, warna cerah **hanya** muncul pada status penting & tombol primer), transisi instan tanpa animasi lambat, dukungan *Command Bar* (`Ctrl+K` / `/`) untuk lompat cepat.

### 2. *Master-Detail Split Triage* (Inspirasi: Superhuman, PACS Medis, Meja Kerja Verifikator Modern)
- **Cocok Untuk**: **Sistem Birokrasi, Verifikasi Berkas, E-Office Disposisi Surat, Klaim Asuransi, Moderasi, Seleksi Lamaran/Tender.**
- **Mengapa Revolusioner**: Di sistem konvensional yang buruk, verifikator harus: *Buka tabel → Klik baris → Tunggu halaman detail muat → Klik unduh PDF → Buka tab baru → Kembali ke tab lama → Klik Setuju → Kembali ke tabel → Ulangi 100 kali!* Dengan paradigma *Split Triage*, daftar antrean ada di lajur kiri sempit, dokumen/rincian langsung terbuka di panel tengah, dan panel keputusan/catatan paraf menempel di kanan. Selesai ketuk `Setujui`, otomatis melompat ke berkas berikutnya!

### 3. *Radical Civic Clarity* (Inspirasi: GOV.UK, Singpass, MijnOverheid)
- **Cocok Untuk**: Layanan publik masyarakat umum, pendaftaran warga, perizinan daring, layanan kesehatan pasien, pengguna lintas usia & perangkat sederhana.
- **Ciri Khas Visual & Interaksi**: Prinsip *"Satu Hal Penting per Layar"*, rasio kontras teks ekstrem tajam (hitam pekat di atas putih bersih), ukuran huruf nyaman (`16px–18px`), tombol aksi sangat jelas, tanpa jargon teknis, sangat hemat kuota internet dan cepat di ponsel murah.

### 4. *Calm Financial & Ledger Precision* (Inspirasi: Wise, Mercury, Stripe Billing)
- **Cocok Untuk**: Sistem anggaran daerah/negara, akuntansi, kasir/POS, perbankan, penggajian, manajemen aset & pengadaan.
- **Ciri Khas Visual & Interaksi**: Angka nominal selalu rata kanan dengan `tabular-nums`, pemisahan visual mutlak antara dana keluar vs masuk vs ditahan (*reserved*), kartu ringkasan saldo bersih tanpa grafik hiasan yang membingungkan, dan pratinjau kalkulasi *real-time* sebelum transaksi disimpan.

### 5. *Guided Progressive Document Canvas* (Inspirasi: Notion Forms, TurboTax, Stripe Onboarding)
- **Cocok Untuk**: Pengajuan dokumen kompleks berpuluh-puluh kolom (proposal hibah, pelaporan pajak/LKPM, rekam asesmen medis lengkap, penyusunan KAK/kontrak).
- **Ciri Khas Visual & Interaksi**: Navigasi bab di sisi samping dengan indikator centang progres per bagian, penyimpanan draf otomatis di latar belakang (*"Tersimpan otomatis 5 detik lalu"*), kemampuan melompat antar-bab yang belum lengkap, serta halaman **Pratinjau Cetak Resmi** sebelum tombol kirim akhir ditekan.

### 6. *Executive Signal & Exception Cockpit* (Inspirasi: Bloomberg Modern / Apple Health Summary / Linear Insights)
- **Cocok Untuk**: Dashboard Kepala Dinas, Menteri, CEO, Direktur Operasional, Kepala Cabang.
- **Ciri Khas Visual & Interaksi**: Bukan kumpulan 12 grafik warna-warni yang memusingkan! Fokus pada **3–4 Angka Indikator Kunci beserta arah perubahan (`+12% dari bulan lalu`)**, diikuti daftar **Pengecualian yang Butuh Tindakan Segera** (*"4 Berkas Melewati Batas SLA"*, *"2 Unit Kerja Hampir Habis Pagu"*), di mana setiap angka bisa diklik langsung menuju daftar sumbernya (*Drill-down*).

### 7. *Field-First High-Contrast Mobile* (Inspirasi: Aplikasi Kurir/Inspeksi Lapangan Kelas Industri)
- **Cocok Untuk**: Petugas survei lapangan, teknisi pemeliharaan, petugas gudang, absensi/patroli, perawat keliling.
- **Ciri Khas Visual & Interaksi**: Dirancang untuk dioperasikan **satu jempol sambil berdiri**, target ketuk besar (`>= 48px`), kontras tinggi terbaca di bawah sinar matahari, input berbasis pilih cepat/kamera/pindai QR alih-alih mengetik panjang, serta indikator status sinkronisasi *offline-to-online* yang jujur di bagian atas layar.

### 8. *Spatial State-Board & Visual Pipeline* (Inspirasi: papan alur produksi & pelacakan logistik modern)
- **Cocok Untuk**: Pelacakan tahapan proyek konstruksi/pengadaan, antrean pelayanan klinik/bengkel, alur produksi pabrik.
- **Ciri Khas Visual & Interaksi**: Kolom tahapan merepresentasikan *State Machine* nyata, setiap kartu hanya memuat maksimal 4 potong data vital (Kode, Judul Singkat, Penanggung Jawab, Sisa Waktu SLA).

