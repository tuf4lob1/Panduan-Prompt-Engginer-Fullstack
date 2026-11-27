# Pengadilan Pustaka Frontend (Dependency Court) & Anggaran Bundle

Dokumen ini menjadi pedoman keras untuk menjaga antarmuka tetap ringan di jaringan lambat maupun perangkat berspesifikasi rendah.

---

## 1. Daftar Pustaka Berat Terlarang vs Pengganti Native / Ultra-Ringan

| Kebutuhan Fitur | DILARANG Dipasang (Bloat!) | Solusi Standar M-AEOS (0 KB s/d Super Ringan) | Penghematan Beban |
| :--- | :--- | :--- | :--- |
| **Format Rupiah, Angka & Tanggal Tampil** | `moment.js`, `numeral`, atau memuat seluruh locale `dayjs`/`date-fns` sekaligus | **Native `Intl.NumberFormat('id-ID')` & `Intl.DateTimeFormat('id-ID')` / `Intl.RelativeTimeFormat`** (bila butuh hitung hari kerja saja, impor fungsi tunggal spesifik!) | Hemat **30–70 KB** gzip |
| **Manipulasi Array / Objek (`debounce`, `groupBy`, `clone`)** | `lodash` utuh (`import _ from 'lodash'`) | **Native JS (`Object.groupBy`, `structuredClone`, `Array.at`)** + fungsi utilitas `debounce` 10 baris di folder internal | Hemat **24–70 KB** gzip |
| **Pemanggilan HTTP / REST API** | `axios` (kecuali ada syarat khusus legacy) | **Native `fetch` + `AbortController`** dibungkus modul internal tipis (~40 baris) untuk injeksi header, error, & *idempotency* | Hemat **13–15 KB** gzip |
| **Pembuatan UUID / Kunci Idempotensi** | Paket `uuid` eksternal untuk klien modern | **Native `crypto.randomUUID()`** bawaan browser | Hemat **3–8 KB** |
| **Ikon Antarmuka** | Memuat paket fon ikon raksasa 2 MB atau `import * as Icons` yang menggagalkan *tree-shaking* | Impor SVG spesifik per ikon yang dipakai saja atau *sprite SVG* bersih (maksimal ukuran 1 set ikon halaman < 8 KB) | Hemat **50–300 KB** |
| **Animasi Transisi Panel / Drawer / Skeleton** | Memasang mesin fisika animasi JS besar (>35 KB gzip) hanya untuk geser menu & pudar halus | **CSS Transitions / `@keyframes` pada properti GPU (`transform`, `opacity`)** + penghormatan `prefers-reduced-motion` | Hemat **35–65 KB** + 60fps stabil |
| **Tata Letak Responsif & Dialog Popup** | Pengukur lebar layar JS pada `window.onresize` atau library modal berlapis | **CSS Grid, Flexbox, Container Queries (`@container`), dan elemen `<dialog>` / Popover standar** | Nol beban CPU saat layar diubah ukurannya |

---

## 2. Anggaran Ukuran & Kecepatan Render (Target Lulus Gate 3)

Mengacu pada profil skala di `SCALE_PROFILE.md`, jaga metrik produksi pada batas berikut:
- **Bundel JS Awal Kritis (*Initial Route Gzip*)**:
  - Aplikasi Server-Driven / Portal Publik (`S3` Warga / `S1` Ringan): **<= 35 KB gzip**
  - Aplikasi Workspace Interaktif / SPA / Hybrid (`S1` / `S2` / `S3` Internal): **<= 120 KB gzip**
- **Pecahan Modul Malas (*Lazy Chunk* per Fitur Berat)**: Setiap komponen berat (seperti pratinjau PDF atau grafik laporan) berdiri di berkas *chunk* terpisah dan baru diunduh saat pengguna membuka layar tersebut.
- **Kinerja Interaksi (*Interaction to Next Paint / INP*)**: **< 100 ms** (tidak boleh ada pembekuan ketikan atau klik tombol).
- **Pergeseran Tata Letak (*Cumulative Layout Shift / CLS*)**: **0.00** — seluruh gambar, kerangka *skeleton*, pita status, dan tabel wajib memiliki reservasi tinggi/dimensi yang pasti sebelum data selesai dimuat!

---

## 3. Lima Pertanyaan Wajib Sebelum Menjalankan `install` Paket Baru

Setiap kali Anda tergoda memasang *library* pihak ketiga baru, jawab 5 pertanyaan ini di kepala Anda:
1. Bisakah ini ditulis dengan bersih, aman, dan teruji dalam **<= 40 baris kode internal** menggunakan API bawaan browser? *(Jika YA → tulis fungsi internal, jangan instal paket!)*
2. Jika menyangkut aksesibilitas rumit (misal *Combobox* keyboard atau *Date Picker* kalender), apakah paket ini *headless* & ramping (< 10–15 KB) tanpa membawa seluruh framework CSS saingan?
3. Berapa banyak sub-dependensi (*transitive dependencies*) yang ikut tertarik masuk ke `node_modules`?
4. Apakah paket ini mendukung *tree-shaking* penuh (`"sideEffects": false` pada ESM)?
5. Jika pembuat paket ini berhenti merawatnya tahun depan, seberapa mudah tim memelihara atau menggantinya? *(Selalu bungkus library pihak ketiga di balik 1 komponen adaptor internal milik proyek sendiri agar mudah diganti di satu tempat!).*

