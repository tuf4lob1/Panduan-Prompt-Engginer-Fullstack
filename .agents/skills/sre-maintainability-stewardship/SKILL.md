---
name: sre-maintainability-stewardship
description: >-
  Playbook kelaikan operasi produksi, penghematan server, dan audit kemudahan pemeliharaan
  jangka panjang (Gate 6) untuk Divisi 08 (Principal SRE Steward). Mencakup audit entropi kode
  (anti-ribet maintenance), container/server tuning hemat RAM, health checks, graceful shutdown,
  structured audit observability, prosedur backup-restore, dan penulisan Deployment Runbook.
---

# Metodologi Kelaikan Produksi Ringan & Kemudahan Maintenance (Gate 6)

Skill ini memastikan sistem yang selesai dibangun benar-benar siap hidup di dunia nyata: hemat server, tidak panik saat mati lampu/restart, mudah dilacak ketika ada keluhan pengguna, dan sangat nyaman dipelihara bertahun-tahun.

---

## Tahap 1: Audit Entropi Kode & Kemudahan Pemeliharaan (*Zero-Maintenance-Nightmare*)

Wajib baca tolok ukur di [audit-entropi-kode-dan-operasi-ringan.md](./references/audit-entropi-kode-dan-operasi-ringan.md) dan jalankan pemeriksaan otomatis melalui `run_command`:
1. **Pindai File Raksasa & Kode Mati**: Cari file kode sumber aplikasi yang membengkak melebihi batas sehat (>350–400 baris), fungsi yang tidak pernah dipanggil (*unused exports/dead files*), atau berkas sementara/sampah yang tertinggal di repo.
2. **Audit Anti-Hardcode (`CFG-XX` Verification)**: Pastikan seluruh aturan kebijakan bisnis yang ditandai di `03-SRS-DAN-KONTRAK-LOGIKA.md` maupun URL/kredensial lingkungan benar-benar dikendalikan lewat tabel kebijakan atau variabel lingkungan (`.env.example` terdokumentasi 100% untuk setiap variabel!).
3. **Uji Kesiapan Orang Baru (*10-Minute Onboarding Test*)**: Jika seorang developer baru meng-clone repositori ini hari ini di laptop kosong, apakah ia bisa menyalakan database lokal, menjalankan migrasi, mengisi data contoh, dan menjalankan aplikasi hanya dengan **<= 3 perintah jelas** tanpa menebak-nebak?

---

## Tahap 2: Konfigurasi Infrastruktur Ringan & Hemat Biaya (*FinOps Tuning*)

Sesuaikan artefak *deployment* dengan target infrastruktur di `SCALE_PROFILE.md`:
1. **Jika Menggunakan Container (`Dockerfile` & `compose.yaml`)**:
   - Wajib memakai **Multi-Stage Build** sehingga citra akhir produksi (*production image*) hanya berisi biner/aset matang tanpa membawa kompilator atau `devDependencies` berat!
   - Jalankan proses sebagai **pengguna non-root (`USER nonroot`)** demi keamanan kontainer.
   - Tetapkan batas memori wajar dan kalibrasi parameter database/runtime agar tidak memakan seluruh RAM VPS kecil.
2. **Kesiapan Sinyal & Kesehatan Layanan**:
   - Pastikan tersedia endpoint pemeriksaan kesehatan ringan (`/healthz` atau `/api/health`) yang memverifikasi konektivitas penyimpanan utama dengan batas waktu singkat.
   - Pastikan server menangani `SIGTERM` / `SIGINT` secara anggun (*Graceful Shutdown*): berhenti menerima koneksi baru, menyelesaikan permintaan yang sedang berjalan dalam beberapa detik, menutup koneksi DB dengan rapi, baru keluar.

---

## Tahap 3: Observabilitas, Pencadangan (*Backup*) & Prosedur Darurat

1. **Keterlacakan Masalah Cepat**: Pastikan setiap permintaan memiliki `request_id / trace_id` yang dikembalikan di header respons error sekaligus tercatat di log JSON server—sehingga saat pengguna melapor *"Muncul kode referensi `req_01J9...`"*, tim IT dapat menemukan penyebab persisnya di log dalam **5 detik**!
2. **Strategi Migrasi Aman & Rollback**: Dokumentasikan bagaimana cara memperbarui versi aplikasi tanpa merusak transaksi berjalan, serta langkah pemulihan cepat jika rilis baru bermasalah.
3. **Prosedur Pencadangan & Uji Pulih (*Backup & Restore*)**: Cadangan yang belum pernah diuji pulih bukanlah cadangan! Sediakan skrip atau perintah pencadangan otomatis database + folder berkas lampiran terenkripsi beserta cara memulihkannya.

---

## Tahap 4: Penulisan Artefak Penutup Gate 6

Tuliskan hasil audit dan panduan operasi yang sangat rapi ke dalam:
1. `docs/project/08-operations/MAINTAINABILITY_AUDIT.md` — Hasil skor kebersihan struktur kode, daftar dependensi akhir, profil jejak resource server, dan peta arsitektur singkat untuk pemelihara masa depan ("Di mana harus mengubah X jika aturan Y berubah?").
2. `docs/project/08-operations/DEPLOYMENT_RUNBOOK.md` — Buku pegangan langkah demi langkah instalasi lokal, deploy produksi, rotasi kunci rahasia, backup/restore, dan penanganan insiden umum.

