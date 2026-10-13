# Keys

On-screen arrow keys for controlling terminals on the Grok Bot VM (or any Linux desktop).

## Setup

```bash
sudo apt update && sudo apt install -y xdotool python3-tk
```

## Run

```bash
python3 arrows.py
```

A small always-on-top window with ↑ ↓ ← → buttons appears. Click them to send real arrow keys.
