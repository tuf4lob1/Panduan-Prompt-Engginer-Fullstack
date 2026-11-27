# Skrip Orkestrasi Dinamis M-AEOS (`workflows/*.wf`)

Folder ini berisi skrip orkestrasi multi-agen paralel yang dieksekusi oleh *tool* internal Google Antigravity **`run_workflow`**.

## Mengapa Menggunakan Ekstensi `.wf` dan Bukan `.py`?

1. Mesin `run_workflow` Google Antigravity menjalankan skrip menggunakan kompilator khusus Python `PyCF_ALLOW_TOP_LEVEL_AWAIT` (serupa dengan sel *Jupyter Notebook*) yang **mewajibkan** pemanggilan `await` di level teratas serta menyuntikkan primitif bawaan (`phase`, `agent`, `parallel`, `pipeline`, `log`) secara otomatis saat dijalankan.
2. Jika disimpan sebagai `.py` biasa, *Language Server* Python standar di IDE (Pylance / Pyright / Ruff) akan menganggapnya sebagai modul Python biasa dan memunculkan peringatan palsu `await can only be used inside an async function` serta `agent is not defined`.
3. Dengan ekstensi **`.wf`**, panel *Problems* IDE tetap **100% bersih tanpa error palsu**, sementara `run_workflow(ScriptPath=".../nama_file.wf")` tetap mengeksekusinya secara *native* dan divalidasi sintaksnya oleh `scripts/gates/verify-maeos-template.py`.

## Daftar Workflow Tersedia

- `blueprint_discovery_pipeline.wf`: Menjalankan riset Analisis Sistem & Birokrasi (`principal-analyst`), lalu memicu perancangan Arsitektur Ringan (`principal-architect`) dan Desain UI/UX Anti-Slop (`principal-ux-designer`) secara paralel.
- `adversarial_gate_tribunal.wf`: Menjalankan sidang penguji silang secara paralel antara Security Red-Team (`principal-redteam`), QA Chaos (`principal-qa-sdet`), dan SRE Maintainability (`principal-sre-steward`).

