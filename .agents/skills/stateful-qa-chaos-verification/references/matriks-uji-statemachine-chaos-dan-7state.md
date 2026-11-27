# Matriks Uji Mesin Status, Chaos Konkurensi & Daftar Periksa 7-Kondisi UI

Dokumen ini menjadi pedoman teknis penyusunan suite pengujian otomatis oleh Divisi QA/SDET (D-07).

---

## 1. Pola Generator Tes Mesin Status (*State-Transition Coverage*)

Untuk setiap entitas berstatus di sistem, pastikan tes otomatis mencakup 4 kuadran berikut:

| Kuadran Uji | Contoh Skenario Nyata | Hasil Wajib yang Diperiksa (`Assertions`) |
| :--- | :--- | :--- |
| **1. Transisi Sah + Guard Terpenuhi** | Verifikator unit yang tepat memaraf berkas lengkap | HTTP `200`, `status` berpindah tepat, `version` naik `+1`, `audit_logs` bertambah tepat 1 baris dengan snapshot akurat |
| **2. Transisi Sah + Guard Gagal** | Pejabat klik `Kembalikan Revisi` dengan alasan kosong, atau klik `Sahkan` saat pagu kurang Rp1 | HTTP `422`, `status` & `version` **tidak berubah**, saldo pagu utuh, tidak ada nomor resmi terbuang |
| **3. Transisi Tidak Sah (*Illegal Jump*)** | Memicu aksi `SAHKAN` pada berkas berstatus `DRAF` atau `DIBATALKAN` | HTTP `409`, database bersih tanpa perubahan |
| **4. Konflik Versi (*Stale Action*)** | Pejabat A dan B membuka versi `1`; A klik `Paraf` (sukses jadi versi `2`), lalu B klik `Kembalikan` masih membawa `expected_version: 1` | Permintaan A sukses; permintaan B **ditolak `409 Conflict`** dengan pesan jelas tanpa menimpa keputusan A |

---

## 2. Daftar Uji Chaos Ringan yang Wajib Lulus

1. **Uji Palu Idempotensi (*Idempotency Hammer*)**: Kirim 5 permintaan `POST` pembuatan transaksi menggunakan `Idempotency-Key` yang sama persis. **Hasil wajib**: Hanya 1 baris transaksi tercipta di database, tidak ada *uncaught exception 500*.
2. **Uji Perebutan Kuota/Anggaran Terakhir**: Buat sisa anggaran `Rp 10.000.000`, lalu jalankan 5 pengajuan paralel masing-masing `Rp 6.000.000`. **Hasil wajib**: Tepat 1 pengajuan lolos (`Rp 4.000.000` tersisa), 4 pengajuan lainnya ditolak rapi karena pagu tidak cukup!
3. **Uji Perubahan Kebijakan Dinamis (`CFG-XX`)**: Ubah nilai ambang kebijakan di tabel `policy` (misal batas plafon persetujuan langsung), lalu jalankan pengajuan baru. **Hasil wajib**: Sistem langsung mengikuti aturan baru tanpa perlu mengubah kode atau kompilasi ulang!

---

## 3. Daftar Periksa Audit Visual & Interaksi 7-Kondisi

Pastikan tidak ada satu pun cacat pengalaman pengguna berikut yang lolos ke produksi:
- [ ] **Tombol Klik Ganda**: Apakah semua tombol simpan/setujui otomatis nonaktif & menampilkan indikator kerja saat diklik sehingga tidak bisa ditekan berkali-kali?
- [ ] **Ketahanan Refresh & Tombol Back**: Jika pengguna menyaring tabel lalu menekan `F5 (Refresh)`, apakah saringan tetap bertahan berkat *URL state*?
- [ ] **Teks Panjang Ekstrem**: Masukkan judul/nama sepanjang 140 karakter tanpa spasi maupun dengan spasi—apakah kartu atau kolom tabel tetap rapi tanpa menabrak tombol di sebelahnya?
- [ ] **Layar Sempit (`360px` Mobile) & Laptop Kerja (`1366x768`)**: Apakah tombol keputusan utama tetap mudah dijangkau tanpa terpotong tepi layar?
- [ ] **Nol Peringatan Konsol**: Tidak ada error merah di konsol runtime maupun kegagalan hidrasi SSR.

