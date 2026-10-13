#!/usr/bin/env python3
"""
Launcher: opens a terminal and the on-screen arrow keys.
Requires: xdotool python3-tk and a terminal emulator (gnome-terminal, xterm, or xfce4-terminal)
"""

import subprocess
import sys
import os
import shutil

def find_terminal():
    for term in ["gnome-terminal", "xfce4-terminal", "xterm", "konsole", "terminator"]:
        if shutil.which(term):
            return term
    return None

def main():
    term = find_terminal()
    if not term:
        print("No terminal emulator found. Install one (e.g. gnome-terminal or xterm).")
        sys.exit(1)

    # Launch terminal
    if term == "gnome-terminal":
        subprocess.Popen([term, "--working-directory", os.getcwd()])
    elif term == "xfce4-terminal":
        subprocess.Popen([term, "--working-directory", os.getcwd()])
    else:
        subprocess.Popen([term])

    # Launch arrows (same directory)
    arrows = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arrows.py")
    if not os.path.exists(arrows):
        print("arrows.py not found in the same directory.")
        sys.exit(1)

    subprocess.Popen([sys.executable, arrows])

if __name__ == "__main__":
    main()
