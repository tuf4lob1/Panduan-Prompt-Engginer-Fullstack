#!/usr/bin/env python3
"""
Skrip Verifikasi Integritas Repositori Template M-AEOS.
Memastikan seluruh kernel konstitusi, 8 subagent spesialis, 9 skill riset,
file referensi, hooks, workflows, dan ruang artefak valid 100%.
"""

import ast
import json
import os
import re
import subprocess
import sys

REQUIRED_SUBAGENTS = [
    "principal-analyst",
    "principal-architect",
    "principal-ux-designer",
    "principal-frontend",
    "principal-backend",
    "principal-redteam",
    "principal-qa-sdet",
    "principal-sre-steward",
]

REQUIRED_SKILLS = [
    "maeos-intake-triage",
    "deep-domain-bureaucracy-analysis",
    "system-data-lightweight-architecture",
    "anti-slop-cognitive-ux-design",
    "zero-bloat-frontend-engineering",
    "high-efficiency-backend-engineering",
    "adversarial-appsec-redteam",
    "stateful-qa-chaos-verification",
    "sre-maintainability-stewardship",
]


def check_frontmatter(path: str, expected_name: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert text.startswith("---\n"), f"Frontmatter hilang pada {path}"
    end = text.find("\n---\n", 4)
    assert end != -1, f"Frontmatter tidak tertutup pada {path}"
    fm = text[4:end]
    m_name = re.search(r"^name:\s*(.+)$", fm, re.M)
    assert m_name, f"Field 'name' hilang pada {path}"
    actual = m_name.group(1).strip()
    assert actual == expected_name, f"Nama tidak cocok di {path}: {actual} != {expected_name}"
    assert re.search(r"^description:", fm, re.M), f"Field 'description' hilang pada {path}"


def main() -> int:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    # 1. Cek ukuran AGENTS.md (< 24.000 byte sesuai batas Antigravity)
    agents_md = os.path.join(root, "AGENTS.md")
    assert os.path.isfile(agents_md), "AGENTS.md tidak ditemukan!"
    size = os.path.getsize(agents_md)
    assert size < 24000, f"AGENTS.md melebihi batas 24KB Antigravity ({size} byte)!"
    print(f"[OK] AGENTS.md valid ({size} / 24000 byte)")

    # 2. Cek seluruh 8 Subagent
    for ag in REQUIRED_SUBAGENTS:
        p = os.path.join(root, ".agents", "agents", f"{ag}.md")
        assert os.path.isfile(p), f"Subagent hilang: {p}"
        check_frontmatter(p, ag)
    print(f"[OK] Seluruh {len(REQUIRED_SUBAGENTS)} Subagent terisolasi valid")

    # 3. Cek seluruh 9 Skill beserta tautan referensinya
    for sk in REQUIRED_SKILLS:
        p = os.path.join(root, ".agents", "skills", sk, "SKILL.md")
        assert os.path.isfile(p), f"Skill hilang: {p}"
        check_frontmatter(p, sk)
        with open(p, "r", encoding="utf-8") as f:
            body = f.read()
        for rel_link in re.findall(r"\]\(\./(references/[^)]+)\)", body):
            ref_file = os.path.join(os.path.dirname(p), rel_link)
            assert os.path.isfile(ref_file), f"File referensi putus di {sk}: {rel_link}"
    print(f"[OK] Seluruh {len(REQUIRED_SKILLS)} Skill & file referensi mendalam valid")

    # 4. Cek hooks.json & uji simulasi Gate Guard
    hooks_path = os.path.join(root, ".agents", "hooks.json")
    with open(hooks_path, "r", encoding="utf-8") as f:
        hooks_cfg = json.load(f)
    assert "maeos-zero-premature-coding-guard" in hooks_cfg
    guard_script = os.path.join(root, "scripts", "gates", "pre-tool-gate-guard.py")

    # Simulasi blokir tulis ke src/ saat Gate 0-2 belum disetujui
    blocked_payload = json.dumps(
        {"toolCall": {"name": "write_file", "args": {"Path": os.path.join(root, "src", "index.ts")}}}
    )
    res_block = subprocess.run(
        [sys.executable, guard_script],
        input=blocked_payload,
        text=True,
        capture_output=True,
        check=True,
    )
    out_block = json.loads(res_block.stdout)
    assert out_block.get("decision") == "deny", f"Gate Guard gagal memblokir src/: {out_block}"

    # Simulasi izinkan tulis ke docs/project/01-analysis/
    allowed_payload = json.dumps(
        {
            "toolCall": {
                "name": "write_file",
                "args": {"Path": os.path.join(root, "docs", "project", "01-analysis", "01-DOMAIN-DAN-AKTOR.md")},
            }
        }
    )
    res_allow = subprocess.run(
        [sys.executable, guard_script],
        input=allowed_payload,
        text=True,
        capture_output=True,
        check=True,
    )
    out_allow = json.loads(res_allow.stdout)
    assert out_allow.get("decision") == "allow", f"Gate Guard salah memblokir docs/: {out_allow}"
    print("[OK] Hooks JSON & simulasi PreToolUse Gate Guard bekerja presisi")

    # 5. Cek sintaks Python Top-Level Await pada workflows/*.wf
    for wf_name in ["blueprint_discovery_pipeline.wf", "adversarial_gate_tribunal.wf"]:
        wf_path = os.path.join(root, "workflows", wf_name)
        with open(wf_path, "r", encoding="utf-8") as f:
            src = f.read()
        compile(src, wf_name, "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    print("[OK] Seluruh skrip orkestrasi workflows/*.wf valid secara sintaksis")

    print("\nSELURUH EKOSISTEM M-AEOS LULUS VERIFIKASI INTEGRITAS 100%!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

