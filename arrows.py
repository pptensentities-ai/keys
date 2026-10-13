#!/usr/bin/env python3
"""
On-screen arrow keys for terminal control.
Requires: xdotool and python3-tk
Install: sudo apt install -y xdotool python3-tk
Run: python3 arrows.py
"""

import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Arrows")
root.geometry("260x90")
root.attributes("-topmost", True)

def send(key):
    subprocess.run(["xdotool", "key", key], check=False)

for text, key in [("↑", "Up"), ("↓", "Down"), ("←", "Left"), ("→", "Right")]:
    tk.Button(
        root,
        text=text,
        command=lambda k=key: send(k),
        font=("Arial", 22),
        width=4,
        height=2
    ).pack(side="left", padx=4, pady=4)

root.mainloop()
