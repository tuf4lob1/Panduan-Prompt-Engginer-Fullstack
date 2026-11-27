# Matriks Pemilihan Tech Stack Ringan & Hukum Anti-Overengineering

Panduan ini membantu Divisi Arsitek memilih tumpukan teknologi paling tepat guna dan paling hemat sumber daya server/browser berdasarkan fakta rekayasa, bukan sekadar tren media sosial.

---

## 1. Spektrum Paradigma Arsitektur Web & Aplikasi

Sebelum memilih framework, pilih **paradigma pengiriman antarmuka** yang paling ringan untuk kasus projek:

| Paradigma | Cara Kerja | Karakter Beban Browser & Server | Sangat Tepat Untuk |
| :--- | :--- | :--- | :--- |
| **Server-Driven Modern / Hypermedia atau Islands** *(misal: Astro, Laravel + Livewire/Blade, Go/Python + HTMX, Rails Hotwire)* | HTML dirender cepat di server; JavaScript hanya dikirim ke komponen yang benar-benar interaktif | **JS Browser Super Kecil (< 30 KB)**, muat instan di HP murah & sinyal lemah, SEO sempurna | Portal layanan publik pemerintah, sistem administrasi formulir/tabel, portal berita/katalog, MVP super hemat |
| **Fullstack Hybrid SSR + SPA Terpadu** *(misal: Next.js App Router, SvelteKit, Nuxt, Remix, Inertia.js)* | Muat awal dari server lalu navigasi antar-halaman mulus tanpa muat ulang penuh | **Seimbang**, kaya interaksi (*split-pane*, *optimistic UI*) namun wajib disiplin membatasi komponen klien! | SaaS B2B modern, meja kerja disposisi birokrasi interaktif, ERP multi-modul, produk startup |
| **SPA Terpisah + Dedicated High-Throughput API** *(misal: Vite React/Vue/Svelte + Backend Go/Rust/.NET/Fastify)* | Aset statis disajikan langsung dari CDN/Nginx super tipis; server API murni memproses JSON biner cepat | **RAM/CPU Server API Sangat Rendah**, mudah diakses bersama oleh Web & aplikasi Mobile (Flutter/Native) | Sistem berskala besar dengan aplikasi Web + Mobile sekaligus, integrasi lintas instansi (API Gateway/SPBE) |

---

## 2. Profil Karakteristik Bahasa & Runtime Backend (Referensi Objektif)

| Ekosistem Backend | Jejak RAM Idle Umum | Keunggulan Utama | Catatan Kewaspadaan Arsitek |
| :--- | :--- | :--- | :--- |
| **Go (Golang)** *(Stdlib `net/http`, Chi, Echo, Fiber + `sqlc`/`pgx`)* | **Sangat Ringan (~15–40 MB)**, 1 file biner mandiri | Konkurensi ribuan koneksi dengan CPU sangat irit, *deploy* sangat mudah tanpa dependensi runtime, kompilasi ketat | Kode bisnis kompleks butuh disiplin struktur domain agar tidak berulang-ulang manual |
| **TypeScript / Node.js atau Bun** *(Hono, Fastify, NestJS modular)* | **Sedang (~60–150 MB)** | Berbagi tipe data & skema validasi 100% antara Frontend dan Backend (mencegah selisih kontrak!), ekosistem sangat luas | Hindari *framework* berlapis refleksi berat bila target RAM ketat; wajib hati-hati presisi angka uang (`BigInt`/`decimal.js`) |
| **PHP Modern** *(Laravel 11/12 + FrankenPHP / Octane, Symfony)* | **Sedang (~80–180 MB mode worker; lebih rendah mode FPM)** | Produktivitas fitur bisnis/CRUD/birokrasi sangat cepat, antrean/auth/jadwal bawaan matang, sangat familier bagi tim IT daerah/instansi | Wajib mengaktifkan mode ketat tipe data (`declare(strict_types=1)`) & penjaga anti *N+1* (`Model::preventLazyLoading()`) |
| **Python** *(FastAPI, Litestar, Django)* | **Sedang (~80–200 MB)** | Tak tertandingi bila sistem memadukan analitik data, pemrosesan dokumen cerdas, AI/ML, atau otomasi ilmiah | Pastikan jalur I/O database berjalan benar-benar `async` non-blocking dan gunakan pemeriksa tipe statis (`mypy`/`pyright`) |
| **Rust / .NET Core / Java GraalVM-Quarkus** | **Sangat Efisien hingga Sedang** | Keamanan tipe ekstrem, performa puncak transaksi keuangan/perbankan tinggi | Waktu kompilasi & kurva belajar lebih curam bagi tim kecil |

---

## 3. Pemilihan Penyimpanan Data, Cache & Antrean Hemat Server

1. **PostgreSQL sebagai Pisau Lipat Utama (Rekomendasi Default Skala S1–S3)**:
   Satu instansi PostgreSQL yang dikonfigurasi benar sanggup menggantikan 4 komponen sekaligus pada skala kecil-menengah:
   - Penyimpanan relasional transaksional ACID ketat
   - Dokumen semi-terstruktur terindeks (`JSONB` + GIN Index untuk metadata dinamis formulir!)
   - Pencarian teks cepat (`tsvector` + `pg_trgm` untuk cari nama/perihal tanpa harus langsung memasang Elasticsearch 2 GB RAM!)
   - Antrean kerja tahan banting (`FOR UPDATE SKIP LOCKED`) tanpa harus memelihara broker terpisah di awal projek.
2. **SQLite (Mode WAL + ` synchronous = NORMAL`)**:
   Sangat layak untuk aplikasi internal satu server (*single-node S1*), perangkat tepi (*edge*), atau alat internal yang menuntut nol biaya perawatan database dan kecepatan baca mikrodetik.
3. **Kapan Menambah Redis / Valkey atau Message Broker Terpisah?**:
   Pasang **HANYA JIKA** terdapat kebutuhan *rate-limiting* terdistribusi lintas banyak server aplikasi, pembagian sesi *real-time* WebSocket multi-node, atau laju antrean melampaui ribuan tugas per detik.

---

## 4. Daftar Cekal Anti-Overengineering (Dilarang di Gate 2 Tanpa Bukti Angka)

Arsitek M-AEOS **WAJIB MENOLAK** komponen berikut pada desain awal kecuali `SCALE_PROFILE.md` membuktikan beban ekstrem:
- **Microservices > 1 layanan untuk tim < 8 engineer**: Biaya sinkronisasi data lintas database akan menghancurkan kecepatan proyek dan menyulitkan *maintenance*.
- **Kubernetes untuk beban yang cukup dilayani 1–2 container Docker / Systemd**: Memakan ratusan MB RAM hanya untuk agen pengatur klaster.
- **GraphQL untuk aplikasi internal yang tidak punya puluhan klien berbeda**: Rentan terhadap serangan kedalaman kueri (*query depth DoS*) dan masalah *N+1* tersembunyi bila tanpa *DataLoader* rumit; REST/RPC bertipe ketat jauh lebih ringan dan mudah di-cache.
- **ORM Berlapis Abstraksi Gelap Tanpa Kendali SQL**: Pilih *query builder* tipis bertipe kuat atau ORM yang transparan terhadap kueri SQL asli yang dihasilkan.

