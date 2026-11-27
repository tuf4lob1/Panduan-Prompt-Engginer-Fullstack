---
name: stateful-qa-chaos-verification
description: >-
  Playbook pengujian perangkat lunak menyeluruh (Gate 5) untuk Divisi 07 (Principal QA/SDET).
  Mencakup pengujian matriks transisi mesin status birokrasi (positif & negatif), pengujian batas
  ekstrem & chaos konkurensi, penelusuran keterlacakan kebutuhan SRS (Traceability), serta audit
  kesesuaian antarmuka 7-kondisi dan responsivitas layar.
---

# Metodologi Verifikasi QA Berlapis, Chaos Input & Audit 7-Kondisi

Pengujian AI biasa sering menipu karena hanya menguji *"buat data normal → berhasil"*. Skill ini mewajibkan pengujian yang meremukkan asumsi rapuh sebelum pengguna nyata mengalaminya.

---

## Tahap 1: Keterlacakan Kebutuhan 100% (*SRS Traceability Matrix*)

Buka `03-SRS-DAN-KONTRAK-LOGIKA.md`:
1. Pastikan setiap kode kebutuhan `FR-XXX` dan setiap skenario *edge-case* `EC-XX` memiliki pasangan kasus pengujian nyata.
2. Periksa apakah ada aturan bisnis di SRS yang lupa dikerjakan oleh Frontend atau Backend!

---

## Tahap 2: Pengujian Mesin Status & Konkurensi Otomatis

Wajib baca panduan skenario ekstrem di [matriks-uji-statemachine-chaos-dan-7state.md](./references/matriks-uji-statemachine-chaos-dan-7state.md) lalu tulis serta jalankan tes otomatis (`run_command`) yang membuktikan:
1. **Jalur Lurus & Jalur Revisi Berlapis**: Draf → Ajukan → Kembalikan Revisi → Perbaiki → Ajukan Ulang → Paraf → Sahkan → Terbit Nomor Resmi + Jejak Audit tercatat lengkap.
2. **Penolakan Transisi Ilegal**: Mencoba melompati tahap, mencoba mengedit dokumen yang sudah terkunci, dan mencoba menyetujui dengan peran yang salah.
3. **Ketahanan Klik Ganda & Balapan Paralel**: Mengirimkan aksi identik secara paralel dan memverifikasi tidak ada data kembar, nomor surat kembar, maupun saldo minus.

---

## Tahap 3: Pengujian Input Ekstrem (*Boundary & Hostile Data*)

Uji ketahanan validasi pada batas bawah, batas atas, dan tipe tak lazim:
- Teks kosong `""`, spasi murni `"    "`, teks sangat panjang (300+ karakter), karakter kutip tunggal/ganda `' "`, simbol mata uang/pemisah, dan karakter multi-bahasa.
- Angka `0`, negatif `-1`, desimal ganjil, dan nilai melampaui plafon maksimum kebijakan (`CFG-XX`).
- Tanggal mundur, tanggal mulai > tanggal selesai, dan batas pergantian hari UTC vs WIB.

---

## Tahap 4: Verifikasi Kesesuaian Desain UI/UX, 7-Kondisi & Aksesibilitas

Periksa implementasi Frontend terhadap kontrak `03-design/`:
1. **Audit 7 Kondisi Layar**: Pastikan komponen tidak meledak (`undefined is not an object`) saat daftar bernilai kosong `[]`, saat respons API lambat 2 detik, saat teks perihal 150 karakter, saat server mengembalikan error validasi `422` maupun error jaringan `500/offline`, dan saat berkas berstatus terkunci!
2. **Audit Anti-AI-Slop & Anti-Dinding-Teks**: Pastikan tidak ada teks instruksi bertele-tele, warna liar di luar token, angka tabel yang tidak memakai `tabular-nums`, atau tabel yang hancur di ukuran layar ponsel (`360px`) maupun laptop kantor (`1366px`).
3. *(Catatan Koordinasi Browser)*: Bila aplikasi web dapat dijalankan secara lokal dan memerlukan inspeksi visual langsung di peramban, laporkan URL lokal siap uji kepada Orchestrator agar Orchestrator dapat menugaskan agen `browser` khusus untuk memverifikasi interaksi visual nyata bila diperlukan.

---

## Tahap 5: Pelaporan Bukti Eksekusi Gate 5

Catat hasil eksekusi perintah tes (jumlah lulus/gagal, waktu eksekusi, daftar bug ditemukan) secara transparan di `docs/project/04-quality-gates/GATE-5-QA-VERIFICATION.md`.

