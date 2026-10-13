# Keys

On-screen arrow keys for controlling terminals on the Grok Bot VM (or any Linux desktop).

## Setup

```bash
sudo apt update && sudo apt install -y xdotool python3-tk
```

Optional (for the launcher):
```bash
sudo apt install -y gnome-terminal
```

## Run arrows only

```bash
python3 arrows.py
```

A small always-on-top window with ↑ ↓ ← → buttons appears. Click them to send real arrow keys.

## Run launcher (opens terminal + arrows)

```bash
python3 launch.py
```

Opens a terminal window and the arrow keys next to it.
