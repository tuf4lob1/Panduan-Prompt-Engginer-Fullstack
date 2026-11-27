#!/usr/bin/env python3
"""
M-AEOS PreToolUse Gate Guard:
Menegakkan Pasal 1 AGENTS.md (Hukum Anti-Koding Dini) secara deterministik.
Memblokir write_file / edit_file ke direktori kode sumber produksi apabila
Gate 0, Gate 1, dan Gate 2 di PROJECT_STATE.md belum berstatus DISETUJUI / FROZEN.
"""

import json
import os
import re
import sys

PROTECTED_APP_DIRS = {
    "src",
    "app",
    "frontend",
    "backend",
    "packages",
    "cmd",
    "internal",
    "server",
    "client",
    "migrations",
}


def is_gate_approved(state_text: str, gate_label: str) -> bool:
    pattern = rf"\|\s*\*\*{re.escape(gate_label)}\*\*.*?\|\s*`([^`]+)`\s*\|"
    match = re.search(pattern, state_text)
    if not match:
        return False
    status = match.group(1).strip().upper()
    return status in {"DISETUJUI", "FROZEN", "LULUS"}


def main() -> None:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
        args = payload.get("toolCall", {}).get("args", {}) or {}
        target_path = args.get("Path", "")

        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        if not target_path:
            print(json.dumps({"decision": "allow"}))
            return

        abs_target = os.path.abspath(target_path)
        if not abs_target.startswith(repo_root + os.sep):
            print(json.dumps({"decision": "allow"}))
            return

        rel_target = os.path.relpath(abs_target, repo_root)
        top_dir = rel_target.split(os.sep)[0]

        if top_dir not in PROTECTED_APP_DIRS:
            print(json.dumps({"decision": "allow"}))
            return

        state_path = os.path.join(
            repo_root, "docs", "project", "00-governance", "PROJECT_STATE.md"
        )
        if not os.path.isfile(state_path):
            print(json.dumps({"decision": "allow"}))
            return

        with open(state_path, "r", encoding="utf-8") as f:
            state_text = f.read()

        g0 = is_gate_approved(state_text, "Gate 0")
        g1 = is_gate_approved(state_text, "Gate 1")
        g2 = is_gate_approved(state_text, "Gate 2")

        if g0 and g1 and g2:
            print(json.dumps({"decision": "allow"}))
            return

        missing = [
            name
            for name, ok in [("Gate 0", g0), ("Gate 1", g1), ("Gate 2", g2)]
            if not ok
        ]
        reason = (
            f"[M-AEOS Gate Guard] Ditolak menulis ke '{rel_target}'. "
            f"Gerbang berikut belum berstatus DISETUJUI/FROZEN di PROJECT_STATE.md: {', '.join(missing)}. "
            "Tuntaskan Analisis Sistem/Birokrasi (D-01), Arsitektur Ringan (D-02), dan Desain UI/UX Anti-Slop (D-03) terlebih dahulu!"
        )
        print(json.dumps({"decision": "deny", "reason": reason}))
    except Exception:
        print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()

