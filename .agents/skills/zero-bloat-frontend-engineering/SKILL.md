---
name: zero-bloat-frontend-engineering
description: >-
  Playbook riset mendalam dan eksekusi rekayasa Frontend ringan (Zero-Bloat) untuk Divisi 04.
  Mencakup pengadilan beban library pihak ketiga, strategi rendering (SSR/RSC/Islands/SPA),
  manajemen state bersih berbasis URL & server-cache, virtualisasi tabel besar, pencegahan
  memory leak browser, serta implementasi presisi Design Tokens & 7-kondisi layar.
---

# Metodologi Rekayasa Frontend Performa Tinggi & Zero-Bloat

Skill ini mencegah penyakit klasik aplikasi modern: ukuran unduhan JavaScript bengkak bermega-megabyte, kipas laptop berbunyi kencang saat mengetik di formulir, tabel lambat digulir, dan kode komponen berantakan yang mustahil dirawat.

---

## Tahap 1: Riset Ekosistem & Pengadilan Pustaka (*Dependency Court*)

Sebelum menambahkan **satu pun** paket baru ke `package.json` / `pubspec.yaml`:
1. Baca aturan cekal dan pengganti ringan di [pengadilan-library-dan-anggaran-bundle.md](./references/pengadilan-library-dan-anggaran-bundle.md).
2. Jika memerlukan pustaka khusus (misal penampil PDF, pemilih tanggal aksesibel, atau tabel virtual), gunakan `search_web` untuk memeriksa ukuran bundelnya, dukungan *tree-shaking* ESM, dan apakah paket tersebut masih aktif dirawat (bebas kerentanan keamanan).
3. Catat setiap pustaka pihak ketiga yang Anda pasang beserta alasan dan perkiraan ukurannya di `docs/project/04-quality-gates/GATE-3-ZERO-BLOAT.md`.

---

## Tahap 2: Pondasi Design Tokens & Komponen Primitif Bersih

Langkah koding pertama di Frontend **BUKAN** membuat halaman fitur, melainkan mengunci sistem dasar:
1. Terjemahkan seluruh variabel warna, skala spasi, radius, dan tipografi (`tabular-nums`!) dari `02-SISTEM-DESAIN-DAN-TOKEN.md` ke dalam variabel CSS terpusat (`tokens.css` / konfigurasi tema tunggal). **Dilarang menebar kode warna Hex mentah (`#...`) langsung di dalam puluhan file komponen!**
2. Bangun komponen dasar bermutu tinggi sekali saja untuk dipakai ulang di seluruh sistem:
   - `Button` (dengan dukungan status `isLoading` otomatis mengunci klik ganda!)
   - `Field / Input` (terintegrasi label aksesibel `htmlFor`, teks bantuan ringkas, dan pesan error `aria-invalid`)
   - `StatusBadge` (mengikat warna + ikon bentuk + label resmi sesuai Mesin Status)
   - `EmptyState`, `SkeletonBlock`, dan `ErrorBanner` (penopang standar 7-kondisi layar).

---

## Tahap 3: Arsitektur Rendering, State & Kinerja Anti-Lemot

Wajib baca dan terapkan pola teknis di [arsitektur-render-state-dan-anti-lemot.md](./references/arsitektur-render-state-dan-anti-lemot.md):
1. **Minimalkan JavaScript di Sisi Klien**: Jika menggunakan framework hybrid/SSR (seperti Next.js, SvelteKit, Nuxt, Astro), jadikan rendering server sebagai standar awal dan hanya tandai interaktivitas klien pada daun komponen (*leaf components*) yang benar-benar membutuhkan event klik/ketik.
2. **Pisahkan 4 Jenis State Secara Tegas**:
   - *URL Search Params* untuk seluruh filter tabel, pencarian, urutan kolom, tab aktif, dan kursor halaman (agar halaman tahan *refresh* dan tautannya bisa dikirim ke rekan kerja!).
   - *Server State Cache* (dengan deduplikasi permintaan & pembatalan `AbortController` otomatis saat berpindah halaman cepat).
   - *Form State Terisolasi* (agar mengetik 1 huruf di kotak catatan tidak merender ulang seluruh tabel 100 baris di sebelahnya!).
   - *Ephemeral UI State* lokal (buka/tutup *drawer* atau menu).
3. **Pemuatan Malas (*Code-Splitting / Dynamic Import*)**: Komponen kelas berat yang tidak langsung terlihat di detik pertama (Penampil PDF, Editor Teks Kaya, Grafik Analitik, Pemindai Kamera/QR) **WAJIB** dimuat secara dinamis (`lazy import`) agar layar utama tetap terbuka seketika.

---

## Tahap 4: Ketahanan Jaringan, Keamanan Klien & Aksesibilitas

1. **Pengiriman `Idempotency-Key` & `expected_version`**: Pastikan klien pembungkus API (*API Client*) otomatis menyertakan kunci idempotensi unik per aksi mutasi sehingga klik ulang saat sinyal terputus tidak menggandakan pengajuan/pencairan.
2. **Anti-XSS Mutlak**: Dilarang merender HTML mentah dari input pengguna (`dangerouslySetInnerHTML` / `v-html` / `{@html}`) tanpa penyaringan ketat berbasis daftar putih!
3. **Standar Navigasi Papan Ketik & Fokus**: Seluruh aksi utama, dialog konfirmasi, dan formulir harus dapat dioperasikan murni menggunakan `Tab`, `Shift+Tab`, `Enter`, dan `Escape` dengan indikator fokus yang terlihat jelas.

---

## Tahap 5: Verifikasi Mandiri Sebelum Menyerahkan ke Gate 3

Jalankan perintah verifikasi nyata menggunakan `run_command`:
1. Pemeriksaan tipe statis tanpa kompromi (nol `any` liar pada TypeScript; nol peringatan analisis statis).
2. Eksekusi *production build* untuk mengukur ukuran asli berkas aset/JS yang dihasilkan dan memastikannya masuk di bawah anggaran `SCALE_PROFILE.md`.
3. Periksa kembali bahwa ketujuh kondisi layar di `03-SPESIFIKASI-LAYAR-7STATE.md` benar-benar memiliki kode penanganannya di setiap halaman!

