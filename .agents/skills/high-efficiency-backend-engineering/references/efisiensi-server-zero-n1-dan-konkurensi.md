# Panduan Efisiensi RAM/CPU Server, Hukum Zero N+1 & Konkurensi Atomik

Dokumen ini memastikan backend buatan M-AEOS sanggup melayani beban tinggi dengan pemakaian memori minimal dan nol korupsi data.

---

## 1. Empat Pembunuh Utama Server (dan Cara Mematikannya)

### Pembunuh #1: Kueri `N+1` Tersembunyi
- **Gejala**: Menampilkan 50 baris pengajuan memicu 1 kueri daftar pengajuan + 50 kueri ambil nama pemohon + 50 kueri ambil nama unit kerja + 50 kueri hitung jumlah lampiran = **151 bolak-balik database dalam 1 klik!**
- **Solusi Wajib**:
  - Jika memakai ORM, matikan *implicit lazy loading* secara global!
  - Ambil data relasi sekaligus dalam **1 `JOIN` ramping** atau **1 kueri `WHERE id IN (...)` terkelompok**, dan hitung agregat ringkas melalui subkueri terindeks atau kolom penghitung terjaga.

### Pembunuh #2: Menyaring atau Mengurutkan Data di Memori Aplikasi (*In-Memory Table Dump*)
- **Gejala**: Menulis `allRows = db.findAll(); filtered = allRows.filter(...)` yang menarik 50.000 baris ke RAM aplikasi lalu membuang 49.980 baris! Satu permintaan semacam ini bisa memakan 200 MB RAM dan memicu *Garbage Collection Pause* yang membekukan seluruh pengguna lain.
- **Solusi Wajib**: Seluruh penyaringan (`WHERE`), pengurutan (`ORDER BY`), pengelompokan (`GROUP BY`), penjumlahan (`SUM/COUNT`), dan pembatasan baris (`LIMIT`) **WAJIB dikerjakan di dalam mesin database** menggunakan indeks komposit!

### Pembunuh #3: Ukuran *Database Connection Pool* Salah Kaprah
- **Kesalahan Umum**: Mengatur `max_connections = 500` pada server kecil 2 vCPU, sehingga database kehabisan RAM dan waktu CPU habis hanya untuk berpindah konteks (*context switching*).
- **Rumus Sehat M-AEOS**: Untuk beban transaksi OLTP yang kuerinya sudah terindeks rapi (< 5ms per kueri), ukuran *connection pool* per proses aplikasi cukup dikalibrasi di kisaran **`(Jumlah Core CPU Database * 2) + 2` s/d `20–30 koneksi maks`** dengan *connection timeout* tegas, sehingga antrean dikelola tertib tanpa menumbangkan database.

### Pembunuh #4: Pekerjaan Berat Memblokir Jalur Utama HTTP
- **Aturan Wajib**: Pembuatan berkas PDF/Excel besar, kompresi gambar, penandatanganan kriptografi eksternal (TTE), dan pengiriman webhook/email keluar **DILARANG** menahan koneksi transaksi database tetap terbuka! Tutup transaksi DB secepat kilat (< 20ms), lalu serahkan tugas berat ke pekerja latar belakang (*Worker*) dengan batas konkurensi terkendali (misal maksimal 2–4 pembuatan PDF serentak agar CPU & RAM tidak melonjak tajam!).

---

## 2. Pola Emas Transaksi Birokrasi & Penomoran Resmi Bebas Bentrok

### A. Pola Eksekusi Aksi Birokrasi Anti-Celah (Urutan 6 Langkah Atomik)
Setiap kali pejabat menekan tombol `Paraf`, `Setujui`, `Kembalikan Revisi`, atau `Batalkan`:
```text
1. Ekstrak user_id dari sesi server & verifikasi mandat jabatan aktif pada detik NOW()
2. Mulai Transaksi Database (BEGIN)
3. Ambil baris dokumen + kunci versi/baris; pastikan cakupan unit kerja cocok & user_id != maker_user_id (bila aturan SoD berlaku)
4. Evaluasi Mesin Status & Syarat Penjaga (Guards) terhadap status dokumen saat ini
5. Eksekusi UPDATE dokumen (naikkan version + 1) + efek samping atomik (misal potong pagu / terbitkan nomor resmi)
6. Eksekusi INSERT ke tabel immutable audit_logs (beserta snapshot sebelum & sesudah + alasan + nomor SK mandat)
7. Selesaikan Transaksi (COMMIT) -> Baru jadwalkan notifikasi asinkron ke antrean keluar!
```

### B. Penomoran Dokumen Resmi Tanpa Ganda & Tanpa Bolong
Untuk menerbitkan nomor urut resmi (misal `042/SK-KEU/XI/2026`) tepat saat status menjadi `TERBIT`:
- Gunakan tabel penghitung khusus per jenis dokumen & periode (`document_sequences`: `doc_type, period_key, last_number`).
- Di dalam transaksi pengesahan yang sama, jalankan operasi atomik:
  `INSERT INTO document_sequences (doc_type, period_key, last_number) VALUES ($1, $2, 1) ON CONFLICT (doc_type, period_key) DO UPDATE SET last_number = document_sequences.last_number + 1 RETURNING last_number;`
- Jika langkah pengesahan gagal karena syarat lain dan transaksi *rollback*, nomor urut otomatis ikut batal naik sehingga **tidak ada nomor bolong dan mustahil ada dua surat bernomor kembar**!

