# Panduan Rekayasa Birokrasi Kompleks & Mesin Status (B-SMP)

Dokumen referensi ini digunakan untuk memodelkan organisasi dengan tata kelola ketat seperti Kementerian/Lembaga, Pemerintah Daerah (SPBE), BUMN, Rumah Sakit, Universitas, Perbankan, dan Korporasi Besar.

---

## 1. Empat Kesalahan Fatal Developer Saat Membuat Sistem Birokrasi

1. **Mengikat Hak Akses Langsung ke Tabel `users` (`user.role = 'kepala_dinas'`)**:
   - *Masalah Nyata*: Saat pejabat tersebut mutasi ke dinas lain, pensiun, atau merangkap jabatan *Plt.* di unit sebelah, seluruh histori dokumen lama ikut rusak atau ia kehilangan/kelebihan akses di unit yang salah.
   - *Pola Benar M-AEOS*: Pisahkan tiga entitas:
     - **Individu (`Person / User`)**: Identitas manusia (NIP/NIK/Email).
     - **Jabatan Struktural/Fungsional (`Position / StructuralNode`)**: Kursi jabatan di dalam pohon unit kerja (misal: *Kepala Bidang Perbendaharaan - BPKAD*).
     - **Penugasan Jabatan (`PositionAssignment / Mandate`)**: Menghubungkan Individu ke Jabatan dengan atribut `jenis_penugasan` (`DEFINITIF | PLT | PLH | PJ | DELEGASI_KHUSUS`), `berlaku_mulai`, `berlaku_sampai`, dan `nomor_sk_dasar`.

2. **Menimpa Data Dokumen Secara Langsung Saat Revisi**:
   - *Masalah Nyata*: Dalam audit inspektorat/BPK/internal, pemeriksa selalu bertanya: *"Apa isi draf awal sebelum dikoreksi verifikator, dan mengapa angkanya berubah?"*
   - *Pola Benar M-AEOS*: Gunakan **Snapshot Versi Dokumen (`DocumentRevision`)** pada setiap perpindahan tahap persetujuan, sehingga selisih perubahan antar-versi selalu terlacak utuh.

3. **Penomoran Resmi Diberikan Terlalu Cepat (Saat Draf) dan Menyisakan Nomor Bolong**:
   - *Masalah Nyata*: Nomor surat keluar, nomor SK, nomor faktur, atau nomor SPM sering tidak boleh melompat/bolong tanpa berita acara.
   - *Pola Benar M-AEOS*: Selama status `DRAF` hingga `MENUNGGU_PENGESAHAN`, gunakan **Nomor Registrasi Internal Sementara**. Nomor resmi baru diterbitkan secara atomik (*transactional sequence lock*) tepat pada detik status berubah menjadi `DISAHKAN / TERBIT`.

4. **Mengizinkan Penghapusan Fisik (`Hard Delete`) atau Pengeditan Diam-Diam Pasca-Persetujuan**:
   - *Pola Benar M-AEOS*: Begitu dokumen melewati gerbang persetujuan pertama, kolom substansi terkunci. Setelah status `TERBIT / DISETUJUI_AKHIR`, dokumen bersifat **100% Immutable**. Koreksi hanya boleh dilakukan melalui entitas baru yang merujuk ke dokumen asal: **Adendum**, **Revisi Resmi Versi Baru**, atau **Pembatalan Resmi (*Revocation*)**.

---

## 2. Pola Alur Persetujuan & Disposisi yang Wajib Dikenali

Pilih dan kombinasikan pola berikut sesuai kebutuhan nyata projek:

| Pola Birokrasi | Cara Kerja | Kapan Digunakan |
| :--- | :--- | :--- |
| **Berjenjang Linier (*Sequential Chain*)** | Pembuat → Verifikator Teknis → Kasubbag/Kasi (Paraf 1) → Kabid (Paraf 2) → Kepala/Direktur (Setuju Akhir) | Pengajuan surat keluar, SK, pencairan anggaran rutin |
| **Ambang Batas Nilai (*Threshold Routing*)** | <= Rp10 Juta cukup Manajer Cabang; Rp10–100 Juta wajib Kepala Divisi; > Rp100 Juta wajib Direksi + Komite Keuangan | Pengadaan barang/jasa, klaim asuransi, persetujuan kredit/diskon |
| **Paralel Lintas Unit (*Parallel Clearance*)** | Dokumen diperiksa bersamaan oleh Divisi Hukum, Divisi Keuangan, dan Divisi Teknis; baru naik ke Direktur jika ketiganya memberi tanda layak | Kontrak kerja sama (MoU/PKS), peluncuran proyek besar |
| **Kuorum Komite (*Quorum Voting*)** | Dari 5 anggota komite penilai, minimal 3 harus menyetujui dan 0 hak veto menolak | Sidang etik, komite kredit, seleksi tender/hibah |
| **Pohon Disposisi (*Hierarchical Disposition*)** | Surat masuk diterima Sekretariat → Pimpinan memberi instruksi + memilih 1 atau beberapa bawahan → Bawahan meneruskan disposisi turunan ke staf pelaksana → Laporan tindak lanjut naik kembali | Tata naskah dinas elektronik (E-Office / Srikandi-style) |

---

## 3. Standar Tabel Spesifikasi Mesin Status (Wajib Ada di Dokumen Analisis)

Setiap alur kerja kompleks harus dituangkan ke dalam tabel transisi formal seperti format berikut:

| Status Asal | Aksi / Pemicu | Aktor Berwenang | Syarat Penjaga (*Guard Conditions*) | Status Tujuan | Kunci Edit? | Catatan / Efek Samping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `DRAF` | `AJUKAN` | Pembuat (`OWN`) | Semua kolom wajib terisi; lampiran >= 1; pagu tersedia | `MENUNGGU_VERIFIKASI` | Terkunci bagi Pembuat | Rekam Snapshot v1; kirim tugas ke antrean Verifikator unit |
| `MENUNGGU_VERIFIKASI` | `KEMBALIKAN_REVISI` | Verifikator Unit | Wajib mengisi catatan alasan revisi minimal 15 karakter | `PERLU_REVISI_PEMBUAT` | Terbuka kembali bagi Pembuat | Notifikasi poin koreksi; SLA pemeriksaan dihentikan sementara |
| `MENUNGGU_VERIFIKASI` | `PARAF_LANJUT` | Verifikator Unit (Bukan Pembuat!) | Checklist kelengkapan berkas tercentang 100% | `MENUNGGU_PENGESAHAN` | Terkunci Penuh | Rekam paraf digital + jabatan aktif |
| `MENUNGGU_PENGESAHAN` | `SAHKAN` | Pejabat Penyetuju / Plt Sah | Mandat jabatan masih aktif pada detik klik; kuota/pagu masih sah | `TERBIT` | **Abadi (Immutable)** | Terbitkan Nomor Resmi Atomik; potong pagu final; buat dokumen resmi |
| `TERBIT` | `AJUKAN_PEMBATALAN` | Kepala Unit / Pejabat Penyetuju | Wajib melampirkan Berita Acara alasan pembatalan | `MENUNGGU_PEMBATALAN` | **Abadi (Immutable)** | Dokumen asli tidak diubah; memicu sub-alur persetujuan pembatalan |

---

## 4. Spesifikasi Jejak Audit Abadi (*Immutable Audit Trail 5W+1H*)

Untuk sistem `S2-Enterprise` dan `S3-Gov-Birokrasi`, setiap perubahan status dan data sensitif wajib menyimpan rekam audit yang **tidak memiliki fitur UPDATE maupun DELETE di level aplikasi**:
- **Who (Siapa)**: `actor_user_id` + `actor_nama_lengkap` (disimpan sebagai teks snapshot) + `acting_position_id` + `acting_position_title` + `mandate_type` (`DEFINITIF` / `PLT` / `PLH`).
- **What (Apa)**: Nama entitas, ID rekaman, jenis aksi (`AJUKAN`, `PARAF`, `TOLAK`, `LIHAT_DOKUMEN_RAHASIA`, `EKSPOR_DATA`), serta ringkasan perubahan nilai (`before_snapshot` & `after_snapshot` hanya pada atribut yang berubah).
- **When (Kapan)**: Waktu server UTC presisi milidetik (`created_at_utc`) yang diambil dari jam server terpusat (dilarang mengambil waktu dari perangkat klien!).
- **Where (Dari Mana)**: Alamat IP, identitas sesi, dan penanda jejak permintaan (`request_trace_id`).
- **Why (Mengapa)**: Alasan tindakan / komentar disposisi / nomor SK dasar tindakan.
- **How (Integritas Opsional S3)**: Rantai hash kriptografis (`previous_hash` + `current_hash`) bila diperlukan pembuktian anti-manipulasi database tingkat tinggi.

