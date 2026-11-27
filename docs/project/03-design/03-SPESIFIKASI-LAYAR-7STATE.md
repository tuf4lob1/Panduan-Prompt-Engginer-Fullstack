---
dokumen: Spesifikasi Anatomi Komponen & Cetak Biru Layar 7-Kondisi
divisi_pembuat: D-03 (Principal UI/UX Researcher & Designer)
gerbang_terkait: Gate 2
status: DRAF
versi: 1.0.0
terakhir_diperbarui: -
---

# 03 — Spesifikasi Layar, Anatomi Komponen & Matriks 7-Kondisi

> **Kontrak untuk Divisi Frontend (D-04)**: Setiap layar di bawah ini wajib diimplementasikan persis mengikuti tata letak struktural, batas kata mikro, dan ketujuh kondisi statusnya.

---

## 1. Komponen Lintas Halaman (*Global Shell & Domain Components*)
- **Kerangka Navigasi Utama & Pemilih Konteks Jabatan/Unit**:
  `[Spesifikasi sidebar/topbar, bagaimana tampilan di Desktop vs Mobile, dan indikator peran aktif]`
- **Komponen Khusus Domain #1 (`[Misal: Pita Jejak Status Birokrasi / Split-Viewer Dokumen]`)**:
  `[Anatomi elemen, data yang ditampilkan, interaksi klik/keyboard]`

---

## 2. Cetak Biru Per Layar Utama

### Layar `SCR-01`: `[Nama Layar, misal: Meja Kerja Verifikasi & Disposisi]`
- **Aktor Pengguna**: `[ACT-XX]`
- **Kebutuhan Fungsional Terkait**: `[FR-001, FR-004]`
- **Satu Fokus Tindakan Utama (*Primary Goal*)**: `[Misal: Memeriksa antrean prioritas SLA & memberi keputusan paraf/revisi tanpa pindah halaman]`

#### A. Kerangka Tata Letak Struktural (*Desktop >= 1024px & Mobile < 768px*)
```text
+-----------------------------------------------------------------------------------+
| [Konteks Unit/Jabatan Aktif]                       [Cari Cepat /] [Notifikasi]    |
+------------------------+-----------------------------------+----------------------+
| ANTREAN KERJA (30%)    | PRATINJAU BERKAS & DATA (42%)     | PANEL KEPUTUSAN (28%)|
| [Jatuh Tempo (2)][Semua]| Nomor & Perihal (Maks 2 baris)    | [✓ Pagu Tersedia]    |
| ---------------------- | [Pita Status Ringkas 4 Tahap]     | Riwayat Paraf Ringkas|
| > #042 Pengadaan Alat  |                                   |                      |
|   Rp 45.000.000 • 3j   | [Penampil Dokumen / Rincian Item] | Catatan Pemeriksa:   |
| ---------------------- | [Sorotan Perubahan Revisi v1->v2] | [__________________] |
|   #043 Perjalanan Dinas|                                   |                      |
|   Rp 12.400.000 • 1h   |                                   | [Kembalikan] [PARAF] |
+------------------------+-----------------------------------+----------------------+
```
- **Adaptasi Mobile (`< 768px`)**: `[Jelaskan bagaimana 3 panel di atas berubah menjadi alur tumpuk bersih dengan bilah keputusan menempel di bawah jempol]`

#### B. Matriks Wajib 7 Kondisi Layar (`SCR-01`)
| No | Kondisi Sistem | Tampilan Visual & Pesan Mikro Spesifik (Sesuai Anggaran Kata) | Perilaku Interaksi |
| :--- | :--- | :--- | :--- |
| **1** | **Kosong (*Empty State*)** | `[Ikon tenang + "Semua berkas telah diperiksa" + tautan lihat arwayat selesai]` | Fokus tenang tanpa kesan error |
| **2** | **Memuat (*Loading*)** | `[Kerangka baris antrean & blok dokumen dengan tinggi identik agar layar tidak melompat]` | Tombol aksi nonaktif sementara |
| **3** | **Ideal Terisi** | `[Sesuai kerangka struktural di atas]` | Navigasi atas/bawah instan |
| **4** | **Data Ekstrem (*Overflow*)** | `[Perihal 150 karakter dipotong 2 baris dengan tooltip utuh; lampiran >10 pakai pemilih berkas ringkas]` | Tata letak tidak melebar/pecah |
| **5** | **Error Validasi Input** | `[Jika klik Kembalikan tanpa catatan: bingkai fokus + "Tulis alasan revisi minimal 15 karakter."]` | Kursor langsung fokus ke kotak catatan |
| **6** | **Gangguan Jaringan / Gagal** | `[Pita peringatan non-destruktif; ketikan catatan tetap utuh tersimpan di memori lokal + tombol "Coba Kirim Lagi"]` | Cegah klik ganda & cegah hilang ketikan |
| **7** | **Terkunci Birokrasi (*Locked*)** | `[Panel keputusan berubah menjadi blok informasi tenang: "Telah diparaf pada 12 Nov 14:05 — Berkas kini di Kepala Dinas"]` | Seluruh input tertutup aman |

