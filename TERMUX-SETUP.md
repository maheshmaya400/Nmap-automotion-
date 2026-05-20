# 📱 Termux Setup Guide

Complete step-by-step setup for Android using Termux.

---

## Step 1 — Install Termux

Download **Termux from F-Droid** (recommended):
👉 https://f-droid.org/packages/com.termux/

> ⚠️ Do NOT use the Play Store version — it's outdated and broken.

---

## Step 2 — Setup Termux

Open Termux and run:

```bash
# Update packages
pkg update && pkg upgrade -y

# Install required packages
pkg install python nmap git -y

# Allow storage access (optional, to save scan results)
termux-setup-storage
```

---

## Step 3 — Clone & Run

```bash
# Clone the tool
git clone https://github.com/YOUR_USERNAME/nmap-multi-scan.git
cd nmap-multi-scan

# Run it
python nmap_tool.py

# Run with a target directly
python nmap_tool.py 192.168.1.1
```

---

## Step 4 — Scans That Need Root

Some scans (SYN, OS fingerprint, UDP, etc.) need root because Android
blocks raw socket access.

**With Magisk/KernelSU rooted device:**
```bash
# Install tsu (Termux sudo)
pkg install tsu -y

# Run as root
sudo python nmap_tool.py
```

**Without root** — just skip those scans. 20+ scans work without root.

---

## Common Termux Errors

| Error | Fix |
|-------|-----|
| `nmap: not found` | `pkg install nmap` |
| `python: not found` | `pkg install python` |
| `Operation not permitted` | Scan needs root — use `sudo` or pick a non-root scan |
| `Could not resolve host` | Check WiFi connection |
| Permission denied on `/proc` | Normal on Android — nmap still works for most scans |

---

## Tips for Termux

- Use a **Bluetooth keyboard** for easier typing
- Long-press the screen to **copy** nmap output
- Run `termux-setup-storage` to save results to your Downloads folder
- Use `tmux` (`pkg install tmux`) to keep scans running in background

---

> ⚠️ **Only scan networks and devices you own or have permission to test.**
