#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NMAP Multi-Scan Terminal Tool
  Termux : pkg install nmap  then  python nmap_tool.py
  Linux  : sudo apt install nmap  then  python nmap_tool.py
  Usage  : python nmap_tool.py
  Usage  : python nmap_tool.py 192.168.1.1
  LEGAL  : Only scan systems you own or have permission to test.
"""

import subprocess
import sys
import os
import re
import time
import socket
import ipaddress
import shutil
import datetime
import platform

# ──────────────────────────────────────
# ANSI COLORS
# ──────────────────────────────────────
R  = '\033[91m'
DR = '\033[31m'
GR = '\033[92m'
DG = '\033[32m'
YL = '\033[93m'
CY = '\033[96m'
WH = '\033[97m'
BL = '\033[94m'
OR = '\033[38;5;208m'
DM = '\033[2m'
BD = '\033[1m'
GY = '\033[38;5;238m'
LG = '\033[38;5;245m'
PR = '\033[35m'
RS = '\033[0m'

def cc(text, *codes):
    prefix = ""
    for c in codes:
        prefix = prefix + c
    return prefix + str(text) + RS

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def div(ch="-", color=DR, width=65):
    print(color + BD + (ch * width) + RS)

# ──────────────────────────────────────
# CUSTOM RED ASCII BANNER
# ──────────────────────────────────────
def print_banner():

    banner = r"""

                                   ......::-----======---:......
                               ...:--===---:::::::::::::---====-:...
                            .:-==--::.........................::--===:..
                        ..-===--:..................................:=-==-:.
                    ...-===:.-.::.......::---========----::........::.::-===:...
                  ..:=---.::.::.-:::-===++====+++++=++====++===-::::..:..:::=-=:..
                .:=---..:.::.::--===++======++++++=---:--======+===-:::..:.::.-=-=:.
             ..==--:.::.::.:=--=---===--====++++++=+=::::-==---==----==--.::..::.---=..
          ..:=-=:.::.::.:-=--::::--=-----======+****+=======----==-::::--==:.::.::.:=-=:..
        .:==--:.-:.:::-=--:::::::--------====+####*###*====--------::::::::-=-:::.::.:----..
      .:=--:.::..:::-=-::::::::::--::----==-*##******##*-==----::--:::::::::::----:..::.---=:.
    .:---:.::..::---:::::::::::::--::::----=*****--***#*=-----:::--::::::::::::::----..::.:=--:.
  ..-=-:.::::----::.............:--::::-----*#*+#++***#*=----:::::-:..............:----:.::::-=-..
  :=--:::::-=---.................:::::::----=****++****+----::::::-:...............:---=-:::::-==:.
  :---:-==----=-.................:-::::::-----+*******=----::::::::................:==-:--+=-::--:.
  :-----+====-=--::..............::-::::::-------==-------:::::::-:.............:::--=======--==-:.
  ..:-=+====---:=-====-::.........:--::::::--------------::::::--:........:::-====--:---==+=+=-:.
     .....::-=+=+==----=====::.....::--:::::::--------:::::::--::.....:-=====----==+++=-::....
             .....-=+++=:---=+==-::.::----:::::-::-:-:::::----::.::=====----=+++=-.....
                    ..-==+==-:---=+=--::------::-::-:-------::-==+=--=--==+==-..
                       ..:-+++=-=-----========-------=========-------=+++-:.
                          ...-=++=----------===========----------==++=-...
                               .:=+++==----------------------==+++=:.
                                  .:-=+++++++=========+++++++==-..
                                      ...::::---------:::::...

                ...::::. ..:::::...::::.   .:::::...::::::::.   ...::::::::...
               .+#####%#-+#######%####%*. .+%##############%+. .=##########%#*-.
               :%*-----#%%+------=----=#*.=#*----=#=-------*#- :%*-----------=##:
               .+##*----*%%##--=#%*----+#*##----+%####+----=##:.+##*--+####+---##.
                .:#*-====+#%%=-=%%#=-==-*%#====-+#-:#*=-+*=-=#*..:#*--*%+=*##--*#-.
                .:#*==**==+#%==+%%#==+*==*+==*==+#=*#+=+%%*==*#+.:*#==*###*+==+##.
                .:#*==*%#==+#+=+%%#+=+#+====*#+=+###+=========*%-:##=========*##.
                .:##==*%%#+====+%%#+=+%#+==*%#+=*%%*==++++++==+##=##==*%%%%%#*-.
                :##*==*##%#+===+%%#+=+#######*+=+#*+=+#%%%%#*==+#%#*==*#####:
               .*#+=====+#%%+==+%*=====+#%%+===========*%%*+=====+========+##.
                .*#%%%%%%*-+%%%%%%%%%%%%#=*#%%%%%%%%%%%##+#%%%%%%%%%%%%%%%##.
                 ......... .............. ............... ..................
"""

    print()

    for line in banner.splitlines():

        colored = ""

        for ch in line:

            if ch in "#%*+=-":
                colored += R + BD + ch + RS

            elif ch in ".:":
                colored += DR + DM + ch + RS

            else:
                colored += ch

        print(colored)

    print()

    width = 80

    l1 = "[ NETWORK MAPPER  .  MULTI-SCAN TOOL ]"
    l2 = "[ Pure Python  .  nmap backend ]"
    l3 = "!! ONLY SCAN SYSTEMS YOU OWN OR HAVE PERMISSION !!"

    print(cc(l1.center(width), R, BD))
    print(cc(l2.center(width), DR))
    print()
    print(cc(l3.center(width), YL, BD))
    print()

# ──────────────────────────────────────
# SYSTEM INFO
# ──────────────────────────────────────
def get_nmap_ver():
    try:
        r = subprocess.run(
            ["nmap", "--version"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        m = re.search(r"Nmap version ([\d.]+)", r.stdout)
        if m:
            return m.group(1)
        return "found"
    except FileNotFoundError:
        return cc("NOT INSTALLED", R, BD)
    except Exception:
        return "unknown"

def print_sysinfo():
    now  = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    pyv  = platform.python_version()
    oss  = platform.system() + " " + platform.release()
    nmv  = get_nmap_ver()
    div("-", DR, 65)
    info = (
        cc("  OS", GY) + cc(" " + oss, LG) +
        cc("  |  PY", GY) + cc(" " + pyv, LG) +
        cc("  |  NMAP", GY) + cc(" " + nmv, LG) +
        cc("  |  ", GY) + cc(now, LG)
    )
    print(info)
    div("-", DR, 65)
    print()

def check_nmap():
    if shutil.which("nmap") is None:
        print()
        print(cc("  [X] nmap is not installed.", R, BD))
        print(cc("      Termux : pkg install nmap", LG))
        print(cc("      Linux  : sudo apt install nmap", LG))
        print(cc("      Mac    : brew install nmap", LG))
        print()
        sys.exit(1)

# ──────────────────────────────────────
# SCAN LIST
# ──────────────────────────────────────
SCANS = [
    {
        "id":    "01",
        "name":  "Host Discovery",
        "desc":  "Ping scan - is the host alive?",
        "args":  ["-sn", "-v"],
        "color": GR,
        "icon":  "[*]",
        "root":  False,
    },
    {
        "id":    "02",
        "name":  "Fast Scan",
        "desc":  "Top 100 ports, quick results",
        "args":  ["-F", "-v", "--open"],
        "color": CY,
        "icon":  "[F]",
        "root":  False,
    },
    {
        "id":    "03",
        "name":  "Service and Version",
        "desc":  "Detect software on open ports",
        "args":  ["-sV", "--version-intensity", "7", "-v"],
        "color": YL,
        "icon":  "[V]",
        "root":  False,
    },
    {
        "id":    "04",
        "name":  "Default NSE Scripts",
        "desc":  "Run nmap built-in safe scripts",
        "args":  ["-sC", "-v"],
        "color": CY,
        "icon":  "[S]",
        "root":  False,
    },
    {
        "id":    "05",
        "name":  "OS Fingerprinting",
        "desc":  "Guess the operating system  [needs root]",
        "args":  ["-O", "--osscan-guess", "-v"],
        "color": OR,
        "icon":  "[O]",
        "root":  True,
    },
    {
        "id":    "06",
        "name":  "Aggressive Scan",
        "desc":  "OS + Version + Scripts + Traceroute  [root]",
        "args":  ["-A", "-v"],
        "color": R,
        "icon":  "[A]",
        "root":  True,
    },
    {
        "id":    "07",
        "name":  "Full TCP Port Scan",
        "desc":  "All 65535 TCP ports  (slow)",
        "args":  ["-p-", "-v", "--open", "-T4"],
        "color": PR,
        "icon":  "[T]",
        "root":  False,
    },
    {
        "id":    "08",
        "name":  "UDP Top-100 Scan",
        "desc":  "Top 100 UDP ports  [needs root]",
        "args":  ["-sU", "--top-ports", "100", "-v"],
        "color": BL,
        "icon":  "[U]",
        "root":  True,
    },
    {
        "id":    "09",
        "name":  "Firewall ACK Scan",
        "desc":  "Detect firewall filter rules  [needs root]",
        "args":  ["-sA", "-v", "-p", "21,22,23,25,53,80,443,445,3389"],
        "color": YL,
        "icon":  "[W]",
        "root":  True,
    },
    {
        "id":    "10",
        "name":  "Vulnerability Scripts",
        "desc":  "NSE vuln detection (own systems only)",
        "args":  ["--script", "vuln", "-v"],
        "color": R,
        "icon":  "[!]",
        "root":  False,
    },
    {
        "id":    "11",
        "name":  "HTTP Enumeration",
        "desc":  "HTTP headers, methods, title",
        "args":  [
            "-p", "80,443,8080,8443,8000,8888",
            "--script", "http-title,http-headers,http-methods",
            "-v",
        ],
        "color": CY,
        "icon":  "[H]",
        "root":  False,
    },
    {
        "id":    "12",
        "name":  "Traceroute",
        "desc":  "Map network path hop by hop",
        "args":  ["--traceroute", "-sn", "-v"],
        "color": DG,
        "icon":  "[R]",
        "root":  False,
    },
    {
        "id":    "13",
        "name":  "SMB Enumeration",
        "desc":  "Windows shares and SMB info",
        "args":  [
            "-p", "445,139",
            "--script", "smb-security-mode,smb-os-discovery,smb-enum-shares",
            "-v",
        ],
        "color": OR,
        "icon":  "[B]",
        "root":  False,
    },
    {
        "id":    "14",
        "name":  "DNS Enumeration",
        "desc":  "DNS service info and zone details",
        "args":  [
            "-p", "53",
            "--script", "dns-nsid,dns-recursion",
            "-v",
        ],
        "color": LG,
        "icon":  "[D]",
        "root":  False,
    },
    # ── FIX 1: scan 15 was missing closing }, ──
    {
        "id":    "15",
        "name":  "SSL/TLS Inspection",
        "desc":  "Cipher suites and certificate info",
        "args":  [
            "-p", "443,8443,465,993,995",
            "--script", "ssl-enum-ciphers,ssl-cert",
            "-v",
        ],
        "color": GR,
        "icon":  "[L]",
        "root":  False,
    },
    # ── FIX 2: removed stray extra }, between 22 and 23 ──
    {
        "id":    "16",
        "name":  "SYN Stealth Scan",
        "desc":  "Half-open scan, no full TCP handshake [needs root]",
        "args":  ["-sS", "-v", "--open"],
        "color": PR,
        "icon":  "[Y]",
        "root":  True,
    },
    {
        "id":    "17",
        "name":  "TCP Connect Scan",
        "desc":  "Full connect() when SYN scan unavailable",
        "args":  ["-sT", "-v", "--open"],
        "color": CY,
        "icon":  "[C]",
        "root":  False,
    },
    {
        "id":    "18",
        "name":  "Xmas Stealth Scan",
        "desc":  "FIN/PSH/URG flags set [needs root]",
        "args":  ["-sX", "-v", "--open"],
        "color": OR,
        "icon":  "[X]",
        "root":  True,
    },
    {
        "id":    "19",
        "name":  "FIN Stealth Scan",
        "desc":  "FIN flag only, bypasses some firewalls [root]",
        "args":  ["-sF", "-v", "--open"],
        "color": YL,
        "icon":  "[F]",
        "root":  True,
    },
    {
        "id":    "20",
        "name":  "NULL Stealth Scan",
        "desc":  "No TCP flags set [needs root]",
        "args":  ["-sN", "-v", "--open"],
        "color": LG,
        "icon":  "[0]",
        "root":  True,
    },
    {
        "id":    "21",
        "name":  "Decoy Scan",
        "desc":  "Hide scan among fake decoy IPs [needs root]",
        "args":  ["-sS", "-D", "RND:10", "-v"],
        "color": R,
        "icon":  "[D]",
        "root":  True,
    },
    {
        "id":    "22",
        "name":  "Fragmented Packets",
        "desc":  "Split packets to evade IDS/IPS [needs root]",
        "args":  ["-sS", "-f", "-v"],
        "color": DR,
        "icon":  "[G]",
        "root":  True,
    },
    {
        "id":    "23",
        "name":  "SSH Audit",
        "desc":  "SSH algorithms and security info",
        "args":  ["-p", "22", "--script", "ssh-auth-methods,ssh-hostkey,ssh2-enum-algos", "-v"],
        "color": CY,
        "icon":  "[S]",
        "root":  False,
    },
    {
        "id":    "24",
        "name":  "FTP Anonymous Check",
        "desc":  "Test for anonymous FTP login",
        "args":  ["-p", "21", "--script", "ftp-anon,ftp-syst,ftp-vsftpd-backdoor", "-v"],
        "color": OR,
        "icon":  "[F]",
        "root":  False,
    },
    {
        "id":    "25",
        "name":  "SMTP Enumeration",
        "desc":  "Mail server users and commands",
        "args":  ["-p", "25,465,587", "--script", "smtp-commands,smtp-enum-users,smtp-open-relay", "-v"],
        "color": BL,
        "icon":  "[M]",
        "root":  False,
    },
    {
        "id":    "26",
        "name":  "Database Scan",
        "desc":  "MySQL, PostgreSQL, MSSQL, Oracle",
        "args":  ["-p", "3306,5432,1433,1521", "--script", "mysql-info,pgsql-info,ms-sql-info", "-v"],
        "color": PR,
        "icon":  "[B]",
        "root":  False,
    },
    {
        "id":    "27",
        "name":  "NoSQL Scan",
        "desc":  "MongoDB and Redis info",
        "args":  ["-p", "27017,6379", "--script", "mongodb-info,redis-info", "-v"],
        "color": GR,
        "icon":  "[N]",
        "root":  False,
    },
    {
        "id":    "28",
        "name":  "SNMP Enumeration",
        "desc":  "SNMP devices and MIB data",
        "args":  ["-p", "161,162", "-sU", "--script", "snmp-info,snmp-processes,snmp-sysdescr", "-v"],
        "color": YL,
        "icon":  "[N]",
        "root":  True,
    },
    {
        "id":    "29",
        "name":  "Heartbleed Check",
        "desc":  "Test for OpenSSL Heartbleed CVE-2014-0160",
        "args":  ["-p", "443", "--script", "ssl-heartbleed", "-v"],
        "color": R,
        "icon":  "[!]",
        "root":  False,
    },
    {
        "id":    "30",
        "name":  "Banner Grabbing",
        "desc":  "Service banners on common ports",
        "args":  ["-sV", "--script", "banner", "-p", "21,22,23,25,80,110,143,443,445,993,995,3306,8080", "-v"],
        "color": LG,
        "icon":  "[B]",
        "root":  False,
    },
    {
        "id":    "31",
        "name":  "IP Geolocation",
        "desc":  "Geo location of target",
        "args":  ["--script", "ip-geolocation-geoplugin,ip-geolocation-maxmind", "-sn", "-v"],
        "color": CY,
        "icon":  "[G]",
        "root":  False,
    },
    {
        "id":    "32",
        "name":  "WHOIS Lookup",
        "desc":  "WHOIS registration data",
        "args":  ["--script", "whois-ip,whois-domain", "-sn", "-v"],
        "color": DG,
        "icon":  "[W]",
        "root":  False,
    },
    {
        "id":    "33",
        "name":  "Heartbleed + SSL",
        "desc":  "SSL vulnerabilities including Heartbleed, POODLE",
        "args":  ["-p", "443,8443,465,993,995", "--script", "ssl-heartbleed,ssl-poodle,ssl-dh-params", "-v"],
        "color": R,
        "icon":  "[!]",
        "root":  False,
    },
    {
        "id":    "34",
        "name":  "Malware Backdoor Check",
        "desc":  "Check for known backdoors",
        "args":  ["--script", "auth-spoof,backdoor-enum,imap-brute", "-v"],
        "color": R,
        "icon":  "[X]",
        "root":  False,
    },
    {
        "id":    "35",
        "name":  "Slowloris DoS Check",
        "desc":  "Test if web server vulnerable to Slowloris",
        "args":  ["-p", "80,443,8080", "--script", "http-slowloris-check", "-v"],
        "color": OR,
        "icon":  "[D]",
        "root":  False,
    },
    {
        "id":    "36",
        "name":  "All TCP Scripts",
        "desc":  "Run all relevant scripts against open ports",
        "args":  ["-sV", "--script", "discovery,vuln,auth,default", "-v"],
        "color": PR,
        "icon":  "[A]",
        "root":  False,
    },
]
# ── FIX 3: SCANS list closed with ] above ──

# ──────────────────────────────────────
# MENU + INPUT
# ──────────────────────────────────────
def print_menu():
    print(cc("  AVAILABLE SCANS", R, BD))
    div("-", DR, 65)
    for s in SCANS:
        root_tag = ""
        if s["root"]:
            root_tag = cc(" [root]", YL)
        sid  = cc("  [" + s["id"] + "]", DR, BD)
        icon = cc(s["icon"] + " ", s["color"])
        name = cc(s["name"].ljust(24), WH, BD)
        desc = cc(s["desc"], LG)
        print(sid + "  " + icon + name + "  " + desc + root_tag)
    div("-", DR, 65)
    print(cc("  [A]", R, BD) + "  " + cc("[*] ", R) + cc("RUN ALL SCANS".ljust(24), R, BD) + "  " + cc("Full automated deep scan", LG))
    print(cc("  [Q]", GY) + "  " + cc("[Q] ", GY) + cc("QUIT", GY))
    div("-", DR, 65)

def get_choice():
    valid = set()
    for s in SCANS:
        valid.add(s["id"])

    prompt = cc("\n  >> ", R, BD) + cc("Scan number(s) [e.g. 01 or 01,03,07 or A]: ", LG)

    while True:
        try:
            raw = input(prompt).strip().upper()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)

        if not raw:
            continue

        if raw == "Q":
            print(cc("\n  Goodbye.\n", DR))
            sys.exit(0)

        if raw == "A":
            return list(SCANS)

        parts  = re.split(r"[,\s]+", raw)
        ids    = [p.zfill(2) for p in parts if p]
        chosen = [s for s in SCANS if s["id"] in ids]
        bad    = [i for i in ids if i not in valid]

        if bad:
            print(cc("  [X] Unknown id(s): " + ", ".join(bad), R))
            continue

        if chosen:
            return chosen

# ──────────────────────────────────────
# TARGET
# ──────────────────────────────────────
def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def resolve_host(host):
    try:
        return socket.gethostbyname(host)
    except Exception:
        return None

def get_target(arg=None):
    if arg:
        target = arg.strip()
    else:
        print(cc("  TARGET", R, BD))
        div("-", DR, 65)
        print(cc("  Examples: 192.168.1.1  |  10.0.0.0/24  |  scanme.nmap.org", GY))
        prompt = cc("  >> ", R, BD) + cc("Enter target IP / hostname: ", LG)
        try:
            target = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)

    if not target:
        print(cc("  [X] No target entered.", R))
        sys.exit(1)

    resolved = None
    if not validate_ip(target) and "/" not in target:
        sys.stdout.write(cc("  [*] Resolving hostname... ", DR))
        sys.stdout.flush()
        resolved = resolve_host(target)
        if not resolved:
            print(cc("FAILED", R))
            print(cc("  [X] Cannot resolve: " + target, R))
            sys.exit(1)
        print(cc("OK -> " + resolved, GR))

    print()
    return target, resolved

# ──────────────────────────────────────
# COLORIZE NMAP OUTPUT
# ── FIX 4: completed the cut-off function ──
# ──────────────────────────────────────
def colorize(line):
    lo = line.lower()

    if re.search(r'\d+/tcp\s+open', lo):
        return GR + BD + line + RS
    if re.search(r'\d+/udp\s+open', lo):
        return CY + BD + line + RS
    if "open|filtered" in lo:
        return YL + line + RS
    if re.search(r'\d+/(tcp|udp)\s+closed', lo):
        return GY + line + RS
    if "filtered" in lo and "/" in line:
        return LG + line + RS
    if line.startswith("Nmap scan report"):
        return R + BD + "+- " + line + RS
    if line.startswith("Host is up"):
        return GR + line + RS
    if line.startswith("Host is down") 