# Arsitektur Backend Modular & Rahasia Kemudahan Maintenance Jangka Panjang

Dokumen ini menjawab keluhan klasik *"kenapa projek makin besar makin ribet dirawat dan tiap ubah satu fitur merusak tiga fitur lain"*.

---

## 1. Anatomi Direktori Modular Monolith Standar M-AEOS

Hindari struktur datar berdasarkan lapisan teknis semata jika projek mulai memiliki >3 domain, karena mengubah satu fitur mengharuskan membuka 8 folder berjauhan. Gunakan pemisahan berbasis modul bisnis yang tegas:

```text
backend/ (atau src/server/)
├── cmd/ atau main                  # Titik nyala server HTTP & Worker + Graceful Shutdown
├── internal/ (atau modules/)
│   ├── platform/                   # Infrastruktur bersama (DB pool, Logger JSON, Auth Middleware, Audit Writer, Config)
│   ├── identity/                   # Modul Akun, Unit Organisasi, Jabatan & Mandat Plt/Plh
│   │   ├── handler.*               # Pintu HTTP tipis
│   │   ├── service.*               # Use-case & transaksi
│   │   ├── domain.*                # Aturan murni mandat & hierarki
│   │   └── repository.*            # Kueri terindeks khusus tabel identity
│   ├── submission/                 # Modul Pengajuan & Mesin Status Birokrasi
│   │   ├── handler.*
│   │   ├── service.*
│   │   ├── statemachine.*          # Tabel aturan transisi status & Guard terpusat!
│   │   └── repository.*
│   └── policy/                     # Modul Parameter Kebijakan Dinamis (CFG-XX Zero-Hardcode)
└── migrations/                     # File migrasi skema & indeks berurutan
```

---

## 2. Enam Aturan Anti-Kerumitan Pemeliharaan (*Low-Entropy Code Rules*)

1. **Satu Sumber Kebenaran Mesin Status (`statemachine`)**:
   - *Dilarang Keras*: Menebar pengecekan `if (doc.status == 'MENUNGGU_PARAF' && user.role == 'KABID')` di 12 file berbeda!
   - *Wajib*: Seluruh aturan perpindahan status untuk satu entitas dikonsentrasikan di **satu file definisi Mesin Status**. Jika tahun depan instansi menambah satu tahap pemeriksaan baru, programmer cukup memperbarui satu definisi tabel transisi tersebut!
2. **Larangan Ketergantungan Melingkar (*Zero Circular Dependency*)**:
   Arah ketergantungan wajib satu arah. Jika Modul A dan Modul B saling membutuhkan informasi, tentukan siapa pemilik data hulu atau komunikasikan lewat antarmuka tipis / peristiwa domain (*Domain Event*) di lapis aplikasi.
3. **Batas Ukuran File & Fungsi**:
   - Satu file kode sumber idealnya **<= 300 baris** (batas keras peringatan **400 baris**).
   - Satu fungsi bisnis idealnya **<= 50 baris** dengan percabangan bersarang maksimal 3 tingkat (*Early Return Pattern*—kembalikan error lebih awal agar kode tidak menjorok ke kanan seperti tangga!).
4. **Katalog Kode Galat Bisnis Bernama Jelas**:
   Jangan melempar pesan string bebas seperti `throw new Error("gagal")`. Gunakan kode terdefinisi (`ERR_MANDATE_EXPIRED`, `ERR_SOD_SELF_APPROVAL`, `ERR_INSUFFICIENT_BUDGET`, `ERR_STALE_DOCUMENT_VERSION`) sehingga mudah dilacak di log produksi dan mudah diterjemahkan di UI.
5. **Nol Angka/String Sakti (*Zero Magic Values*)**:
   Semua nama status, kode peran, batas ukuran lampiran, dan kunci kebijakan wajib berupa konstanta bertipe kuat (*Enum / Typed Constant*). Kebijakan bisnis yang dapat berubah wajib dibaca dari layanan `policy` (dengan cache memori ringan), bukan ditanam mati di kode!
6. **Migrasi Database yang Selalu Aman Maju (*Expand-and-Contract*)**:
   Saat memperbarui aplikasi yang sudah berjalan, hindari migrasi yang langsung menghapus/mengubah nama kolom aktif seketika jika aplikasi masih melayaninya; tambahkan kolom/indeks secara aman (`CREATE INDEX CONCURRENTLY` pada Postgres produksi besar) dan jangan pernah mengedit file migrasi lama yang sudah pernah dijalankan!

