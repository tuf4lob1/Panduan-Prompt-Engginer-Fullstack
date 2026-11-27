---
dokumen: Sistem Desain Karakter Visual & Token Fungsional (Anti-AI-Slop)
divisi_pembuat: D-03 (Principal UI/UX Researcher & Designer)
gerbang_terkait: Gate 2
status: DRAF
versi: 1.0.0
terakhir_diperbarui: -
---

# 02 — Sistem Desain Anti-Generik & Token Fungsional

## 1. Identitas & Karakter Visual Produk (*Design Manifesto*)
- **Kepribadian Visual**: `[Misal: Tegas, Berwibawa, Tenang, Presisi Tinggi — terinspirasi cetak arsip modern & meja kerja finansial]`
- **Aturan Pembeda dari Template AI**: `[Jelaskan komitmen visual spesifik: bebas gradasi neon, garis batas 1px tajam, warna hanya muncul saat membawa makna status/aksi]`

## 2. Sistem Token Warna Semantik (Teruji Kontras WCAG AA)
### A. Permukaan & Garis Batas (*Surfaces & Borders*)
| Nama Token | Nilai Hex (Light) | Nilai Hex (Dark - Opsional) | Fungsi Penggunaan Tegas |
| :--- | :--- | :--- | :--- |
| `--bg-canvas` | `[#...]` | `[#...]` | Latar dasar ruang kerja agar mata tidak silau |
| `--bg-surface` | `[#...]` | `[#...]` | Permukaan kartu utama, tabel, dan panel kerja |
| `--bg-subtle` | `[#...]` | `[#...]` | Baris kepala tabel, area terkunci/read-only |
| `--border-hairline` | `[#...]` | `[#...]` | Pemisah struktur utama `1px` |

### B. Hierarki Teks & Aksen Aksi Utama
| Nama Token | Nilai Hex | Rasio Kontras terhadap Surface | Aturan Pemakaian |
| :--- | :--- | :--- | :--- |
| `--text-primary` | `[#...]` | `[>= 9:1]` | Judul, nilai utama, isi dokumen |
| `--text-secondary` | `[#...]` | `[>= 5:1]` | Label kolom, metadata waktu/unit |
| `--accent-primary` | `[#...]` | `[>= 4.5:1 dengan teks tombol]` | **Hanya** untuk 1 tombol aksi primer per area fokus |

### C. Warna + Ikon Status Birokrasi / Transaksi (Ramah Buta Warna)
| Status Sistem | Token Latar Halus | Token Teks/Garis | Bentuk Ikon Wajib | Label UI (Maks 3 Kata) |
| :--- | :--- | :--- | :--- | :--- |
| `DRAF` | `[#...]` | `[#...]` | `[Lingkaran titik-titik]` | `Draf` |
| `MENUNGGU_VERIFIKASI` | `[#...]` | `[#...]` | `[Jam / Lingkaran setengah]` | `Menunggu Verifikasi` |
| `PERLU_REVISI` | `[#...]` | `[#...]` | `[Panah putar balik / Segitiga]` | `Perlu Revisi` |
| `TERBIT / DISETUJUI` | `[#...]` | `[#...]` | `[Perisai centang]` | `Disahkan` |
| `DITOLAK / BATAL` | `[#...]` | `[#...]` | `[Silang tegas]` | `Ditolak` |

## 3. Sistem Tipografi & Disiplin Angka
- **Fon Antarmuka Utama (*UI Sans*)**: `[Nama Fon + alasan kejelasan karakter angka/huruf]`
- **Fon Kode / Nomor Surat / Hash (*Monospace*)**: `[Nama Fon]`
- **Kewajiban `tabular-nums`**: Berlaku mutlak untuk seluruh kolom uang, kuantitas, tanggal, waktu hitung mundur SLA, dan kode registrasi.
- **Skala Ukuran & Tinggi Baris**:
  - Judul Halaman (`H1`): `[Misal: 20px / 28px, SemiBold — bukan 36px raksasa untuk aplikasi kerja!]`
  - Judul Bagian (`H2`): `[Misal: 15px / 22px, SemiBold]`
  - Isi Utama & Input: `[Misal: 14px / 20px, Regular]`
  - Sel Tabel & Metadata: `[Misal: 13px / 18px, Regular/Medium]`

## 4. Skala Ruang, Radius, & Standar Aksesibilitas Interaksi
- **Grid Spasi Dasar**: Kelipatan `4px` (`4, 8, 12, 16, 24, 32, 48px`).
- **Radius Sudut**: `[Misal: 6px untuk tombol/input, 8px untuk panel/kartu — hindari pembulatan ekstrem tidak seragam]`.
- **Standar Fokus Keyboard & Target Sentuh**: Cincin fokus `2px` jelas untuk pengguna `Tab/Enter`, tinggi input/tombol desktop `36px`, tinggi sentuh mobile minimal `44px–48px`.

