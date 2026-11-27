---
name: deep-domain-bureaucracy-analysis
description: >-
  Playbook riset sistem mendalam A-Z untuk Divisi 01 (Principal Analyst). Gunakan saat
  membedah kebutuhan bisnis dari nol, memetakan alur birokrasi kompleks (pemerintahan/SPBE,
  enterprise, keuangan, startup), menyusun matriks wewenang jabatan & Plt/Plh, merancang
  state-machine dokumen bebas celah, mengidentifikasi edge-case ekstrem, serta menyusun SRS.
---

# Metodologi Riset Sistem Mendalam & Rekayasa Alur Birokrasi (A–Z)

Skill ini memastikan tidak ada satu pun fitur yang dibangun di atas asumsi dangkal. Ikuti urutan 6 tahap riset dan spesifikasi di bawah ini secara disiplin.

---

## Tahap 1: Riset Domain Industri & Regulasi (`search_web` + Konteks)

Jangan mengandalkan ingatan umum semata bila menyentuh domain spesifik. Gunakan `search_web` untuk memverifikasi standar nyata di lapangan:
- **Istilah Baku Domain (*Ubiquitous Language*)**: Pastikan penamaan entitas sesuai praktik industri/instansi terkait (misal: *DIPA/RKA, SPM/SP2D, Disposisi, Berita Acara, Faktur Pajak, Rekam Medis Elektronik, Polis, Ledger*).
- **Kepatuhan Regulasi & Standar**:
  - Jika mengelola data pribadi warga/pelanggan Indonesia → petakan kewajiban **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)**: persetujuan eksplisit, tujuan pemrosesan, retensi data, hak koreksi/hapus, dan perlindungan kolom sensitif.
  - Jika sistem pemerintahan/BUMN → petakan prinsip **SPBE / Satu Data**: kode referensi baku, interoperabilitas API, tanda tangan elektronik tersertifikasi (TTE), dan kearsipan dinamis.
  - Jika menyentuh uang, stok barang, atau kuota terbatas → terapkan prinsip **Buku Besar Tak Terhapus (*Append-Only Ledger*)**: saldo/stok tidak boleh diedit bebas dengan `UPDATE angka`, melainkan harus lahir dari mutasi/jurnal yang tercatat.

---

## Tahap 2: Dekomposisi Organisasi, Aktor & Matriks Wewenang

Baca referensi lengkap di [panduan-birokrasi-dan-statemachine.md](./references/panduan-birokrasi-dan-statemachine.md) apabila projek memiliki lebih dari 2 peran atau berskala `S2-Enterprise` / `S3-Gov-Birokrasi`.

1. **Pisahkan Identitas Orang (*User*) dari Jabatan/Peran (*Position/Role Assignment*)**:
   Di organisasi nyata, Budi hari ini adalah *Analis Anggaran Bidang A*, bulan depan dimutasi ke *Bidang B*, dan selama seminggu ditunjuk menjadi *Plh. Kepala Bidang A*. Hak akses dan riwayat persetujuan harus melekat pada konteks jabatan & unit kerja pada detik tindakan dilakukan!
2. **Batas Cakupan Data (*Data Visibility Scope*)**:
   Untuk setiap peran, tentukan dengan tegas apakah ia melihat:
   - Hanya miliknya sendiri (`OWN`)
   - Seluruh data satu tim/seksi/cabang (`UNIT`)
   - Seluruh data unit di bawah hierarkinya (`SUBTREE`)
   - Lintas unit yang didisposisikan kepadanya (`ASSIGNED`)
   - Seluruh organisasi (`GLOBAL`)
3. **Pemisahan Tugas (*Segregation of Duties / SoD*)**:
   Tentukan aksi krusial di mana pembuat usulan (*Maker*) **haram** menjadi penyetuju usulannya sendiri (*Approver*), meskipun orang tersebut kebetulan merangkap jabatan.

---

## Tahap 3: Rekayasa Mesin Status Deterministik (*State-Machine Engineering*)

Setiap entitas berumur panjang (Pengajuan, Surat, Pesanan, Klaim, Tiket, Kontrak, Pencairan) wajib dimodelkan sebagai **Mesin Status Formal**, bukan sekadar daftar status lepas:

Untuk setiap entitas berstatus, definisikan tabel lengkap yang memuat:
1. **Daftar Status Sah (*Valid States*)** beserta apakah data masih boleh diedit atau sudah **Terkunci (*Immutable*)**.
2. **Pemicu Transisi (*Action/Event*)**: Siapa aktor yang berhak memicu?
3. **Syarat Penjaga (*Transition Guards*)**: Validasi bisnis apa yang wajib terpenuhi sebelum status boleh berpindah? (Contoh: *"Status tidak bisa pindah ke `DISETUJUI_KEPALA` jika berkas lampiran wajib belum lengkap atau pagu anggaran unit tidak mencukupi"*).
4. **Efek Samping Atomik (*Side Effects*)**: Apa yang terjadi bersamaan? (Penomoran otomatis bebas bentrok, pemotongan kuota/pagu sementara, notifikasi ke jabatan berikutnya, pencatatan log audit).
5. **Jalur Mundur & Pengecualian**:
   - *Revisi / Dikembalikan*: Ketika ditolak pemeriksa di level ke-3, apakah dokumen kembali ke pembuat awal atau turun 1 tingkat ke level ke-2? Apakah setelah diperbaiki harus mengulang verifikasi dari level ke-1?
   - *Pembatalan / Pencabutan (*Void / Revoke*)*: Jika dokumen yang sudah terbit/disahkan ternyata salah, dilarang dihapus (`DELETE`)! Rancang mekanisme **Berita Acara Pembatalan / Dokumen Adendum / Jurnal Pembalik**.

---

## Tahap 4: Pemburuan Edge-Case & Kegagalan Dunia Nyata

Baca daftar uji tuntas di [katalog-edgecase-dan-nfr.md](./references/katalog-edgecase-dan-nfr.md) dan uji spesifikasi Anda terhadap seluruh skenario kritis:
- Klik ganda / pengiriman paralel (*Idempotency & Concurrency Conflict*).
- Perebutan sumber daya terbatas pada detik yang sama (kuota pendaftaran, stok barang terakhir, nomor surat urut resmi, sisa anggaran).
- Batas waktu (*Cut-off*, hari libur vs hari kerja untuk perhitungan SLA, perbedaan zona waktu WIB/WITA/WIT).
- Kegagalan layanan eksternal (gateway pembayaran, TTE, WhatsApp/Email, API kementerian lain sedang *down*).
- Data yatim & jebakan penghapusan (*referential integrity* saat pegawai pensiun, cabang ditutup, atau kategori lama dinonaktifkan).

---

## Tahap 5: Rekayasa Kemudahan Maintenance Sejak Level Analisis

Agar sistem tidak menjadi mimpi buruk pemeliharaan 1–3 tahun ke depan, wajib buat bagian khusus **"Titik Variabilitas & Kebijakan Terkonfigurasi"**:
- Daftar aturan angka/batas yang berpotensi berubah (persentase biaya, batas nominal persetujuan per level jabatan, durasi SLA, kuota unggah).
- Daftar alur persetujuan atau template dokumen cetak yang mungkin berubah tiap tahun anggaran atau reorganisasi struktur dinas/divisi.
- Klasifikasi fitur berdasarkan prioritas (`MVP Inti Fase 1` vs `Pengembangan Fase Lanjutan`) agar ruang lingkup terkendali tajam dan tidak membengkak liar (*Scope Creep*).

---

## Tahap 6: Penulisan 3 Artefak Standar Gate 1

Tuliskan hasil riset dan analisis secara lengkap, bersih, dan saling konsisten ke dalam 3 file berikut di `docs/project/01-analysis/`:
1. `01-DOMAIN-DAN-AKTOR.md` — Kamus domain, peta struktur unit organisasi, matriks peran/jabatan, cakupan visibilitas data, dan pendelegasian wewenang.
2. `02-ALUR-KERJA-DAN-BIROKRASI.md` — Diagram Mermaid & tabel *state-machine* lengkap seluruh alur bisnis utama, aturan disposisi/eskalasi SLA, mekanisme revisi/pembatalan, serta standar jejak audit.
3. `03-SRS-DAN-KONTRAK-LOGIKA.md` — Spesifikasi kebutuhan fungsional bernomor unik (`FR-001`, dst.), aturan validasi bisnis deterministik, matriks penanganan *edge-case*, klasifikasi keamanan data, target NFR, dan daftar kebijakan terkonfigurasi.

### Daftar Periksa Mandiri Sebelum Menyerahkan ke Orchestrator:
- [ ] Apakah masih ada kata kabur (*"dll"*, *"secukupnya"*, *"otomatis menyesuaikan"* tanpa rumus)? Jika ada, hapus dan ganti dengan rumus/aturan eksplisit!
- [ ] Apakah setiap proses persetujuan sudah memiliki jalur **Revisi**, **Penolakan**, dan **Pembatalan Pasca-Setuju**?
- [ ] Apakah skenario pejabat mutasi / *Plt* / *Plh* sudah tertangani (untuk profil `S2`/`S3`)?
- [ ] Apakah beban server & keamanan privasi sudah diterjemahkan menjadi batasan nyata di dokumen `03-SRS-DAN-KONTRAK-LOGIKA.md`?

