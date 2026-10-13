#!/usr/bin/env python3
"""
Launches a terminal and runs a max Project Eyes On scan,
saving output to /workspace/Project-Eyes-On/scans
"""

import os
import subprocess
import sys
import shutil

OUTPUT_DIR = "/workspace/Project-Eyes-On/scans"
SCAN_CMD = [
    "eyeson",
    "--scan", "100",
    "--max-dorks", "0",
    "--mode", "SNAPSHOT",
    "-o", OUTPUT_DIR,
    "--format", "json"
]

def find_terminal():
    for term in ["gnome-terminal", "xfce4-terminal", "xterm", "konsole", "terminator"]:
        if shutil.which(term):
            return term
    return None

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

    term = find_terminal()
    if not term:
        print("No terminal found. Running scan in current process...")
        subprocess.run(SCAN_CMD)
        return

    # Build the command string for the terminal
    cmd_str = " ".join(SCAN_CMD)
    full_cmd = f"{cmd_str}; echo; echo 'Scan finished. Press Enter to close.'; read"

    if term == "gnome-terminal":
        subprocess.Popen([term, "--", "bash", "-c", full_cmd])
    elif term == "xfce4-terminal":
        subprocess.Popen([term, "-e", f"bash -c '{full_cmd}'"])
    else:
        subprocess.Popen([term, "-e", f"bash -c '{full_cmd}'"])

    print("Terminal launched with the scan.")

if __name__ == "__main__":
    main()
