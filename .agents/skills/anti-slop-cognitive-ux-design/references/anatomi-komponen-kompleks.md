# Anatomi Komponen Kompleks untuk Sistem Nyata (Startup, Enterprise & Gov)

Gunakan standar anatomi komponen ini saat menyusun spesifikasi di `03-SPESIFIKASI-LAYAR-7STATE.md` agar antarmuka terasa dirancang oleh tim produk papan atas.

---

## 1. Anatomi Tabel Operasional Kelas Enterprise (Bebas Sesak & Bebas Lemot)

Tabel adalah jantung dari 70% aplikasi bisnis dan pemerintahan. Rancang dengan disiplin berikut:
1. **Bilah Filter Cepat (*Quick-Triage Tabs*) di Atas Tabel**:
   Sediakan tab hitung langsung berdasarkan status kerja aktor aktif, misalnya: `Perlu Tindakan Saya (8)` | `Mendekati Tenggat SLA (2)` | `Sedang Diproses (24)` | `Semua`. Pengguna tidak perlu merakit filter rumit untuk tugas rutinnya.
2. **Batas Maksimal 5–7 Kolom Terlihat**:
   Jangan menjejalkan 16 kolom hingga muncul *horizontal scrollbar* menyakitkan. Gabungkan pasangan serumpun (misal `Nomor & Perihal`, `Pemohon & Unit Kerja`) dan pindahkan atribut detail ke panel pratinjau samping saat baris diklik.
3. **Perataan Kolom Matematis**:
   - Teks, nama, dan status: **Rata Kiri**
   - Angka kuantitas, nominal uang, durasi, dan persentase: **Rata Kanan + `tabular-nums`**
   - Aksi baris cepat: **Menempel tetap di ujung kanan (*Sticky Right*)** bila layar sempit.
4. **Adaptasi Layar Ponsel (*Responsive Table Transformation*)**:
   Di layar ponsel `< 768px`, dilarang membiarkan tabel mengecil tak terbaca! Tentukan apakah ia berubah menjadi **Kartu Ringkas Terstruktur (*Structured Action Card*)** yang memuat Judul, Status, Nilai Utama, dan Waktu, atau tabel dengan kolom pertama terkunci.

---

## 2. Anatomi Meja Kerja Verifikasi & Disposisi Birokrasi (*Split-Pane Review*)

Untuk setiap fitur pemeriksaan berkas, klaim, persetujuan anggaran, atau tata naskah dinas:
- **Panel Kiri/Utama (60%–65% lebar Desktop)**: Menampilkan isi substansi pengajuan dan **Pratinjau Langsung Dokumen Lampiran (PDF/Gambar)** di dalam halaman (tanpa memaksa unduh berkas satu per satu ke komputer!).
- **Panel Kanan Tetap (*Sticky Decision Rail*, 35%–40% lebar Desktop)**:
  1. Ringkasan kepatuhan otomatis sistem (misal: `[✓ Pagu Cukup]`, `[✓ Lampiran Lengkap]`, `[! Mendekati Tenggat 4 Jam Lagi]`).
  2. Riwayat jejak paraf & catatan pejabat sebelumnya secara kronologis ringkas.
  3. Kotak catatan disposisi/alasan (wajib terisi otomatis menjadi syarat aktif jika memilih *Kembalikan Revisi* atau *Tolak*).
  4. Tombol keputusan tegas dengan pemisahan visual antara aksi setuju dan aksi kembalikan/tolak.

---

## 3. Anatomi Formulir Panjang Anti-Lelah (15 s/d 100+ Input)

1. **Pengisian Pintar & Pencegahan Ketik Ulang**: Ambil semua data yang sudah diketahui sistem secara otomatis; sediakan pencarian pilih cepat (*combobox searchable*) untuk daftar panjang (> 7 pilihan), dan tombol radio/segmen terbuka untuk pilihan sedikit (2–4 pilihan, jangan disembunyikan di dalam dropdown sehingga menghemat 1 klik!).
2. **Validasi Ramah Waktu (*Reward Early, Punish Late*)**:
   - Jangan memunculkan tulisan merah `"Email tidak valid!"` saat pengguna baru mengetik huruf ke-2!
   - Munculkan pesan salah hanya **setelah pengguna berpindah keluar dari kolom tersebut (`onBlur`)**, namun segera hilangkan tanda merah begitu ketikan pengguna menjadi benar!
3. **Perlindungan Kehilangan Ketikan**: Untuk formulir panjang, rancang mekanisme `Simpan sebagai Draf` kapan saja (meskipun belum semua kolom wajib terisi!) dan peringatan pencegah bila pengguna tak sengaja menutup tab saat ada perubahan belum tersimpan.

---

## 4. Anatomi Navigasi Berdasarkan Peran & Beban Sistem

- **Maksimal 5–7 Menu Tingkat Atas**: Jika sistem memiliki 25 modul besar (seperti ERP atau Portal Instansi), kelompokkan secara fungsional dengan sub-kelompok berlabel tipis, dan **sembunyikan total menu modul yang sama sekali tidak boleh diakses oleh peran pengguna tersebut** (jangan menampilkan 15 menu yang ketika diklik memunculkan pesan *"Akses Ditolak 403"*!).
- **Indikator Konteks Jabatan Aktif (Khusus Skala `S2` / `S3`)**: Jika satu pengguna memiliki mandat rangkap (misal Jabatan Definitif + Mandat *Plt.* di bidang lain, atau akses ke 3 cabang perusahaan), tampilkan **Pemilih Konteks Jabatan/Unit Aktif** yang sangat jelas di pojok atas layar agar pengguna selalu sadar sedang bertindak atas nama kursi jabatan yang mana.

