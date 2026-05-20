# 🚀 How to Push to GitHub from Termux

Follow these exact steps. Copy-paste each command one by one.

---

## Step 1 — Install Git in Termux

```bash
pkg install git -y
```

---

## Step 2 — Set Your Git Identity

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

## Step 3 — Create the Repo on GitHub

1. Open https://github.com in your browser
2. Click **"+"** → **"New repository"**
3. Name it: `nmap-multi-scan`
4. Set it to **Public**
5. ❌ Do NOT check "Add README" (we already have one)
6. Click **"Create repository"**
7. **Copy the repo URL** — looks like:
   `https://github.com/YOUR_USERNAME/nmap-multi-scan.git`

---

## Step 4 — Create a GitHub Token (Password)

GitHub no longer accepts your password via terminal.
You need a **Personal Access Token**:

1. GitHub → Click your avatar → **Settings**
2. Scroll down → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)**
4. Click **Generate new token (classic)**
5. Give it a name: `termux`
6. Expiration: `90 days` or `No expiration`
7. Check the box: ✅ **repo**
8. Click **Generate token**
9. **COPY THE TOKEN NOW** — you won't see it again!

---

## Step 5 — Initialize and Push

Run these commands in Termux (in your project folder):

```bash
# Go to your home folder
cd ~

# Create the project folder
mkdir nmap-multi-scan
cd nmap-multi-scan

# Copy your script here
cp ~/nmap.py nmap_tool.py

# Download the README and other files from the release
# OR copy the files you downloaded into this folder

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "🚀 Initial release: NMAP Multi-Scan Tool v1.0"

# Set main branch
git branch -M main

# Connect to GitHub (replace YOUR_USERNAME with yours)
git remote add origin https://github.com/YOUR_USERNAME/nmap-multi-scan.git

# Push!
git push -u origin main
```

When it asks for **username**: type your GitHub username
When it asks for **password**: paste your **TOKEN** (not your GitHub password)

---

## Step 6 — Make It Look Good on GitHub

After pushing, on your repo page:

1. Click the ⚙️ gear icon next to "About"
2. Add description: `36+ nmap scan profiles | Termux & Linux | Color terminal UI`
3. Add topics (tags): `nmap`, `termux`, `android`, `security`, `python`, `hacking`, `network-scanner`, `ethical-hacking`
4. Check ✅ "Releases", "Packages"

---

## Updating Later

Every time you change the code:

```bash
cd ~/nmap-multi-scan
git add .
git commit -m "Fix: describe what you changed"
git push
```

---

## ⭐ Get More Stars

Share your repo link on:
- Reddit: r/termux, r/netsec, r/Python, r/HowToHack
- Twitter/X with hashtags: #termux #nmap #cybersecurity #python
- YouTube: make a short demo video

---

> Good luck! 🔴
