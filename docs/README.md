# 🔒 Network Scanner & Security Dashboard

**Professional-grade network monitoring and security analysis platform**

![Security Grade](https://img.shields.io/badge/Security%20Grade-A--Excellent-brightgreen)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Overview

A comprehensive network visibility platform that combines:
- **Firewalla device inventory** (network gateway integration)
- **Zeek network traffic analysis** (real-time monitoring)
- **Security vulnerability scanning** (nmap-based)
- **Automated correlation & reporting** (Python-powered)
- **Interactive HTML dashboard** (beautiful web interface)

**This tool is for monitoring YOUR OWN network only. Unauthorized network scanning is illegal.**

---

## ✨ Features

### 📊 Interactive HTML Dashboard
- Beautiful gradient design with responsive layout
- Real-time search across all devices
- Smart filtering by category and risk level
- Sortable columns (14 data points per device)
- Color-coded security risk indicators
- Works on desktop, tablet, and mobile
- Self-contained HTML (no server needed)

### 📈 Comprehensive Reports
- **Text Reports**: Detailed, grep-able analysis
- **HTML Dashboard**: Interactive visualization
- Device categorization (cameras, IoT, appliances, etc.)
- Security risk assessment (LOW/MEDIUM/HIGH)
- Bandwidth usage tracking
- DNS query monitoring
- Protocol and service identification

### 🔒 Security Analysis
- Port scanning and service detection
- Vulnerability assessment
- Behavior analysis (normal vs suspicious)
- External connection monitoring
- Risk scoring and recommendations

### 🔄 Automated Monitoring
- Pulls live data from Firewalla gateway
- Processes Zeek network logs
- Correlates multiple data sources
- Generates reports on-demand
- Historical tracking and comparison

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Firewalla gateway (Gold, Purple, etc.)
- SSH access to Firewalla
- Linux/macOS (Ubuntu recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/network-scanner.git
cd network-scanner

# Install dependencies
sudo apt update
sudo apt install -y nmap sshpass jq python3 python3-pip

# Set up environment
cp .env.example .env
# Edit .env with your Firewalla credentials
nano .env

# Create data directories
mkdir -p data/zeek data/reports data/scans
```

### Configuration

1. **Enable SSH on Firewalla**
   - Open Firewalla app
   - Settings → Advanced → SSH
   - Enable and note the password

2. **Export Device List from Firewalla**
   - Firewalla app → Devices
   - Export to CSV
   - Save to `~/Downloads/Firewalla_Devices.csv`

3. **Update .env file**
   ```bash
   FIREWALLA_IP=192.168.156.1
   FIREWALLA_USER=pi
   FIREWALLA_PASSWORD=your_password_here
   ```

### Usage

#### Generate Interactive HTML Dashboard
```bash
cd network-scanner
python3 scripts/generate_html_report.py
```

Opens automatically in browser! 🎨

#### Generate Text Report
```bash
python3 scripts/network_correlation_analyzer.py
```

#### Refresh Data & Generate New Dashboard
```bash
# Download latest Zeek logs
sshpass -p "$FIREWALLA_PASSWORD" scp \
  $FIREWALLA_USER@$FIREWALLA_IP:/log/blog/current/*.log data/zeek/

# Generate fresh dashboard
python3 scripts/generate_html_report.py
```

---

## 📁 Project Structure

```
network-scanner/
├── scripts/
│   ├── generate_html_report.py          # HTML dashboard generator
│   └── network_correlation_analyzer.py  # Text report generator
├── data/
│   ├── zeek/                            # Zeek logs from Firewalla
│   ├── reports/                         # Generated reports
│   └── scans/                           # nmap scan results
├── docs/                                # Documentation files
├── .env.example                         # Environment template
├── .gitignore                           # Git ignore rules
└── README.md                            # This file
```

---

## 🎯 Key Features

### Device Discovery
- Automatic device categorization
- Vendor identification (MAC lookup)
- First seen / Last seen tracking
- Online/offline status

### Network Activity
- Connection counting
- Bandwidth measurement (sent/received)
- Protocol identification (TCP/UDP/ICMP)
- Service detection (HTTP/DNS/SSL)

### Security Assessment
- **LOW Risk**: Secure, no concerns
- **MEDIUM Risk**: Minor issues (e.g., TP-Link Kasa port 9999)
- **HIGH Risk**: Critical vulnerabilities (Telnet, open ports)

### DNS Monitoring
- Query tracking per device
- Domain identification
- Unusual activity detection

---

## 🎨 Dashboard Features

### Statistics Cards
- Total devices online
- Total network connections
- Total data transfer
- Risk distribution (HIGH/MEDIUM/LOW)

### Interactive Filters
- **Search**: Real-time device search
- **Category**: Filter by device type
- **Risk Level**: Show only specific risk levels

### Sortable Table
Click any column header to sort by:
- Device name
- IP address
- Connection count
- Bandwidth usage
- DNS queries
- Risk level
- And more!

---

## 📖 Documentation

Comprehensive guides included:

- **QUICK_START_GUIDE.md** - Daily usage instructions
- **QUICK_REFERENCE_CARD.md** - Quick commands
- **HTML_DASHBOARD_GUIDE.md** - Dashboard usage
- **FIREWALLA_ZEEK_ACCESS.md** - SSH and Zeek setup
- **PROJECT_COMPLETE.md** - Full project summary

---

## 🔧 Advanced Usage

### Automated Daily Reports
```bash
# Add to crontab
crontab -e

# Run every morning at 8 AM
0 8 * * * cd ~/network-scanner && \
  sshpass -p "$FIREWALLA_PASSWORD" scp \
  pi@$FIREWALLA_IP:/log/blog/current/*.log data/zeek/ && \
  python3 scripts/generate_html_report.py
```

### Compare Reports Over Time
```bash
# Save baseline
cp data/reports/network_dashboard_*.html data/reports/baseline.html

# Generate new report later
python3 scripts/generate_html_report.py

# Compare device counts, security posture, etc.
```

### Export Specific Data
```bash
# View only high-risk devices
grep "Risk Level.*HIGH" data/reports/network_report_*.txt

# See all Wyze cameras
grep -A 15 "Security Camera" data/reports/network_report_*.txt

# Check DNS queries from specific IP
cat data/zeek/dns.log | jq 'select(."id.orig_h" == "192.168.156.84")'
```

---

## 🛡️ Security & Privacy

### Important Notes

⚠️ **This tool is for YOUR OWN network only!**
- Unauthorized network scanning is illegal
- Only scan networks you own or have permission to scan
- Respect privacy and security laws

### Data Handling

- Network logs contain sensitive information
- `.gitignore` excludes logs and reports
- `.env` file excluded from git (contains credentials)
- Use `.env.example` as template only

### Credentials

**Never commit:**
- Firewalla passwords
- Network logs
- Device lists with personal info
- Generated reports

---

## 🤝 Contributing

While this is a personal network monitoring tool, suggestions are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

**Note**: Remove any personal network data before submitting!

---

## 📊 Example Output

### Network Status
```
Total Devices: 53 online
Security Grade: A- (Excellent)

Risk Distribution:
  LOW:    51 devices (96%)
  MEDIUM:  2 devices (4%)
  HIGH:    0 devices (0%)

Device Categories:
  Security Cameras: 13
  Smart Plugs/Bulbs: 10
  IoT Devices: 7
  Mobile Devices: 4
  Computers: 3
  Smart TVs: 2
  Appliances: 2
```

---

## 🎓 Skills Demonstrated

This project showcases:

**Technical:**
- Python programming
- Network security concepts
- Data visualization (HTML/CSS/JS)
- Linux system administration
- Log analysis and correlation

**Tools:**
- Firewalla gateway
- Zeek network monitor
- nmap port scanner
- SSH automation
- JSON/CSV processing

---

## 📜 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

- **Firewalla** - Network gateway and security platform
- **Zeek** - Network traffic analysis framework
- **nmap** - Network scanner
- **Python** - Scripting and automation

---

## 📞 Support

For issues or questions:
1. Check the documentation in `/docs`
2. Review existing issues
3. Create a new issue with details

---

## 🚀 Roadmap

**Completed:**
- ✅ Device discovery and tracking
- ✅ Zeek log integration
- ✅ Security risk assessment
- ✅ Interactive HTML dashboard
- ✅ Automated reporting

**Future Enhancements:**
- [ ] Real-time dashboard (auto-refresh)
- [ ] Historical trending (graphs)
- [ ] Email alerting
- [ ] Dark mode theme
- [ ] Network topology visualization
- [ ] Anomaly detection (ML-based)

---

## 💼 Use Cases

**Home Network:**
- Monitor IoT devices
- Track bandwidth usage
- Ensure security compliance
- Troubleshoot connectivity

**Professional:**
- Portfolio project
- Learning platform
- Network security training
- SOC demonstrations

---

**Built with ❤️ for network visibility and security**

**Status:** Production Ready ✅  
**Last Updated:** 2025-12-01  
**Version:** 1.0.0

---

**⚠️ ETHICAL USE ONLY ⚠️**

This tool is designed for monitoring your own network.  
Unauthorized network scanning is illegal and unethical.  
Always obtain proper authorization before scanning any network.
