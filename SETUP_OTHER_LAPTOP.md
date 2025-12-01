# 🚀 Setup Network Scanner on Your Other Laptop

**Clone and configure this project on another machine**

---

## 📥 Quick Setup

### 1. Clone the Repository

```bash
# Navigate to Projects folder
cd ~/Projects

# Clone from GitHub
git clone https://github.com/MSSecCSA/network-scanner.git
cd network-scanner
```

### 2. Install Dependencies

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install -y \
  nmap \
  sshpass \
  jq \
  python3 \
  python3-pip \
  git
```

#### macOS (with Homebrew)
```bash
brew install nmap jq sshpass python3
```

### 3. Create Data Directories

```bash
# Already in git, but ensure they exist
mkdir -p data/zeek data/reports data/scans
```

### 4. Configure Environment

```bash
# Copy the environment template
cp .env.example .env

# Edit with your Firewalla credentials
nano .env
```

**Update these values:**
```bash
FIREWALLA_IP=192.168.156.1
FIREWALLA_USER=pi
FIREWALLA_PASSWORD=PqSCNHefBV

NETWORK_SUBNET=192.168.156.0/24
NETWORK_GATEWAY=192.168.156.1

FIREWALLA_CSV_PATH=~/Downloads/Firewalla_Devices.csv
```

### 5. Test SSH Access to Firewalla

```bash
# Test connection
ssh pi@192.168.156.1

# If successful, exit
exit
```

### 6. Export Firewalla Device List

**On Firewalla App (Phone/Tablet):**
1. Open Firewalla app
2. Go to "Devices"
3. Tap menu (⋮) → Export
4. Share/Send to laptop
5. Save as `~/Downloads/Firewalla_Devices.csv`

**Or download via laptop browser:**
1. Log into Firewalla web portal (if available)
2. Export device list
3. Save to `~/Downloads/Firewalla_Devices.csv`

### 7. Test the Setup

```bash
cd ~/Projects/network-scanner

# Download Zeek logs
sshpass -p 'PqSCNHefBV' scp \
  pi@192.168.156.1:/log/blog/current/*.log data/zeek/

# Verify logs downloaded
ls -lh data/zeek/

# Generate HTML dashboard
python3 scripts/generate_html_report.py

# Should open automatically in browser!
```

---

## 🎯 Verify Everything Works

### ✅ Checklist

- [ ] Git repository cloned
- [ ] Dependencies installed (nmap, sshpass, jq, python3)
- [ ] `.env` file created and configured
- [ ] SSH access to Firewalla working
- [ ] Firewalla CSV exported and saved
- [ ] Zeek logs downloaded successfully
- [ ] HTML dashboard generated
- [ ] Dashboard opens in browser

### Test Commands

```bash
# Check dependencies
command -v nmap && echo "✅ nmap installed"
command -v sshpass && echo "✅ sshpass installed"
command -v jq && echo "✅ jq installed"
command -v python3 && echo "✅ python3 installed"

# Check SSH
ssh pi@192.168.156.1 'echo "✅ SSH works"'

# Check files
ls -lh ~/Downloads/Firewalla_Devices.csv && echo "✅ CSV exists"
ls -lh data/zeek/*.log && echo "✅ Zeek logs exist"

# Generate report
python3 scripts/generate_html_report.py && echo "✅ Dashboard generated"
```

---

## 🔄 Daily Usage on New Laptop

### Quick Commands

```bash
# Refresh data and generate dashboard
cd ~/Projects/network-scanner && \
sshpass -p 'PqSCNHefBV' scp pi@192.168.156.1:/log/blog/current/*.log data/zeek/ && \
python3 scripts/generate_html_report.py
```

### View Latest Dashboard

```bash
xdg-open ~/Projects/network-scanner/data/reports/network_dashboard_*.html
```

### Generate Text Report

```bash
cd ~/Projects/network-scanner
python3 scripts/network_correlation_analyzer.py
cat data/reports/network_report_*.txt | less
```

---

## 🌐 Network Requirements

### Must Be Connected To:
- **Same network** as Firewalla (192.168.156.0/24)
- **WiFi SSID**: darkstar (or morpheus for IoT)
- **IP Range**: 192.168.156.x

### Verify Network Connection

```bash
# Check your IP
ip addr show | grep "192.168.156"

# Ping Firewalla
ping -c 3 192.168.156.1

# Check route to Firewalla
ip route get 192.168.156.1
```

---

## 💡 Differences Between Laptops

### This Laptop (Original)
- Full development history
- All Zeek logs and reports (git ignored)
- Active monitoring

### Other Laptop (New)
- Clean clone from GitHub
- No historical logs (download fresh)
- Same functionality

**Both can:**
- Generate reports independently
- Monitor the same network
- Share updates via git

---

## 🔄 Keeping in Sync

### Pull Latest Changes

```bash
cd ~/Projects/network-scanner
git pull origin main
```

### Push Your Changes (Documentation, etc.)

```bash
cd ~/Projects/network-scanner

# Add changes
git add docs/

# Commit
git commit -m "Updated documentation"

# Push to GitHub
git push origin main
```

**⚠️ Never commit:**
- `.env` file (contains passwords)
- Zeek logs (`data/zeek/*.log`)
- Reports (`data/reports/*.html`, `*.txt`)
- Firewalla CSV files

These are automatically excluded by `.gitignore`!

---

## 🛠️ Troubleshooting

### Can't SSH to Firewalla

```bash
# Verify Firewalla IP
ping 192.168.156.1

# Check SSH is enabled in Firewalla app
# Settings → Advanced → SSH

# Test manual SSH
ssh pi@192.168.156.1
# Enter password: PqSCNHefBV
```

### sshpass Command Not Found

```bash
# Ubuntu/Debian
sudo apt install sshpass

# macOS
brew install hudochenkov/sshpass/sshpass
```

### Python Script Errors

```bash
# Check Python version (need 3.8+)
python3 --version

# Verify files exist
ls -la scripts/generate_html_report.py
ls -la ~/Downloads/Firewalla_Devices.csv
ls -la data/zeek/conn.log
```

### No Zeek Logs

```bash
# Download manually
sshpass -p 'PqSCNHefBV' scp \
  pi@192.168.156.1:/log/blog/current/*.log \
  ~/Projects/network-scanner/data/zeek/

# Verify
ls -lh ~/Projects/network-scanner/data/zeek/
```

### Dashboard Doesn't Open

```bash
# Open manually
firefox ~/Projects/network-scanner/data/reports/network_dashboard_*.html

# Or Chrome
google-chrome ~/Projects/network-scanner/data/reports/network_dashboard_*.html

# Or default browser
xdg-open ~/Projects/network-scanner/data/reports/network_dashboard_*.html
```

---

## 📱 Export Firewalla CSV (Detailed)

### Method 1: Firewalla Mobile App

1. Open Firewalla app on phone
2. Tap "Devices" at bottom
3. Tap menu icon (⋮ or •••) in top-right
4. Select "Export" or "Share"
5. Choose "Save to Files" or email to yourself
6. Transfer to laptop
7. Save as `~/Downloads/Firewalla_Devices.csv`

### Method 2: Firewalla Web Interface (if enabled)

1. Open browser on laptop
2. Navigate to Firewalla IP (if web UI enabled)
3. Log in
4. Go to Devices
5. Export CSV
6. Save as `~/Downloads/Firewalla_Devices.csv`

### Method 3: AirDrop (macOS/iOS)

1. Export from Firewalla app
2. AirDrop to laptop
3. Save to `~/Downloads/Firewalla_Devices.csv`

---

## �� One-Line Setup Script

**Copy and paste this entire block:**

```bash
# Full setup in one command
cd ~/Projects && \
git clone https://github.com/MSSecCSA/network-scanner.git && \
cd network-scanner && \
cp .env.example .env && \
echo "✅ Cloned! Now edit .env with your credentials:" && \
echo "   nano .env" && \
echo "" && \
echo "Then download Firewalla CSV to ~/Downloads/Firewalla_Devices.csv" && \
echo "Then run: python3 scripts/generate_html_report.py"
```

---

## 🎓 What's Included

After cloning, you'll have:

```
network-scanner/
├── scripts/
│   ├── generate_html_report.py          # HTML dashboard
│   └── network_correlation_analyzer.py  # Text reports
├── data/
│   ├── zeek/                            # (empty - download logs)
│   ├── reports/                         # (empty - generated here)
│   └── scans/                           # nmap results
├── docs/                                # Full documentation
│   ├── QUICK_START_GUIDE.md
│   ├── QUICK_REFERENCE_CARD.md
│   ├── HTML_DASHBOARD_GUIDE.md
│   └── ... (14 total guides)
├── .env.example                         # Template
├── .gitignore                           # Excludes sensitive data
├── LICENSE                              # MIT + disclaimer
└── README.md                            # Main documentation
```

---

## 📞 Quick Reference

### Generate Dashboard
```bash
python3 ~/Projects/network-scanner/scripts/generate_html_report.py
```

### Generate Text Report
```bash
python3 ~/Projects/network-scanner/scripts/network_correlation_analyzer.py
```

### Download Fresh Logs
```bash
sshpass -p 'PqSCNHefBV' scp \
  pi@192.168.156.1:/log/blog/current/*.log \
  ~/Projects/network-scanner/data/zeek/
```

### View Documentation
```bash
ls ~/Projects/network-scanner/docs/
cat ~/Projects/network-scanner/docs/QUICK_REFERENCE_CARD.md
```

---

## 🎉 You're Ready!

Once setup is complete, you can:

✅ Generate interactive HTML dashboards  
✅ Create comprehensive text reports  
✅ Monitor your network from any laptop  
✅ Track security posture  
✅ Identify devices and analyze traffic  
✅ Keep both laptops in sync via GitHub

---

**GitHub Repository:** https://github.com/MSSecCSA/network-scanner

**Questions?** Check the docs folder!

**Status:** Production Ready ✅

---

*Setup time: ~10 minutes*  
*Complexity: Easy*  
*Result: Full network visibility!* 🚀
