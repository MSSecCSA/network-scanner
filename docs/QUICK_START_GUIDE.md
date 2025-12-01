# 🚀 Network Scanner - Quick Start Guide

## What You Have Now

A **complete network visibility platform** that combines:
- Firewalla device inventory
- Zeek network logs
- Security scanning (nmap)
- Automated correlation and reporting

---

## 📊 Generate a Fresh Network Report

### Step 1: Download Latest Zeek Logs
```bash
cd ~/Projects/network-scanner/data/zeek
sshpass -p 'PqSCNHefBV' scp pi@192.168.156.1:/log/blog/current/*.log ./
```

### Step 2: Run Correlation Analysis
```bash
cd ~/Projects/network-scanner
python3 scripts/network_correlation_analyzer.py
```

### Step 3: View Report
```bash
# Find latest report
ls -lt data/reports/network_report_*.txt | head -1

# View report
cat data/reports/network_report_*.txt | less
```

---

## 🔍 What The Report Shows You

### For EACH Device:
- ✅ Name, IP, MAC address
- ✅ Vendor and device type
- ✅ Online/offline status
- ✅ First seen / last seen
- ✅ **Network activity (connections, data transfer)**
- ✅ **Protocols and services used**
- ✅ **DNS queries made**
- ✅ **Security risk assessment**
- ✅ **Top connections**

### Network-Wide:
- Total devices online
- Total connections
- Total data transfer
- Devices by category
- Security risk distribution

---

## 📁 Key Files and Locations

### Configuration & Data
```
~/Projects/network-scanner/
├── data/
│   ├── zeek/              # Zeek logs from Firewalla
│   │   ├── conn.log       # Connection logs
│   │   ├── dns.log        # DNS queries
│   │   ├── http.log       # HTTP traffic
│   │   └── ssl.log        # TLS/SSL connections
│   ├── reports/           # Generated reports
│   └── scans/             # nmap scan results
├── scripts/
│   └── network_correlation_analyzer.py  # Main analyzer
└── ~/Downloads/
    └── Firewalla_Devices.csv  # Device inventory
```

### Important Documents
- `CORRELATION_REPORT_SUMMARY.md` - Latest analysis summary
- `FIREWALLA_ZEEK_ACCESS.md` - SSH access guide
- `SCAN_COMPLETE_EXCELLENT_NEWS.md` - Security assessment
- `ZEEK_ANALYSIS_OPTIONS.md` - Zeek setup guide

---

## 🔄 Daily Workflow

### Morning: Check Network Health
```bash
# Download fresh logs
cd ~/Projects/network-scanner
sshpass -p 'PqSCNHefBV' scp pi@192.168.156.1:/log/blog/current/*.log data/zeek/

# Generate report
python3 scripts/network_correlation_analyzer.py

# Quick summary
tail -50 data/reports/network_report_*.txt | less
```

### Look For:
- New devices appeared?
- Unusual connection counts?
- High-risk devices?
- Unexpected DNS queries?

---

## 🎯 Common Tasks

### 1. Find a Specific Device
```bash
# Search report for device by name
grep -A 20 "Samsung TV" data/reports/network_report_*.txt

# Search by IP
grep -A 20 "192.168.156.84" data/reports/network_report_*.txt
```

### 2. Check Device Activity
```bash
# View all connections from a device (using Zeek logs directly)
cd data/zeek
cat conn.log | jq 'select(."id.orig_h" == "192.168.156.84")'

# View DNS queries from device
cat dns.log | jq 'select(."id.orig_h" == "192.168.156.84") | .query'
```

### 3. Monitor Specific Device Type
```bash
# All Wyze cameras
grep -A 15 "Security Camera" data/reports/network_report_*.txt

# All TP-Link devices
grep -A 15 "Smart Plug" data/reports/network_report_*.txt
```

### 4. Security Check
```bash
# Find any high-risk devices
grep -B 5 "Risk Level:      HIGH" data/reports/network_report_*.txt

# Find medium-risk devices
grep -B 5 "Risk Level:      MEDIUM" data/reports/network_report_*.txt
```

---

## 📊 Understanding the Report

### Device Categories
- **Security Camera** - Wyze cameras (13)
- **Smart Plug/Bulb** - TP-Link devices (10)
- **IoT Device** - Generic smart devices (7)
- **Mobile Device** - Phones, tablets (4)
- **Gaming/Computer** - PCs, Xbox (3)
- **Smart Appliance** - LG washer/dryer (2)
- **Smart TV** - Samsung TVs (2)
- **Network Infrastructure** - Routers (2)

### Risk Levels
- **LOW** - No concerns, secure ✅
- **MEDIUM** - Minor concerns (e.g., TP-Link port 9999)
- **HIGH** - Significant issues (needs attention!)

### Connection Count
- **0 connections** - Device idle (normal for cameras/appliances)
- **1-10 connections** - Light activity
- **10-50 connections** - Normal activity (phones, PCs)
- **50+ connections** - Heavy activity (routers, servers)

---

## 🚨 What to Watch For

### Normal Behavior:
- ✅ Cameras: 0 connections when idle
- ✅ Appliances: 0 connections when not in use
- ✅ Phones: 10-50 connections (apps, notifications)
- ✅ TVs: Some connections for content recommendations
- ✅ Routers: High connection count (routing traffic)

### Suspicious Behavior:
- ⚠️ Camera with hundreds of connections
- ⚠️ Appliance constantly connecting
- ⚠️ New unknown device appeared
- ⚠️ Device connecting to unusual ports
- ⚠️ Excessive DNS queries (>100)

---

## 🔧 Troubleshooting

### "Connection refused" to Firewalla
```bash
# Test SSH access
ssh pi@192.168.156.1
# If fails, check Firewalla app SSH settings
```

### "File not found" for Zeek logs
```bash
# Verify logs exist on Firewalla
ssh pi@192.168.156.1 'ls -la /log/blog/current/'

# Re-download
cd ~/Projects/network-scanner/data/zeek
sshpass -p 'PqSCNHefBV' scp pi@192.168.156.1:/log/blog/current/*.log ./
```

### Python script errors
```bash
# Check Python version
python3 --version  # Should be 3.8+

# Verify files
ls -la ~/Downloads/Firewalla_Devices.csv
ls -la ~/Projects/network-scanner/data/zeek/conn.log
```

---

## 📈 Advanced Usage

### Compare Two Reports
```bash
# Generate baseline
python3 scripts/network_correlation_analyzer.py
mv data/reports/network_report_*.txt data/reports/baseline.txt

# Wait some time, generate new report
# ... do stuff on network ...
python3 scripts/network_correlation_analyzer.py

# Compare
diff data/reports/baseline.txt data/reports/network_report_*.txt
```

### Track Bandwidth Over Time
```bash
# Run every hour and save
for i in {1..24}; do
  sshpass -p 'PqSCNHefBV' scp pi@192.168.156.1:/log/blog/current/conn.log \
    data/zeek/conn_$(date +%H%M).log
  sleep 3600
done
```

### Export to CSV
```bash
# Modify analyzer script to output CSV instead of text
# (Future enhancement)
```

---

## 🎓 Learning More

### Understanding Zeek Logs
- Read: `FIREWALLA_ZEEK_ACCESS.md`
- Zeek field reference: https://docs.zeek.org/en/master/

### Firewalla Features
- Documentation: https://help.firewalla.com/
- Community: https://help.firewalla.com/hc/en-us/community/topics

### Network Security
- Review reports daily
- Establish baseline behavior
- Alert on deviations

---

## 📞 Quick Reference Commands

```bash
# Download latest Zeek logs
sshpass -p 'PqSCNHefBV' scp pi@192.168.156.1:/log/blog/current/*.log ~/Projects/network-scanner/data/zeek/

# Generate report
cd ~/Projects/network-scanner && python3 scripts/network_correlation_analyzer.py

# View latest report
ls -lt ~/Projects/network-scanner/data/reports/ | head -5

# SSH to Firewalla
ssh pi@192.168.156.1

# Scan network (nmap)
sudo nmap -sn 192.168.156.0/24

# Check device by IP
cat ~/Projects/network-scanner/data/zeek/conn.log | jq 'select(."id.orig_h" == "192.168.156.84")'
```

---

## 🎉 You're All Set!

**Your network monitoring platform is:**
- ✅ Fully operational
- ✅ Automated
- ✅ Comprehensive
- ✅ Easy to use

**Run the analyzer anytime to get fresh insights!**

---

**Last Updated:** 2025-12-01 02:12 EST  
**Status:** Production-ready ✅  
**Support:** All docs in ~/Projects/network-scanner/
