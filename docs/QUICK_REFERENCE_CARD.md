# 📇 NETWORK SCANNER - QUICK REFERENCE CARD

---

## 🚀 QUICK COMMANDS

### **Generate HTML Dashboard**
```bash
cd ~/Projects/network-scanner
python3 scripts/generate_html_report.py
```

### **Generate Text Report**
```bash
cd ~/Projects/network-scanner
python3 scripts/network_correlation_analyzer.py
```

### **Refresh All Data**
```bash
cd ~/Projects/network-scanner && \
sshpass -p 'PqSCNHefBV' scp pi@192.168.156.1:/log/blog/current/*.log data/zeek/ && \
python3 scripts/generate_html_report.py
```

### **Open Latest Dashboard**
```bash
xdg-open ~/Projects/network-scanner/data/reports/network_dashboard_*.html
```

### **SSH to Firewalla**
```bash
ssh pi@192.168.156.1
# Password: PqSCNHefBV
```

---

## 📁 KEY FILES

| File | Purpose |
|------|---------|
| `data/reports/network_dashboard_*.html` | Interactive web dashboard |
| `data/reports/network_report_*.txt` | Text report |
| `data/zeek/*.log` | Network logs from Firewalla |
| `~/Downloads/Firewalla_Devices.csv` | Device inventory |
| `scripts/generate_html_report.py` | HTML generator |
| `scripts/network_correlation_analyzer.py` | Text report generator |

---

## 🎯 COMMON TASKS

### **Find a Device**
- HTML: Type in search box
- Text: `grep "device-name" data/reports/network_report_*.txt`

### **Check Security**
- HTML: Click "High Risk" badge (should be 0)
- Text: `grep "Risk Level.*HIGH" data/reports/network_report_*.txt`

### **See Bandwidth Hogs**
- HTML: Sort by "Data Transfer" column
- Text: `grep "Data.*MB" data/reports/network_report_*.txt`

### **Monitor DNS**
- HTML: Sort by "DNS Queries" column
- Zeek: `cat data/zeek/dns.log | jq .query`

---

## 📊 YOUR NETWORK STATUS

**Devices:** 53 online  
**Security Grade:** A- (Excellent)  
**Risk:** 0 high, 2 medium, 51 low  

**Categories:**
- 13 Security Cameras
- 10 Smart Plugs/Bulbs
- 7 IoT Devices
- 4 Mobile Devices
- 3 Computers
- 2 Smart TVs
- 2 Appliances
- 12 Others

---

## 🔒 SECURITY NOTES

**Firewalla SSH:**
- IP: 192.168.156.1
- User: pi
- Pass: PqSCNHefBV
- Zeek Logs: /log/blog/current/

**Zeek Log Rotation:** Every 3 minutes  
**Log Retention:** 1 day

---

## 📖 DOCUMENTATION

| Guide | Location |
|-------|----------|
| Project Complete | `PROJECT_COMPLETE.md` |
| Quick Start | `QUICK_START_GUIDE.md` |
| HTML Dashboard | `HTML_DASHBOARD_GUIDE.md` |
| Firewalla/Zeek | `FIREWALLA_ZEEK_ACCESS.md` |
| Security Scan | `SCAN_COMPLETE_EXCELLENT_NEWS.md` |

---

## 🎨 DASHBOARD FEATURES

**Interactive:**
- ✅ Search (real-time)
- ✅ Filter by category
- ✅ Filter by risk
- ✅ Sort any column

**Data Shown:**
- Device name, IP, MAC
- Category & vendor
- Connections & bandwidth
- DNS queries
- Security risk level
- Top connections
- And more!

---

## 💡 DAILY WORKFLOW

**Morning (1 min):**
```bash
python3 ~/Projects/network-scanner/scripts/generate_html_report.py
# Check "High Risk" = 0
# Check device count = ~53
```

**Weekly (5 min):**
- Review medium-risk devices
- Check for new unknowns
- Compare with baseline
- Update documentation

---

## 🚨 RED FLAGS

Watch for:
- ⚠️ High Risk devices (investigate!)
- ⚠️ New unknown devices
- ⚠️ 100+ DNS queries (very chatty)
- ⚠️ 20+ external IPs (suspicious)
- ⚠️ Telnet/FTP detected (insecure!)

---

## ✅ NORMAL BEHAVIOR

Expected:
- ✅ Cameras: 0 connections when idle
- ✅ Appliances: 0 connections
- ✅ Phones: 10-50 connections
- ✅ Routers: 50+ connections
- ✅ TP-Link: Port 9999 (Kasa)

---

**Last Updated:** 2025-12-01 02:18 EST  
**Status:** All systems operational ✅  
**Next Review:** Daily
