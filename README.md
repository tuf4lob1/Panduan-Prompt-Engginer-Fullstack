# M-AEOS (Multi-Agent Engineering Operating System)

**Sistem Operasi Rekayasa Perangkat Lunak Multi-Agen untuk Google Antigravity**

M-AEOS adalah **GitHub Template Repository** berbahasa Indonesia yang mengubah Google Antigravity dari sekadar asisten pembuat kode tunggal menjadi **organisasi Principal Engineering & Product Design lintas divisi** dengan **Isolasi Peran Ketat (*Role Isolation*)**, **Protokol Riset Mendalam (*Deep Research Playbooks*)**, dan **Gerbang Kualitas Silang (*Adversarial Quality Gates*)**.

---

## Mengapa M-AEOS Dibuat?

Pengembangan perangkat lunak *fullstack* menggunakan AI konvensional hampir selalu jatuh ke dalam 7 jebakan klasik:
1. **Analisis Spesifikasi Lemah**: Langsung menulis kode tanpa memetakan proses bisnis nyata, *edge-case*, dan alur birokrasi berjenjang (disposisi, paraf, *Plt/Plh*, pembatalan, audit).
2. **Desain UI/UX Generik Buatan AI (*AI Slop*)**: Warna ungu-biru klise, tata letak seragam tanpa hierarki visual, dan antarmuka penuh teks penjelasan panjang yang membingungkan pengguna.
3. **Frontend Berat & Boros Memori**: Asal memasang belasan *library* besar tanpa audit ukuran *bundle* dan merender seluruh halaman di sisi klien tanpa strategi.
4. **Backend & Server Berat**: Penuh *query* `N+1`, skema database tanpa indeks terukur, tidak tahan klik ganda (*race condition*), dan memakan RAM/CPU besar bahkan saat pengguna sedikit.
5. **Keamanan Rapuh**: Sekadar memasang halaman *login*, namun bocor terhadap serangan IDOR, manipulasi hak akses jabatan, dan lompatan status ilegal.
6. **Banyak Bug Tersembunyi**: Agen yang menulis kode diminta memeriksa kodenya sendiri (*Self-Grading Hallucination*).
7. **Maintenance Ribet**: Kode tercampur aduk (*spaghetti*), aturan bisnis ditanam mati (*hardcoded*), tanpa catatan keputusan arsitektur (ADR) maupun panduan operasi.

**M-AEOS memutus ketujuh masalah tersebut dari akarnya** melalui pemisahan wewenang 8 divisi spesialis dan 7 gerbang kualitas yang tidak bisa dilompati.

---

## Arsitektur Ekosistem Repositori

```text
.
├── AGENTS.md                               # Konstitusi Utama (<14 KB): Hukum Orchestrator & Quality Gates
├── README.md                               # Dokumentasi & Panduan Cepat Pemakaian Template
├── .agents/                                # Mesin Native Google Antigravity
│   ├── hooks.json                          # Penjaga otomatis siklus eksekusi (Lifecycle Gatekeepers)
│   ├── agents/                             # Subagent Spesialis dengan Pembatasan Tool (Role Isolation)
│   │   ├── principal-analyst.md            # D-01: Analis Sistem, Domain & Birokrasi
│   │   ├── principal-architect.md          # D-02: Arsitek Sistem, Database & Infrastruktur Ringan
│   │   ├── principal-ux-designer.md        # D-03: Periset UI/UX Kognitif & Desainer Anti-Generik
│   │   ├── principal-frontend.md           # D-04: Engineer Frontend Performa Tinggi (Zero-Bloat)
│   │   ├── principal-backend.md            # D-05: Engineer Backend Modular & Hemat Resource
│   │   ├── principal-redteam.md            # D-06: Auditor Keamanan & Pembobol Sistem (Read-Only)
│   │   ├── principal-qa-sdet.md            # D-07: Engineer QA, Uji Transisi Status & E2E
│   │   └── principal-sre-steward.md        # D-08: Pengawal Keringanan Server & Kemudahan Maintenance
│   └── skills/                             # Playbook Riset Mendalam (Progressive Disclosure)
│       ├── maeos-intake-triage/
│       ├── deep-domain-bureaucracy-analysis/
│       ├── system-data-lightweight-architecture/
│       ├── anti-slop-cognitive-ux-design/
│       ├── zero-bloat-frontend-engineering/
│       ├── high-efficiency-backend-engineering/
│       ├── adversarial-appsec-redteam/
│       ├── stateful-qa-chaos-verification/
│       └── sre-maintainability-stewardship/
├── scripts/gates/                          # Skrip pemeriksa gerbang kualitas & kebersihan repo
├── workflows/                              # Skrip orkestrasi multi-agen paralel (run_workflow)
└── docs/
    ├── maeos-manual/                       # Dokumentasi filosofi, standar, & panduan kerja M-AEOS
    └── project/                            # Ruang Artefak Projek Aktif (Single Source of Truth)
        ├── 00-governance/                  # Status projek & profil skala (Startup / Enterprise / Gov)
        ├── 01-analysis/                    # Riset domain, aktor, state-machine birokrasi, & SRS
        ├── 02-architecture/                # ADR, pemilihan stack, ERD + indeks, & kontrak API
        ├── 03-design/                      # Riset paradigma UX, design tokens, & spek layar 7-kondisi
        ├── 04-quality-gates/               # Berita acara & laporan pengujian Gate 0 s/d Gate 6
        └── 08-operations/                  # Panduan deploy, migrasi aman, & pemeliharaan jangka panjang
```

---

## Cara Menggunakan Template Ini untuk Projek Baru

1. **Gunakan sebagai Template**: Klik **"Use this template"** di GitHub (atau salin folder repositori ini) untuk membuat repositori projek baru Anda.
2. **Buka di Google Antigravity**: Buka folder projek di Antigravity IDE / Antigravity 2.0 / `agy` CLI. Antigravity secara otomatis membaca `AGENTS.md`, seluruh subagent di `.agents/agents/`, dan skill di `.agents/skills/`.
3. **Mulai Percakapan Pertama (Gate 0 — Triage)**:
   Cukup jelaskan ide atau kebutuhan projek Anda dengan bahasa alami. Contoh:
   > *"Saya ingin membangun sistem manajemen pengajuan anggaran & disposisi kegiatan berjenjang untuk instansi pemerintah daerah, dipakai oleh staf sampai kepala dinas, dan harus ringan dijalankan di server VPS internal."*
   atau:
   > *"Saya ingin membuat produk SaaS manajemen klinik multi-cabang yang cepat, desainnya bersih tidak seperti template AI, dan mudah dirawat sendiri."*
4. **Ikuti Alur Kolaborasi Principal Team**:
   - **Gate 0**: Orchestrator akan melakukan wawancara singkat yang tajam untuk mengunci `SCALE_PROFILE.md`.
   - **Gate 1**: Divisi Analis (`principal-analyst`) akan meriset domain A–Z dan memetakan seluruh aktor, aturan bisnis, birokrasi, serta *edge-case* di `docs/project/01-analysis/`.
   - **Gate 2**: Divisi Arsitek (`principal-architect`) dan Divisi Desain UI/UX (`principal-ux-designer`) bekerja menyusun arsitektur super ringan serta sistem desain UI/UX anti-generik bebas dinding teks sebelum koding dimulai.
   - **Gate 3 s/d Gate 6**: Pembangunan terisolasi oleh Frontend & Backend, diikuti pembobolan keamanan oleh Red-Team, pengujian ekstrem oleh QA, dan audit kemudahan *maintenance* oleh SRE.

---

## Skala Projek yang Didukung

- **`S1-Startup`**: Fokus MVP cepat, arsitektur *Modular Monolith* hemat biaya server, UX tajam & konversi tinggi, bebas utang teknis parah.
- **`S2-Enterprise`**: Multi-tenant, integrasi pihak ketiga kompleks, pemisahan modul bisnis ketat, performa data skala besar, observabilitas lengkap.
- **`S3-Gov-Birokrasi`**: Alur birokrasi bertingkat (*Maker-Verifier-Approver*), disposisi surat/dokumen, pendelegasian *Plt/Plh*, jejak audit abadi (*Immutable Audit Log*), kepatuhan regulasi (UU PDP / SPBE), dan antarmuka jelas bagi pengguna lintas generasi.

