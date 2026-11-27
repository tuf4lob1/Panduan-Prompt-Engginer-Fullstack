---
name: anti-slop-cognitive-ux-design
description: >-
  Playbook riset mendalam metode UI/UX, psikologi kognitif, paradigma tampilan modern,
  sistem desain anti-generik (Anti-AI-Slop), hukum anti-dinding-teks (Zero-Text-Wall),
  dan spesifikasi komponen 7-kondisi untuk Divisi 03 (Principal UX Designer) sebelum frontend dibuat.
---

# Metodologi Riset Desain UI/UX Kognitif & Sistem Anti-Generik

Skill ini memandu proses riset desain mendalam dari nol hingga menjadi cetak biru antarmuka berkelas dunia. Dilarang melompat langsung ke penentuan warna sebelum menyelesaikan Tahap 1 hingga Tahap 3.

---

## Tahap 1: Riset Ergonomi Pengguna & Konteks Pemakaian Nyata

Bedah setiap kelompok pengguna dari `01-DOMAIN-DAN-AKTOR.md` menggunakan empat lensa ergonomi:
1. **Durasi & Intensitas Sesi**:
   - *Pengguna Maraton (4–8 jam/hari, misal admin, kasir, analis verifikator)* → Membutuhkan kontras lembut yang tidak menyilaukan mata, kepadatan informasi tinggi tanpa banyak gulir (*scroll*), pintasan papan ketik (*keyboard navigation*), dan perpindahan antar-berkas secepat kilat.
   - *Pengguna Kilat Eksekutif (2–5 menit/sesi di sela rapat, misal Kepala Dinas, Direksi)* → Membutuhkan ringkasan intisari, sorotan anomali/risiko, pratinjau dokumen instan, dan tombol keputusan tegas di jempol.
   - *Pengguna Insidental / Publik (1–2 kali setahun, misal pemohon izin, pasien, pelanggan baru)* → Membutuhkan ketenangan visual, istilah sehari-hari yang ramah (bukan kode birokrasi internal), dan panduan langkah demi langkah.
2. **Kondisi Fisik & Perangkat**: Layar monitor kantor 1366x768 murah (bukan hanya MacBook Retina!), tablet kasir, atau ponsel Android di luar ruangan terik.
3. **Beban Emosional & Risiko Kesalahan**: Saat pengguna menyetujui pencairan Rp2 Miliar atau menolak berkas warga, desain harus menghadirkan rasa yakin melalui pratinjau dampak sebelum eksekusi (*Confirmation with Impact Summary*), bukan sekadar popup *"Apakah Anda yakin? Ya/Tidak"*.

---

## Tahap 2: Riset Metode UX & Pemilihan Paradigma Tampilan

1. Wajib baca [metode-dan-paradigma-uiux.md](./references/metode-dan-paradigma-uiux.md).
2. Bila domain projek memiliki referensi produk global/nasional terbaik, gunakan `search_web` untuk meneliti pola interaksi terbaik di bidang tersebut (misal: pola antarmuka rekam medis modern, pola *e-procurement* transparan, pola buku besar perbankan B2B, atau pola tata naskah dinas elektronik).
3. Pilih **Paradigma Tampilan Utama** dan **Paradigma Pendukung** (bisa berbeda antara portal warga/publik dengan ruang kerja internal staf!), lalu jelaskan alasan ilmiah pemilihannya di dokumen `01-RISET-UX-DAN-PARADIGMA.md`.

---

## Tahap 3: Pemodelan OOUX (Object-Oriented UX) & Pemangkasan Klik

Sebelum membuat daftar menu samping (*sidebar*), petakan **Objek Mental Utama** yang dipikirkan pengguna:
1. Apa benda utama yang dikerjakan pengguna? (Misal: *Berkas Usulan*, *Disposisi Masuk*, *Pagu Anggaran*).
2. Atribut kunci apa (maksimal 4–5 titik data!) yang membedakan satu objek dari objek lain saat dipindai cepat di daftar?
3. Aksi langsung apa yang paling sering dilakukan tanpa harus masuk ke tiga lapis halaman dalam?
4. **Hukum Kedalaman Klik (*Click-Depth Budget*)**: Tugas harian yang menyumbang 80% pekerjaan pengguna wajib dapat dijangkau dalam **maksimal 1–2 klik** sejak halaman kerja terbuka.

---

## Tahap 4: Audit Keras Anti-Teks-Penuh & Anti-AI-Slop

Wajib baca dan terapkan seluruh aturan di [hukum-anti-slop-dan-anti-teks-penuh.md](./references/hukum-anti-slop-dan-anti-teks-penuh.md):
- Terapkan **Anggaran Kata Mikro (*Strict Microcopy Budget*)** pada setiap komponen.
- Ubah setiap penjelasan alur birokrasi yang panjang menjadi **Jejak Visual Ringkas (*Visual Stepper / Compact Status Rail*)**.
- Ubah petunjuk pengisian formulir yang bertele-tele menjadi contoh format langsung (*placeholder* presisi, pemformatan input otomatis seperti pemisah ribuan Rupiah saat mengetik, dan pesan koreksi tepat di bawah kolom terkait).
- Pastikan tidak ada satu pun dari **15 Dosa Visual AI Slop** yang lolos ke spesifikasi desain Anda.

---

## Tahap 5: Perancangan Sistem Desain & Token Fungsional

Susun sistem visual yang beridentitas kuat dan matematis di `02-SISTEM-DESAIN-DAN-TOKEN.md`:
1. **Arah Karakter Visual (*Aesthetic Direction*)**: Rumuskan kepribadian antarmuka secara spesifik (misal: *"Kewibawaan Sipil Bersih — kertas hangat terang, tinta arang tajam, aksen biru samudra tua berwibawa, garis pembatas tipis 1px tegas"* — bukan warna default framework!).
2. **Palet Warna Berbasis Fungsi Semantik**:
   - Latar permukaan bertingkat (`surface-canvas`, `surface-card`, `surface-subtle`, `surface-elevated`)
   - Hierarki teks teruji kontras WCAG AA (`text-primary` rasio >= 7:1, `text-secondary` >= 4.5:1, `text-muted`)
   - Warna status birokrasi/transaksi yang dapat dibedakan bahkan oleh penderita buta warna parsial (selalu pasangkan warna status dengan **ikon bentuk berbeda + label singkat 1-2 kata**, jangan pernah mengandalkan bulatan merah/hijau saja!).
3. **Tipografi & Disiplin Angka**:
   - Pasangan fon yang memiliki keterbacaan UI unggul (bedakan huruf `I`, `l`, `1`, dan `0`, `O` dengan jelas untuk kode berkas/NIP/nomor surat!).
   - Wajib menetapkan aturan `font-variant-numeric: tabular-nums` pada seluruh nominal uang, tanggal, persentase, penghitung waktu SLA, dan nomor dokumen agar lurus sempurna dari atas ke bawah.
4. **Skala Spasi, Radius & Kepadatan**: Tetapkan unit dasar `4px` serta aturan kepadatan baris tabel/formulir sesuai profil pengguna.

---

## Tahap 6: Anatomi Komponen Kompleks & Spesifikasi Layar 7-Kondisi

Wajib baca [anatomi-komponen-kompleks.md](./references/anatomi-komponen-kompleks.md) lalu tuangkan rancangan detail setiap layar/alur di `03-SPESIFIKASI-LAYAR-7STATE.md`:
1. Gambarkan kerangka tata letak struktural (*ASCII Layout Blueprint*) dengan proporsi area yang jelas untuk Desktop dan Mobile.
2. Jelaskan anatomi komponen khusus domain (misal: *Panel Split-View Verifikasi Dokumen*, *Pita Status Birokrasi*, *Kartu Ringkasan Anggaran*, *Tabel Antrean Berprioritas SLA*).
3. **Kewajiban Mutlak 7 Kondisi Layar**: Untuk setiap layar utama, definisikan tampilan dan perilaku pada:
   - `(1) Kondisi Kosong Awal (Empty State)` — bukan teks pasif *"Tidak ada data"*, melainkan ilustrasi/ikon tenang + 1 kalimat alasan + tombol aksi mulai!
   - `(2) Kondisi Memuat (Skeleton Loading)` — kerangka bentuk asli komponen tanpa layar berkedip/melompat (*Zero CLS*).
   - `(3) Kondisi Ideal Terisi` — tampilan kerja normal paling efisien.
   - `(4) Kondisi Data Ekstrem (Overflow)` — nama orang/instansi 120 karakter, lampiran 25 berkas, catatan disposisi panjang, nominal triliunan Rupiah.
   - `(5) Kondisi Salah Input / Validasi Parsial` — penunjuk salah ketik yang sopan, spesifik, dan langsung mengarahkan kursor ke kolom bermasalah tanpa menghapus isian lain.
   - `(6) Kondisi Gangguan Jaringan / Server Sibuk` — indikator koneksi, pencegahan hilang ketikan (*local draft recovery*), dan tombol coba ulang aman.
   - `(7) Kondisi Terkunci Birokrasi / Read-Only` — penanda jelas mengapa dokumen tidak bisa diedit (misal: *"Terkunci — Sedang diperiksa Kepala Bidang sejak 14 Nov 10:20"*) beserta siapa pemegang bola saat ini.

