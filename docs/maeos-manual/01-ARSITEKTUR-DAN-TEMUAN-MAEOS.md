# Arsitektur & Lima Temuan Inti M-AEOS

Dokumen ini menjelaskan fondasi rekayasa di balik **M-AEOS (Multi-Agent Engineering Operating System)** dan bagaimana ia memanfaatkan mesin internal Google Antigravity untuk mengatasi kelemahan bawaan *Large Language Models* (LLM) dalam membangun perangkat lunak skala penuh (*fullstack*).

---

## 1. Mengapa Kumpulan Prompt Panjang Saja Tidak Pernah Cukup?

Banyak pendekatan *prompt engineering* gagal ketika dibawa ke projek produksi nyata karena tiga batasan teknis:
1. **Batas Kuota Aturan & Penurunan Perhatian (*Attention Dilution*)**: Di Google Antigravity, file aturan selalu-aktif (`AGENTS.md`) dibatasi maksimal **24 KB per file** dengan anggaran gabungan **20.000 token**. Jika seluruh instruksi analisis, UI/UX, frontend, backend, dan keamanan dijejalkan ke satu file, aturan akan terpotong atau membuat perhatian model terpecah.
2. **Bias Konfirmasi Mandiri (*Self-Grading Bias*)**: Agen AI yang baru saja menulis 1.000 baris kode secara psikologis statistik cenderung membenarkan desainnya sendiri ketika diminta mengecek *bug* atau celah keamanan di percakapan yang sama.
3. **Regresi ke Rata-Rata Statistik (*AI Slop*)**: Tanpa riset eksplisit dan batasan negatif yang terukur, model selalu memilih pola paling sering muncul di internet: warna ungu-biru neon, komponen kartu seragam dengan teks deskripsi bertele-tele, serta pemasangan pustaka (*library*) populer namun usang/berat.

---

## 2. Lima Pilar Arsitektural M-AEOS

### Pilar 1: Pemisahan Kernel Konstitusi & Playbook On-Demand (*Progressive Disclosure*)
M-AEOS membagi instruksi menjadi tiga lapis:
- **Lapis Konstitusi (`AGENTS.md`)**: Berukuran ramping (<14 KB), selalu dimuat di memori utama untuk menjaga disiplin Orchestrator dan urutan gerbang kualitas.
- **Lapis Isolasi Peran (`.agents/agents/*.md`)**: Setiap divisi berjalan di konteks percakapan subagent tersendiri (*clean context window*) dengan pembatasan hak akses *tool* (misalnya agen Analis, Desainer UX, dan Red-Team tidak memiliki akses modifikasi kode produksi atau eksekusi bebas).
- **Lapis Metodologi Riset Mendalam (`.agents/skills/*/SKILL.md` + `references/`)**: Ribuan baris panduan teknis, matriks keputusan, dan daftar periksa hanya dimuat saat divisi terkait bekerja, sehingga fokus penalaran mencapai 100% tanpa mengotori divisi lain.

### Pilar 2: Protokol Mesin Status Birokrasi (*Bureaucracy State-Machine Protocol / B-SMP*)
Projek enterprise dan pemerintahan sering hancur di tengah jalan karena pengembang menganggap persetujuan hanyalah kolom `status = approved | rejected`. M-AEOS mewajibkan pemodelan:
- Hierarki unit kerja & pemisahan tugas (*Maker, Verifier, Paraf Koordinator, Penyetuju Akhir*).
- Wewenang sementara (*Pelaksana Tugas / Plt, Pelaksana Harian / Plh, Mandat Delegasi*) yang terikat rentang waktu.
- Transisi status deterministik termasuk pengembalian untuk revisi (*Return with Notes*), disposisi bercabang, pembatalan pasca-terbit (*Revocation/Addendum*), dan pembekuan data (*Field/Record Immutability*).
- Jejak audit abadi (*Immutable Audit Trail*) yang merekam pelaku asli, jabatan aktif saat bertindak, dasar kewenangan, waktu presisi, serta selisih data sebelum-sesudah.

### Pilar 3: Rekayasa Kognitif UI/UX & Hukum Anti-Dinding-Teks (*Zero-Text-Wall*)
M-AEOS melarang Frontend merancang tampilan sambil mengetik kode. Divisi Desain UI/UX wajib melakukan riset metode ergonomi kognitif terlebih dahulu:
- **Kalibrasi Kepadatan (*Density Calibration*)**: Membedakan antarmuka kerja harian intensitas tinggi (*High-Density Workbench*) dengan layanan publik satu kali pakai (*Guided Step Flow*).
- **Uji Sipit 3 Detik (*3-Second Squint Test*)**: Hierarki visual harus langsung menunjukkan posisi pengguna, status objek utama, dan satu aksi primer tanpa membaca paragraf penjelasan.
- **Anggaran Kata Mikro (*Microcopy Budget*)**: Mengganti teks instruksi panjang menjadi penanda visual, *stepper*, *status badge* bermakna, dan pengungkapan bertahap (*Progressive Disclosure*).
- **Spesifikasi 7 Kondisi Layar**: Menjamin tidak ada layar pecah saat data kosong, sedang memuat, teks sangat panjang, terjadi galat parsial, jaringan putus, atau dokumen terkunci birokrasi.

### Pilar 4: Pengadilan Beban & Efisiensi Server (*Zero-Bloat Engineering*)
Setiap penambahan ketergantungan dan desain kueri diaudit secara kuantitatif:
- **Pengadilan Pustaka (*Dependency Court*)**: Dilarang menambah *package* pihak ketiga untuk fungsi yang dapat diselesaikan dalam <30 baris kode bersih atau API standar bawaan platform.
- **Anggaran Kueri & Memori**: Larangan mutlak pola kueri berulang di dalam perulangan (*N+1*), kewajiban paginasi berbasis kursor/batas tegas, pelepasan tugas berat (cetak PDF, rekapitulasi besar, pengiriman pesan massal) ke antrean latar belakang, serta desain modular yang sanggup berjalan gesit di server berspesifikasi hemat sekalipun.

### Pilar 5: Sidang Penguji Adversarial (*Red-Team & Chaos Tribunal*)
Gerbang kualitas pasca-implementasi dijalankan oleh agen yang diberi insentif berlawanan dengan pembuat kode:
- `principal-redteam` berasumsi kode memiliki celah keamanan dan aktif mencari cara melompati wewenang birokrasi atau mengintip data unit kerja lain.
- `principal-qa-sdet` berasumsi pengguna akan menekan tombol dua kali bersamaan, memasukkan data ekstrem, dan memutus koneksi di tengah transaksi.
- `principal-sre-steward` berasumsi engineer berikutnya yang merawat sistem ini belum pernah melihat kodenya, sehingga menolak arsitektur yang rumit dirawat.

---

## 3. Alur Serah-Terima Artefak (*Artifact Handshake*)

Di M-AEOS, komunikasi antar-divisi **tidak mengandalkan ingatan percakapan semata**, melainkan melalui dokumen kontrak terstruktur di `docs/project/`. Setiap dokumen wajib memiliki blok metadata status di bagian atas:

```yaml
---
dokumen: Nama Artefak
divisi_pembuat: D-XX (Nama Divisi)
gerbang_terkait: Gate X
status: DRAF | DALAM_REVIEW | PERLU_REVISI | DISETUJUI | FROZEN
versi: 1.0.0
terakhir_diperbarui: YYYY-MM-DD
---
```

Selama dokumen hulu belum berstatus `DISETUJUI` atau `FROZEN`, divisi hilir wajib menolak memulai implementasi dan mengembalikan laporan kekurangan ke Orchestrator.

