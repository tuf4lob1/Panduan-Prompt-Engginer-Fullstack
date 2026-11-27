---
name: adversarial-appsec-redteam
description: >-
  Playbook audit keamanan adversarial & simulasi pembobolan aplikasi (Gate 4) untuk Divisi 06
  (Principal Red-Team). Mencakup pemodelan ancaman STRIDE, pembobolan RBAC/ABAC birokrasi,
  IDOR lintas unit/tenant, State-Skip Attack, Race Condition finansial, Mass Assignment,
  injeksi, keamanan lampiran privat, dan audit kebocoran PII sesuai UU PDP & OWASP ASVS.
---

# Metodologi Sidang Keamanan Adversarial & Pembobolan Sistem (Gate 4)

Ikuti 6 tahapan perburuan celah keamanan di bawah ini secara menyeluruh dari pintu masuk jaringan hingga ke baris kueri database dan kode klien.

---

## Tahap 1: Pemodelan Ancaman Spesifik Domain (*Targeted Threat Modeling*)

Berdasarkan `SCALE_PROFILE.md` dan `01-analysis/`, identifikasi **Aset Paling Berharga (Crown Jewels)** di proyek ini:
- Apakah dana/anggaran/saldo dompet?
- Apakah keabsahan surat keputusan/izin resmi bernomor hukum?
- Apakah data pribadi sensitif warga/pasien/nasabah (`PII_SENSITIF`)?
- Apakah kerahasiaan penawaran tender antar-peserta?

Wajib baca daftar serangan spesifik di [vektor-serangan-birokrasi-dan-owasp.md](./references/vektor-serangan-birokrasi-dan-owasp.md).

---

## Tahap 2: Audit Pembobolan Otorisasi & Alur Birokrasi (Prioritas #1!)

Telusuri setiap endpoint mutasi dan pembacaan detail di kode sumber Backend:
1. **Uji IDOR Horizontal & Lintas Unit Kerja**:
   - Jika pengguna dari *Unit Kerja A* mengganti parameter `:id` dengan ID milik *Unit Kerja B* pada endpoint `GET detail`, `PATCH edit`, `DELETE`, atau `GET download-lampiran`, apakah kueri database menolaknya?
2. **Uji Lompatan Mesin Status (*State-Skip Attack*)**:
   - Bisakah endpoint pengesahan akhir dipanggil terhadap dokumen yang masih berstatus `DRAF` atau `DITOLAK`?
   - Setelah dokumen berstatus `MENUNGGU_VERIFIKASI` atau `TERBIT` (*Locked State*), bisakah pembuat awal masih memanggil endpoint `PATCH /update` untuk mengubah angka nominal secara diam-diam?!
3. **Uji Pemisahan Tugas & Mandat Jabatan (*SoD & Plt/Plh Bypass*)**:
   - Apakah kode secara tegas memblokir `actor_user_id == maker_user_id` pada tahap verifikasi/persetujuan?
   - Apakah masa berlaku `valid_from <= NOW() <= valid_until` dan `is_active = true` pada mandat `Plt/Plh` selalu diperiksa di setiap transaksi, atau hanya dicek sekali saat login pagi hari?
   - Bisakah pengguna memalsukan header `X-Acting-Mandate-Id` milik pejabat lain?

---

## Tahap 3: Audit Manipulasi Payload, Balapan Saldo & Injeksi

1. **Mass Assignment / Over-Posting**: Periksa apakah body JSON dari klien langsung dilempar ke fungsi simpan ORM (`Model.create(req.body)` / `update(req.body)`) sehingga penyerang bisa menyuntikkan kolom `status`, `role`, `unit_id`, `approved_by`, atau `balance`!
2. **Serangan Konkurensi (*Race Condition / TOCTOU*)**: Periksa apakah ada pola *baca dulu di variabel aplikasi, lalu kurangi saldo di baris berikutnya* (`if (saldo >= req.nominal) { update(saldo - req.nominal) }`) tanpa penguncian baris atau syarat atomik `WHERE` di SQL!
3. **Injeksi Lintas Lapis**: Audit seluruh kueri mentah (SQL Injection termasuk pada parameter `ORDER BY` dinamis!), eksekusi perintah sistem (Command Injection saat konversi PDF/gambar), SSRF pada fitur ambil URL eksternal, dan XSS pada perenderan teks/nama berkas di Frontend.

---

## Tahap 4: Audit Keamanan Sesi, Rahasia, Berkas & Kebocoran PII

1. **Pencarian Rahasia Tertanam & Ketergantungan Rentan**: Gunakan `run_command` untuk memindai apakah ada kunci API, sandi default, JWT secret lemah di kode/git, serta jalankan audit kerentanan paket (`npm audit` / `govulncheck` / `pip-audit` / `composer audit` bila tersedia).
2. **Keamanan Unggah & Unduh Berkas**:
   - Apakah aplikasi memvalidasi isi asli file (*magic bytes*), membatasi ukuran maksimal untuk mencegah *Disk/Memory DoS*, dan menonaktifkan eksekusi skrip (misal bahaya unggah `.svg` berisi `<script>` XSS atau `.html`)?
   - Apakah dokumen lampiran rahasia bisa diakses tanpa login hanya dengan menebak path URL statis?
3. **Kepatuhan Privasi & Kebocoran Data (*Data Exposure*)**:
   - Apakah respons API mengirim lebih banyak kolom daripada yang ditampilkan di UI (misal membocorkan NIK utuh, email pribadi, atau hash sandi di JSON daftar)?
   - Apakah log server mencetak isi body permintaan yang mengandung sandi, token, atau data `PII_SENSITIF`?

---

## Tahap 5: Penyusunan Laporan Sidang Gate 4

Tuliskan seluruh temuan secara jujur dan terukur di `docs/project/04-quality-gates/GATE-4-SECURITY-REDTEAM.md` lengkap dengan:
- Tingkat bahaya (`KRITIS`, `TINGGI`, `SEDANG`, `RENDAH`).
- Lokasi persis di kode (`path/file:baris`).
- Bukti skenario pembobolan langkah demi langkah (*Proof of Concept*).
- Panduan perbaikan arsitektural yang tepat (bukan sekadar menyembunyikan tombol di UI!).

