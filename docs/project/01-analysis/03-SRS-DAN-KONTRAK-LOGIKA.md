---
dokumen: Spesifikasi Kebutuhan Perangkat Lunak (SRS) & Kontrak Logika
divisi_pembuat: D-01 (Principal System, Domain & Bureaucracy Analyst)
gerbang_terkait: Gate 1
status: DRAF
versi: 1.0.0
terakhir_diperbarui: -
---

# 03 — SRS, Kontrak Logika, Edge-Case & Kemudahan Maintenance

## 1. Katalog Kebutuhan Fungsional & Aturan Validasi Deterministik
> Setiap kebutuhan memiliki ID unik (`FR-XXX`) agar dapat dilacak hingga ke kontrak API, komponen UI, dan skenario pengujian QA.

| Kode FR | Modul / Fitur | Prioritas | Aturan Logika & Rumus Bisnis Eksplisit | Kriteria Penerimaan (*Acceptance Criteria*) |
| :--- | :--- | :--- | :--- | :--- |
| `FR-001` | `[Nama Fitur]` | `WAJIB_MVP` | `[Aturan pasti, batas karakter/angka, syarat unik]` | `[Kondisi terukur kapan dinyatakan benar]` |

## 2. Matriks Penanganan Edge-Case & Kegagalan Dunia Nyata
| ID | Kategori Risiko | Skenario Kejadian Ekstrem | Perilaku Wajib Sistem (Solusi Deterministik) |
| :--- | :--- | :--- | :--- |
| `EC-01` | Klik Ganda / Konkurensi | Pengguna klik tombol proses 2x atau 2 pejabat memproses berkas bersamaan | `[Penanganan idempotency / optimistic lock]` |
| `EC-02` | Uang / Kuota / Angka | Perebutan sisa kuota/anggaran terakhir atau pembulatan nilai | `[Transaksi atomik + tipe data bulat/desimal presisi]` |
| `EC-03` | Waktu & Batas Periode | Transaksi melewati jam tutup buku atau beda zona waktu | `[Validasi jam server UTC + aturan zona waktu resmi]` |
| `EC-04` | Integrasi / Jaringan | Layanan eksternal lambat/mati atau unggah file gagal di tengah jalan | `[Antrean ulang aman + umpan balik status jujur]` |
| `EC-05` | Siklus Hidup Master Data | Pegawai mutasi/nonaktif atau unit kerja berubah nama | `[Snapshot historis pada transaksi + larangan hard-delete]` |

## 3. Klasifikasi Keamanan Data & Kepatuhan Regulasi (UU PDP / SPBE / Standar)
| Entitas & Kolom Data | Tingkat Kerahasiaan | Aturan Tampilan UI (Utuh / Masking) | Aturan Penyimpanan & Log |
| :--- | :--- | :--- | :--- |
| `[Contoh: NIK / No Rekening]` | `PII_SENSITIF` | `Disamarkan di tabel daftar, tampil utuh hanya bagi peran berwenang` | `Enkripsi kolom; haram masuk ke log aplikasi` |

## 4. Target Non-Fungsional Terukur (Beban, Kecepatan & Reliabilitas)
- **Estimasi Volume Data 1–3 Tahun**: `[Jumlah baris per tabel utama & ukuran lampiran]`
- **Puncak Beban Bersamaan (*Peak Traffic*)**: `[Jumlah request/pengguna serentak saat jam sibuk]`
- **Batas Waktu Respons Maksimal**: `[Target baca daftar, pencarian, simpan transaksi, dan cetak laporan]`

## 5. Titik Kebijakan Terkonfigurasi (*Maintainability & Zero-Hardcode Map*)
> Daftar parameter dan aturan di bawah ini **DILARANG ditanam mati di dalam kode sumber** oleh Divisi Backend/Frontend agar perubahan kebijakan masa depan tidak memerlukan bongkar pasang kode.

| Kode Parameter | Nama Kebijakan yang Dapat Berubah | Nilai Awal Default | Siapa yang Mengubah & Bagaimana |
| :--- | :--- | :--- | :--- |
| `CFG-01` | `[Contoh: Batas nominal persetujuan langsung Kepala Bidang]` | `[Rp 25.000.000]` | `[Admin Sistem melalui tabel konfigurasi bertanggal efektif]` |

