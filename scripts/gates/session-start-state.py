#!/usr/bin/env python3
"""
M-AEOS SessionStart Hook:
Membaca status fase terkini dari docs/project/00-governance/PROJECT_STATE.md
dan menyuntikkan pengingat ringkas ke konteks percakapan saat sesi baru dimulai.
"""

import json
import os
import re
import sys


def main() -> None:
    try:
        _ = sys.stdin.read()
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        state_file = os.path.join(
            repo_root, "docs", "project", "00-governance", "PROJECT_STATE.md"
        )
        if not os.path.isfile(state_file):
            print(json.dumps({}))
            return

        with open(state_file, "r", encoding="utf-8") as f:
            content = f.read()

        phase_match = re.search(r"\*\*Fase Aktif Saat Ini\*\*:\s*`([^`]+)`", content)
        code_lock_match = re.search(
            r"\*\*Izin Penulisan Kode Aplikasi.*?\*\*:\s*`([^`]+)`", content
        )
        active_phase = phase_match.group(1) if phase_match else "TIDAK DIKETAHUI"
        code_lock = code_lock_match.group(1) if code_lock_match else "TERKUNCI"

        msg = (
            f"[M-AEOS Kernel Aktif] Fase Projek: {active_phase} | "
            f"Status Izin Kode Aplikasi: {code_lock}. "
            "Patuhi isolasi peran subagent dan gerbang kualitas di AGENTS.md."
        )
        print(
            json.dumps(
                {
                    "injectSteps": [
                        {
                            "systemMessage": {
                                "systemMessage": msg,
                            }
                        }
                    ]
                }
            )
        )
    except Exception:
        print(json.dumps({}))


if __name__ == "__main__":
    main()
