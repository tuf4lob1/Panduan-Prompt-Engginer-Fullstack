# Hukum Anti-AI-Slop & Rumus Anti-Teks-Penuh (Zero-Text-Wall Law)

Dokumen ini adalah saringan keras Gate 2 untuk memastikan antarmuka yang dirancang **tidak terlihat seperti buatan AI generik** dan **tidak membanjiri mata pengguna dengan teks berlebihan**.

---

## Bagian 1: Daftar Cekal 15 Ciri Desain Generik AI (*AI Slop Blacklist*)

Jika salah satu dari 15 pola di bawah ini muncul tanpa alasan fungsional yang sangat kuat, rancangan **OTOMATIS DITOLAK** di Gate 2:

1. **Palet Ungu-Indigo-Neon Default**: Memakai `#6366F1` / `#8B5CF6` dengan gradasi ungu-ke-biru di tombol, judul teks (*gradient text*), atau latar belakang tanpa kaitan identitas institusi/produk.
2. **Kotak Kartu Kembar Empat Berikon Bundar**: Deretan 4 kartu statistik di atas setiap halaman dengan ikon di dalam lingkaran warna pastel yang ukurannya semua sama tanpa pembedaan mana metrik paling kritis.
3. **Kalimat Sapaan & Basa-Basi Tak Berguna**: Banner lebar bertuliskan *"Selamat datang kembali, Budi! Berikut adalah ringkasan aktivitas pengelolaan data sistem informasi Anda hari ini agar lebih produktif."* (Membuang 180px ruang vertikal layar tanpa nilai kerja!).
4. **Paragraf Penjelasan di Atas Tabel/Form**: Menulis 3–4 kalimat untuk menjelaskan cara memakai tabel yang seharusnya sudah jelas dari label kolomnya.
5. **Efek Kaca Kabur (*Heavy Glassmorphism*) & Bola Cahaya Mengambang (*Blurred Glow Blobs*)** pada aplikasi bisnis/operasional/pemerintahan yang menuntut ketajaman baca tinggi.
6. **Kotak di Dalam Kotak (*Nested Card Mania*)**: Membungkus halaman dalam kartu, di dalamnya ada kartu seksi, di dalamnya lagi ada kartu item dengan bayangan tebal (*heavy drop-shadow*) berlapis-lapis.
7. **Pelangi Lencana (*Badge Rainbow*)**: Satu baris tabel memiliki 5 kapsul warna mencolok sekaligus (merah, kuning, biru, ungu, hijau) sehingga mata kehilangan sinyal bahaya yang sesungguhnya.
8. **Label Tombol Kabur**: Tombol bertuliskan `Submit`, `Proses`, `OK`, `Klik di Sini`, atau sebaliknya tombol terlalu panjang `Simpan dan Kirim Pengajuan Ini ke Kepala Bagian`. Gunakan **Kata Kerja + Objek Ringkas**: `Ajukan Berkas`, `Setujui Anggaran`, `Simpan Draf`.
9. **Ikon Dekoratif di Setiap Baris Label**: Menaruh ikon roket, bintang, kilat, atau emoji (`🚀`, `✨`, `📊`, `✅`) di seluruh antarmuka kerja profesional. **DILARANG memakai emoji sebagai pengganti ikon sistem yang konsisten!**
10. **Tata Letak Formulir 3–4 Kolom Menyamping Acak**: Memaksa mata pengguna melompat zig-zag kiri-kanan-bawah saat mengisi data. Gunakan alur vertikal 1 kolom bersih (hanya pasangkan berdampingan untuk pasangan alami pendek seperti `Tanggal Mulai` – `Tanggal Selesai` atau `RT` – `RW`).
11. **Tabel Raksasa Tanpa Prioritas Lebar Kolom**: Semua kolom dibagi rata sehingga kolom `No` lebarnya 150px sementara kolom `Perihal Surat` terpotong tinggal 2 kata!
12. **Modal Popup Bertumpuk di Atas Modal Lain (*Modal-on-Modal*)**: Membuka dialog di atas dialog lain. Gunakan *Slide-Over Drawer* samping atau halaman fokus penuh.
13. **Teks Rata Tengah (*Center-Aligned*) untuk Data Operasional atau Lebih dari 2 Baris**: Teks rata tengah menyulitkan pemindaian mata. Gunakan rata kiri untuk teks bacaan/label dan rata kanan untuk nominal angka.
14. **Pesan Kosong Mati (*Dead Empty State*)**: Hanya menampilkan tulisan abu-abu kecil `"Data tidak ditemukan"` di tengah layar putih kosong.
15. **Hero Marketing di Dalam Aplikasi Setelah Login**: Pengguna yang sudah masuk untuk bekerja langsung menginginkan meja kerja dan antrean tugasnya, bukan gambar ilustrasi besar dan slogan promosi!

---

## Bagian 2: Anggaran Kata Mikro Ketat (*Strict Microcopy Budget*)

Agar pengguna langsung paham sistem tanpa kelelahan membaca, patuhi batas kata berikut pada seluruh layar:

| Elemen Antarmuka | Batas Maksimal | Aturan Emas Penulisan |
| :--- | :--- | :--- |
| **Menu Navigasi Utama** | **1 – 2 kata** | Kata benda lugas: `Pengajuan`, `Disposisi`, `Anggaran`, `Laporan` (bukan `Manajemen Pengelolaan Data Pengajuan`) |
| **Judul Halaman (`H1`)** | **2 – 4 kata** | Langsung sebut objek/konteks: `Verifikasi Berkas`, `Detail Pengajuan #042` |
| **Subjudul Halaman** | **0 atau maks 10 kata** | **Hapus total** jika judul sudah jelas! Hanya pakai untuk info dinamis (misal: `12 berkas menunggu pemeriksaan Anda • 2 mendekati tenggat SLA`) |
| **Label Kolom Input / Tabel** | **1 – 3 kata** | Jelas tanpa singkatan membingungkan; letakkan satuan di dalam/samping kolom (`Nilai Pagu (Rp)`) |
| **Teks Bantuan Input (*Helper*)** | **0 atau maks 12 kata** | Hanya untuk syarat non-standar (misal: `PDF maks. 5 MB, sudah dibubuhi materai`) |
| **Label Tombol Aksi** | **2 – 3 kata** | Kata Kerja Aktif + Objek: `Terbitkan SK`, `Kembalikan Revisi`, `Unduh Rekap` |
| **Lencana Status (*Status Pill*)** | **1 – 3 kata** | Konsisten dengan Mesin Status: `Draf`, `Menunggu Paraf`, `Perlu Revisi`, `Terbit` |
| **Pesan Galat / Peringatan** | **Maks 16 kata** | Rumus: **[Apa yang salah] + [Cara memperbaiki]** (`Lampiran melebihi 5 MB. Kompres berkas PDF lalu unggah kembali.`) |

---

## Bagian 3: Enam Teknik Mengubah "Dinding Teks" Menjadi Pemahaman Instan

1. **Ganti Paragraf Penjelasan Alur → *Compact Visual Stepper***
   - *Buruk (Penuh Teks)*: *"Berkas Anda saat ini telah selesai diperiksa oleh Staf Verifikator pada tanggal 12 Mei dan sedang berada di meja Kepala Subbagian Keuangan untuk proses pemberian paraf sebelum diajukan ke Kepala Dinas."*
   - *Baik (Visual Instan)*: Pita 4 titik: `[✓ Diajukan 10 Mei] ── [✓ Verifikasi Teknis 12 Mei] ── [● Menunggu Paraf Kasubbag Keu] ── [○ Pengesahan Kadis]`
2. **Ganti Daftar Syarat Panjang di Atas Form → *Interactive Checklist Real-Time***
   - Tampilkan 3–4 poin syarat pendek yang berubah menjadi centang hijau otomatis begitu pengguna mengunggah berkas atau melengkapi kolom terkait.
3. **Ganti Kolom Tabel Penuh Kalimat → *Primary + Secondary Micro-Stack***
   - Di satu sel tabel, baris atas cetak agak tegas (`Perbaikan Jembatan Desa Sukamaju`), baris bawah ukuran kecil warna sekunder (`Dinas PU • Diajukan 2 jam lalu`). Hemat kolom, mudah dipindai!
4. **Gunakan *Progressive Disclosure* (Sembunyikan Detail Sekunder Hingga Diminta)**
   - Tampilkan 5 informasi inti yang dibutuhkan 90% waktu; letakkan histori lengkap 20 versi lama, metadata teknis, atau rincian pasal regulasi di dalam tab sekunder, baris lipat (*accordion*), atau panel geser samping (*drawer*).
5. **Gunakan Format Visual Mandiri (*Self-Formatting Data*)**
   - `Rp 125.000.000` dengan sisa pagu berbentuk batang progres tipis (`75% terpakai`) jauh lebih cepat dipahami otak dalam 0,5 detik dibandingkan kalimat *"Anggaran telah terpakai sebesar seratus dua puluh lima juta rupiah dari seratus enam puluh lima juta rupiah."*
6. **Gunakan Perbandingan Bersebelahan (*Visual Diff*) Saat Revisi Dokumen**
   - Saat pejabat memeriksa berkas yang habis direvisi pemohon, sorot langsung kolom mana yang berubah (`Rp 15.000.000` dicoret tipis → **`Rp 12.500.000`**) sehingga pemeriksa tidak perlu membaca ulang seluruh dokumen dari awal!

