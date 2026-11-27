---
name: maeos-intake-triage
description: >-
  Gunakan skill ini pada awal projek baru atau saat menginisialisasi Gate 0 di M-AEOS.
  Memandu wawancara tajam penggalian kebutuhan awal, menentukan profil skala projek
  (S1-Startup, S2-Enterprise, S3-Gov-Birokrasi), menetapkan anggaran beban server/browser,
  dan mengisi SCALE_PROFILE.md serta PROJECT_STATE.md sebelum mendelegasikan ke Divisi Analisis.
---

# Protokol Intake & Triage Skala Projek (Gate 0 M-AEOS)

Skill ini dijalankan oleh **Chief Engineering Orchestrator** saat pengguna pertama kali menyampaikan ide projek baru, dokumen TOR/KAK (*Kerangka Acuan Kerja*), atau permintaan pembuatan sistem.

Tujuan Anda adalah mencegah kesalahan arah sejak menit pertama tanpa membuat pengguna lelah dengan puluhan pertanyaan remeh.

---

## Langkah 1: Periksa Status Eksisting

1. Baca `docs/project/00-governance/PROJECT_STATE.md` dan `docs/project/00-governance/SCALE_PROFILE.md`.
2. Jika Gate 0 sudah berstatus `DISETUJUI` dan pengguna tidak meminta perubahan arah projek, hentikan skill ini dan lanjutkan ke fase aktif sesuai `PROJECT_STATE.md`.
3. Jika pengguna memberikan dokumen awal (misal KAK, PRD kasar, catatan rapat, atau skema lama), baca seluruh file tersebut terlebih dahulu agar Anda **tidak menanyakan hal yang sudah tertulis**.

---

## Langkah 2: Diagnosis Cepat 5 Dimensi Projek

Dari penjelasan awal pengguna, petakan mana yang sudah jelas dan mana yang masih gelap pada 5 dimensi penentu arsitektur berikut:

1. **Misi Inti & Masalah Nyata**: Masalah operasional/bisnis apa yang paling menyakitkan saat ini dan apa ukuran sukses utamanya?
2. **Profil Pengguna & Konteks Pemakaian**: Siapa pemakai utamanya (masyarakat awam lintas usia, staf admin harian 8 jam di desktop, pejabat eksekutif di HP, atau petugas lapangan sinyal lemah)?
3. **Kompleksitas Alur & Birokrasi**: Apakah alurnya lurus sederhana, atau memiliki persetujuan berjenjang, disposisi lintas bagian, pelimpahan wewenang (*Plt/Plh*), revisi dokumen, dan audit ketat?
4. **Sensitivitas Data & Regulasi**: Apakah menyimpan data pribadi sensitif (NIK/kesehatan/keuangan — terkait UU PDP), transaksi uang/anggaran negara, atau dokumen resmi bernomor hukum?
5. **Realitas Infrastruktur & Pemeliharaan**: Di mana sistem ini akan dijalankan (VPS kecil hemat biaya, server on-premise instansi, atau cloud terkelola) dan siapa yang akan merawatnya sehari-hari (developer tunggal atau tim khusus)?

---

## Langkah 3: Wawancara Terfokus (Maksimal 4–5 Pertanyaan Kunci)

Jika masih ada dimensi kritis yang belum terjawab, ajukan pertanyaan terstruktur (gunakan *tool* `ask_question` untuk pilihan strategis yang jelas, atau pertanyaan poin ringkas).

**Aturan Wawancara Tajam**:
- Dilarang menanyakan detail teknis rendah (seperti *"mau pakai library CSS apa?"*) kepada pengguna jika mereka belum menentukan preferensi stack; itu tugas Divisi Arsitek & Desain nanti.
- Fokuskan pertanyaan pada **skala pengguna, tingkat birokrasi/persetujuan, target infrastruktur server, dan preferensi karakter produk**.
- Jika pengguna sudah menyebutkan preferensi bahasa/framework tertentu yang wajib dipakai (misal karena aturan kantor/tim), catat sebagai **Batasan Keras (*Hard Constraint*)**.

---

## Langkah 4: Penetapan Profil Skala & Anggaran Performa

Berdasarkan jawaban pengguna, tetapkan salah satu profil berikut di `docs/project/00-governance/SCALE_PROFILE.md`:

| Parameter Kalibrasi | `S1-Startup` (Cepat & Gesit) | `S2-Enterprise` (Skalabel & Multi-Unit) | `S3-Gov-Birokrasi` (Regulasi & Alur Berlapis) |
| :--- | :--- | :--- | :--- |
| **Fokus Utama** | Kecepatan rilis, kejelasan nilai produk, hemat biaya server | Pemisahan tenant/cabang, reliabilitas tinggi, integrasi sistem | Kepatuhan aturan/SK, alur berjenjang presisi, jejak audit abadi |
| **Target Infrastruktur Dasar** | Ringan di 1–2 vCPU / 1–2 GB RAM | Modular siap skala horizontal, cache & antrean terpisah | Tahan jaringan lambat/on-premise maupun cloud pemerintah |
| **Target Beban Awal Frontend** | JS awal sangat ramping (< 120 KB gzip), muat instan | Modul terpisah (*code-splitting* ketat per peran/fitur) | Sangat ringan di perangkat spesifikasi rendah & koneksi 3G/4G tidak stabil |
| **Target Respons API (P95)** | < 150 ms untuk baca, < 300 ms untuk tulis standar | < 150 ms baca, tugas berat wajib via antrean latar belakang | < 200 ms baca, generasi dokumen/PDF resmi via antrean asinkron |
| **Kedalaman Hak Akses** | RBAC bersih (2–4 peran jelas) | RBAC + pembatasan unit/organisasi/tenant | RBAC + ABAC (Jabatan, Unit Kerja, Eselon, Plt/Plh, Status Dokumen) |
| **Standar Jejak Audit** | Log aktivitas bisnis krusial | Audit perubahan data penting & akses sensitif | *Immutable Audit Log* 5W+1H lengkap nilai sebelum & sesudah |

---

## Langkah 5: Penguncian Gate 0 & Serah Terima ke Divisi Analisis

1. Perbarui `docs/project/00-governance/SCALE_PROFILE.md` dengan seluruh parameter projek yang telah disepakati.
2. Perbarui `docs/project/00-governance/PROJECT_STATE.md`:
   - Ubah status **Gate 0** menjadi `DISETUJUI`.
   - Ubah fase aktif menjadi `FASE 1: ANALISIS SISTEM & BIROKRASI MENDALAM`.
3. Buat ringkasan Berita Acara Gate 0 di `docs/project/04-quality-gates/GATE-0-TRIAGE.md`.
4. Segera panggil subagent `principal-analyst` dengan memberikan ringkasan konteks dari `SCALE_PROFILE.md` untuk memulai riset sistem A–Z.

