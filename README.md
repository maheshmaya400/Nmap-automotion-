# 🔴 NMAP Multi-Scan Terminal Tool

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-red?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Termux%20%7C%20Mac-red?style=for-the-badge&logo=linux&logoColor=white"/>
  <img src="https://img.shields.io/badge/Nmap-Backend-red?style=for-the-badge&logo=nmap&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Scans-36%2B-red?style=for-the-badge"/>
</p>

<p align="center">
  A powerful, colorful, menu-driven nmap wrapper written in pure Python.<br/>
  Runs perfectly on <strong>Termux (Android)</strong>, Linux, and macOS.
</p>

--- 
## 📸 Screenshot

<p align="center">
  <img src="assets/banner.png" width="700"/>
</p>

## ⚡ Features

- 🎯 **36 pre-built scan profiles** — from quick pings to full vuln detection
- 🤖 **Run ALL scans** with one keypress (`A`)
- 🎨 **Color-coded live output** — open ports in green, filtered in yellow, etc.
- 📱 **Termux-friendly** — works on Android without root for most scans
- 🔍 **Hostname resolution** — enter a domain, it resolves automatically
- 🛡️ **Root/non-root** labels — knows which scans need elevated privileges
- ⚡ **Multi-scan mode** — run `01,05,10` in one go

---

## 📋 Scan List

| ID | Scan Name | Needs Root |
|----|-----------|:----------:|
| 01 | Host Discovery | ❌ |
| 02 | Fast Scan (Top 100 ports) | ❌ |
| 03 | Service & Version Detection | ❌ |
| 04 | Default NSE Scripts | ❌ |
| 05 | OS Fingerprinting | ✅ |
| 06 | Aggressive Scan | ✅ |
| 07 | Full TCP Port Scan (65535) | ❌ |
| 08 | UDP Top-100 Scan | ✅ |
| 09 | Firewall ACK Scan | ✅ |
| 10 | Vulnerability Scripts | ❌ |
| 11 | HTTP Enumeration | ❌ |
| 12 | Traceroute | ❌ |
| 13 | SMB Enumeration | ❌ |
| 14 | DNS Enumeration | ❌ |
| 15 | SSL/TLS Inspection | ❌ |
| 16 | SYN Stealth Scan | ✅ |
| 17 | TCP Connect Scan | ❌ |
| 18 | Xmas Stealth Scan | ✅ |
| 19 | FIN Stealth Scan | ✅ |
| 20 | NULL Stealth Scan | ✅ |
| 21 | Decoy Scan | ✅ |
| 22 | Fragmented Packets | ✅ |
| 23 | SSH Audit | ❌ |
| 24 | FTP Anonymous Check | ❌ |
| 25 | SMTP Enumeration | ❌ |
| 26 | Database Scan (MySQL/PG/MSSQL) | ❌ |
| 27 | NoSQL Scan (MongoDB/Redis) | ❌ |
| 28 | SNMP Enumeration | ✅ |
| 29 | Heartbleed Check | ❌ |
| 30 | Banner Grabbing | ❌ |
| 31 | IP Geolocation | ❌ |
| 32 | WHOIS Lookup | ❌ |
| 33 | Heartbleed + SSL Vulns | ❌ |
| 34 | Malware Backdoor Check | ❌ |
| 35 | Slowloris DoS Check | ❌ |
| 36 | All TCP Scripts | ❌ |

---

## 🚀 Installation

### 📱 Termux (Android)

```bash
# Install dependencies
pkg update && pkg upgrade -y
pkg install python nmap git -y

# Clone the repo
git clone https://github.com/YOUR_USERNAME/nmap-multi-scan.git
cd nmap-multi-scan

# Run
python nmap_tool.py
```

### 🐧 Linux (Debian/Ubuntu/Kali)

```bash
# Install dependencies
sudo apt update
sudo apt install python3 nmap git -y

# Clone the repo
git clone https://github.com/YOUR_USERNAME/nmap-multi-scan.git
cd nmap-multi-scan

# Run
python3 nmap_tool.py

# For root scans
sudo python3 nmap_tool.py
```

### 🍎 macOS

```bash
# Install dependencies
brew install python nmap

# Clone the repo
git clone https://github.com/YOUR_USERNAME/nmap-multi-scan.git
cd nmap-multi-scan

# Run
python3 nmap_tool.py
```

---

## 🎮 Usage

```bash
# Interactive menu
python nmap_tool.py

# Pass target directly (skip the prompt)
python nmap_tool.py 192.168.1.1
python nmap_tool.py 10.0.0.0/24
python nmap_tool.py scanme.nmap.org
```

### Menu Controls

```
[01]–[36]  — Pick a specific scan
01,05,10   — Run multiple scans in one go
A          — Run ALL 36 scans automatically
Q          — Quit
```

---

## 📸 Preview

```
+- Nmap scan report for 192.168.1.1
22/tcp   open  ssh     OpenSSH 8.9
80/tcp   open  http    Apache httpd 2.4.52
443/tcp  open  https   nginx 1.18.0
3306/tcp open  mysql   MySQL 8.0.31
```

---

## ⚠️ Legal Disclaimer

> **This tool is for educational and authorized security testing only.**
>
> Only scan systems you **own** or have **explicit written permission** to test.
> Unauthorized scanning is **illegal** in most countries and violates the
> Computer Fraud and Abuse Act (CFAA) and similar laws worldwide.
>
> The author is **not responsible** for any misuse or damage caused by this tool.

---



---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">Made with ❤️ for the security community · Use responsibly</p>
