# Arsitektur Rendering, State Bersih & Pencegahan Tampilan Lemot

Panduan ini memastikan aplikasi tetap gesit bahkan saat menampilkan ribuan data transaksi atau digunakan selama 8 jam kerja tanpa henti.

---

## 1. Mematikan "Request Waterfall" (Air Terjun Permintaan Beruntun)

Salah satu penyebab utama halaman terasa sangat lambat meskipun server cepat adalah pola air terjun di Frontend:
- **Pola Buruk (Dilarang)**: Halaman dimuat → unduh JS utama → cek profil user ke API → setelah selesai baru panggil API daftar unit → setelah selesai baru panggil API tabel pengajuan (Total waktu tunggu terbuang 4x lipat!).
- **Pola Standar M-AEOS**:
  1. Pada arsitektur SSR/Server Component, ambil sesi, konteks jabatan, dan data awal halaman **secara paralel (`Promise.all`) langsung di sisi server** dekat database!
  2. Pada navigasi sisi klien, jalankan pemanggilan independen secara paralel dan mulai *prefetch* data saat kursor mengarah/fokus pada tab antrean utama bila tepat guna.

---

## 2. Hukum URL sebagai Sumber Kebenaran Navigasi Kerja (*URL-Driven State*)

Pada sistem enterprise dan pemerintahan, pengguna sangat sering menyalin alamat URL untuk dikirim ke atasan/rekan (*"Pak, mohon cek daftar berkas macet di unit ini"*), atau menekan tombol *Back* setelah memeriksa satu berkas.
- **Wajib Disimpan di Parameter URL (`?status=MENUNGGU_PARAF&unit=04&q=...&cursor=...`)**:
  - Tab saringan aktif
  - Kata kunci pencarian (setelah *debounce* 250–300ms, menggunakan `replaceState` agar riwayat tombol *Back* tidak penuh sampah per huruf!)
  - Kolom urut & arah urut
  - ID berkas yang sedang dibuka di panel samping (*Split-Pane*: `?berkas=sub_01J9...` sehingga tautan langsung membuka panel berkas yang tepat!).
- **Dilarang Disimpan di Global Store**: Jangan menduplikasi isi respons tabel API ke dalam *global store* manual yang tidak sinkron ketika data berubah di server!

---

## 3. Mencegah Badai Render Ulang (*Re-render Storm*) & Lag Ketikan

1. **Isolasi Input Formulir Besar**:
   Pada formulir 30–100 kolom, jangan menaruh seluruh nilai ketikan pada satu variabel *state* di komponen paling atas yang memicu render ulang 100 komponen input setiap kali 1 tombol keyboard ditekan! Gunakan pengelola form berbasis langganan per kolom (*uncontrolled/field-level subscription*) atau pecah state per seksi bagian.
2. **Kewajiban Virtualisasi Baris & Penanganan Tabel Lebar**:
   - Jangan pernah me-render > 100 baris tabel kompleks (masing-masing punya 10 elemen DOM = > 1.000 node DOM!) sekaligus tanpa paginasi ketat (25–50 baris per halaman) atau **Virtualisasi Jendela (*Window Virtualization*)** bila memakai gulir panjang.
3. **Pencegahan Kebocoran Memori (*Memory Leak Zero-Tolerance*)**:
   Staf verifikator membuka aplikasi dari pukul 08.00 hingga 17.00 tanpa menutup tab browser. Pastikan setiap:
   - `addEventListener`, `ResizeObserver`, `IntersectionObserver`
   - `setInterval` / `setTimeout` (penghitung mundur SLA)
   - `URL.createObjectURL(blob)` (untuk pratinjau PDF/gambar lampiran!) → **WAJIB dipanggil `URL.revokeObjectURL()` saat pratinjau ditutup/berganti berkas!**
   - Koneksi SSE / WebSocket dan `AbortController` permintaan HTTP
   dibersihkan secara tuntas ketika komponen dilepas (*unmount*).

---

## 4. Pemulihan Draf Lokal (*Zero-Lost-Work*) & Penguncian Aksi

- Untuk formulir pengajuan panjang atau kotak penulisan catatan disposisi penting, simpan salinan draf sementara secara ringan di penyimpanan sesi lokal terikat ID pengguna & ID dokumen (jangan pernah menyimpan rahasia/PII mentah lintas akun di `localStorage`; bersihkan segera begitu server mengonfirmasi simpan sukses atau saat pengguna *logout*!).
- Setiap tombol aksi mutasi wajib beralih ke kondisi **Terkunci Memproses** pada milidetik pertama ditekan hingga respons server kembali, sehingga mustahil memicu pengiriman ganda dari klik tak sabar.

