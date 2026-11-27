---
dokumen: Analisis Domain, Struktur Organisasi & Matriks Aktor
divisi_pembuat: D-01 (Principal System, Domain & Bureaucracy Analyst)
gerbang_terkait: Gate 1
status: DRAF
versi: 1.0.0
terakhir_diperbarui: -
---

# 01 — Analisis Domain, Organisasi & Matriks Wewenang Aktor

## 1. Visi Operasional & Batas Ruang Lingkup
- **Masalah Inti yang Diselesaikan**:
- **Ukuran Keberhasilan Terukur (KPI Sistem)**:
- **Di Dalam Ruang Lingkup (*In-Scope* Fase Ini)**:
- **Di Luar Ruang Lingkup (*Out-of-Scope* Eksplisit)**:

## 2. Kamus Istilah Baku Domain (*Ubiquitous Language*)
> Seluruh penamaan tabel, API, label UI, dan dokumentasi wajib konsisten menggunakan istilah di bawah ini.

| Istilah Baku | Kode Sistem (Inggris/Teknis) | Definisi Tegas & Contoh Nyata |
| :--- | :--- | :--- |
| `[Contoh: Berkas Pengajuan]` | `submission` | `[Definisi spesifik tanpa multitafsir]` |

## 3. Struktur Organisasi, Multi-Unit & Pendelegasian Jabatan
- **Model Hierarki Organisasi**: `[Tunggal / Multi-Cabang / Multi-Tenant / Pohon Instansi: Pusat -> Dinas/Direktorat -> Bidang -> Seksi]`
- **Aturan Pemisahan Orang vs Jabatan**: `[Jelaskan apakah hak akses melekat pada akun pengguna langsung atau melalui penugasan jabatan/mandat]`
- **Mekanisme Pendelegasian Sementara (*Plt / Plh / Pejabat Pengganti*)**: `[Bagaimana sistem menangani pejabat cuti, dinas luar, atau mutasi di tengah proses berjalan]`

## 4. Katalog Aktor & Profil Konteks Kerja
| Kode Peran | Nama Peran / Jabatan | Frekuensi Pakai & Perangkat Utama | Tujuan Utama & Titik Rawan Kesalahan Manusia |
| :--- | :--- | :--- | :--- |
| `ACT-01` | `[Nama Peran]` | `[Harian 8 jam Desktop / Harian HP Lapangan / Insidental]` | `[Apa yang dikerjakan & kesalahan apa yang harus dicegah UI/sistem]` |

## 5. Matriks Hak Akses & Cakupan Visibilitas Data (RBAC + ABAC)
> Keterangan Cakupan: `NONE` (Dilarang), `OWN` (Milik Sendiri), `ASSIGNED` (Didisposisikan), `UNIT` (Satu Unit Kerja), `SUBTREE` (Unit & Bawahan), `GLOBAL` (Seluruh Sistem).

| Modul / Entitas | Aksi Spesifik | `ACT-01` | `ACT-02` | `ACT-03` | Aturan Pemisahan Tugas (*Segregation of Duties*) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[Entitas]` | Lihat Daftar & Detail | | | | `[Misal: Pemeriksa tidak boleh menyetujui draf buatannya sendiri]` |
| `[Entitas]` | Buat / Ajukan Baru | | | | |
| `[Entitas]` | Verifikasi / Paraf | | | | |
| `[Entitas]` | Setujui / Sahkan | | | | |
| `[Entitas]` | Batalkan / Adendum | | | | |
| `[Entitas]` | Ekspor Laporan | | | | |

