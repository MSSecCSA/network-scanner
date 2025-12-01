# Network Scanner - Local Network Security & Monitoring Suite

## Project Overview

**Purpose:** A comprehensive, ethical network scanning and monitoring solution designed exclusively for personal home network security assessment and device management.

**⚠️ CRITICAL - ETHICAL USE ONLY:**
This tool is designed EXCLUSIVELY for scanning and monitoring networks that you own or have explicit written authorization to test. Unauthorized network scanning is illegal in most jurisdictions and may violate:
- Computer Fraud and Abuse Act (CFAA) - US
- Computer Misuse Act - UK  
- Similar laws worldwide

**By using this software, you acknowledge:**
1. You will ONLY scan networks you own or manage
2. You have explicit authorization for any network you scan
3. You understand unauthorized scanning is illegal
4. You accept full responsibility for your actions
5. The authors are not liable for misuse

## Technology Stack

### Core Language
- **Python 3.11+** (async/await for concurrent operations)

### Backend Framework
- **FastAPI** - REST API for TUI and future web interface
- **PostgreSQL** - Historical data, scan results, device tracking
- **Redis** - Real-time data caching, session management

### Network Scanning Tools
- **nmap** - Service/OS detection, comprehensive port scanning
- **masscan** - Ultra-fast port scanning for large ranges
- **scapy** - Packet crafting, custom protocol analysis
- **python-nmap** - Python wrapper for nmap
- **arp-scan** - Fast local network discovery

### Packet Analysis
- **tshark** - CLI packet capture and analysis
- **pyshark** - Python wrapper for tshark
- **airodump-ng** - Wireless network monitoring (optional)

### Firewalla Integration
- SSH-based flow data collection
- API integration (if available)
- Log parsing and correlation

### TUI Framework
- **Textual** - Modern, rich Python TUI framework
- Live dashboards, tables, and visualizations
- Keyboard-driven interface

### Vulnerability Detection
- **vulners** - Vulnerability database API
- **CVE integration** - Common Vulnerabilities and Exposures
- Custom vulnerability signatures

## Project Structure

```
network-scanner/
├── src/
│   ├── scanner/          # Core scanning engines
│   │   ├── __init__.py
│   │   ├── discovery.py  # Device discovery (ARP, ping, mDNS)
│   │   ├── port_scan.py  # Port scanning (nmap, masscan)
│   │   ├── service_enum.py # Service enumeration
│   │   └── passive.py    # Passive monitoring
│   ├── detector/         # Detection & fingerprinting
│   │   ├── __init__.py
│   │   ├── os_detect.py  # OS fingerprinting
│   │   ├── device_type.py # Device classification
│   │   ├── vuln_scan.py  # Vulnerability detection
│   │   └── signatures.py # Device signatures
│   ├── integrations/     # External system integrations
│   │   ├── __init__.py
│   │   ├── firewalla.py  # Firewalla API/SSH
│   │   ├── database.py   # PostgreSQL operations
│   │   └── cache.py      # Redis operations
│   ├── ui/               # User interface
│   │   ├── __init__.py
│   │   ├── app.py        # Main TUI application
│   │   ├── dashboard.py  # Dashboard view
│   │   ├── devices.py    # Device list view
│   │   └── scans.py      # Scan results view
│   └── api/              # REST API
│       ├── __init__.py
│       ├── main.py       # FastAPI app
│       └── routes/       # API endpoints
├── tests/                # Unit and integration tests
│   ├── test_scanner/
│   ├── test_detector/
│   └── test_integrations/
├── scripts/              # Utility scripts
│   ├── install_deps.sh   # Install system dependencies
│   ├── setup_db.sh       # Database initialization
│   └── first_run.sh      # Initial setup wizard
├── data/                 # Data storage
│   ├── scans/            # Scan results (JSON/CSV)
│   └── reports/          # Generated reports
├── logs/                 # Application logs
├── docs/                 # Documentation
│   ├── SETUP.md          # Setup instructions
│   ├── USAGE.md          # Usage guide
│   ├── API.md            # API documentation
│   └── ETHICS.md         # Ethical guidelines
├── .github/
│   └── workflows/        # GitHub Actions (future)
├── .gitignore
├── .env.example          # Environment variables template
├── pyproject.toml        # Python project config (Poetry)
├── requirements.txt      # Python dependencies
├── LICENSE               # MIT License
├── README.md             # Project overview
└── GEMINI.md             # This file
```

## Development Workflow

### Version Control
- **Git** with semantic commit messages
- **Conventional Commits** format
- Feature branches, pull requests
- Tagged releases (semver)

### Code Quality
- **Black** - Code formatting
- **isort** - Import sorting
- **flake8** - Linting
- **mypy** - Type checking
- **pytest** - Testing (>80% coverage goal)
- **pre-commit** - Git hooks for quality checks

### Environment Management
- **pyenv** - Python version management
- **Poetry** - Dependency management
- Virtual environments for isolation

## Features Roadmap

### Phase 1: Core Discovery & Mapping ✅ (Current)
- [x] Project structure created
- [ ] ARP-based device discovery
- [ ] ICMP ping sweeps
- [ ] mDNS/SSDP service discovery
- [ ] Device database schema
- [ ] Basic TUI dashboard

### Phase 2: Deep Analysis
- [ ] Comprehensive port scanning
- [ ] Service version detection
- [ ] OS fingerprinting
- [ ] Device manufacturer identification (OUI lookup)
- [ ] Historical device tracking

### Phase 3: Firewalla Integration
- [ ] SSH connection to Firewalla
- [ ] Flow data parsing
- [ ] Traffic pattern analysis
- [ ] Alert correlation
- [ ] Bandwidth monitoring per device

### Phase 4: Vulnerability Assessment
- [ ] CVE database integration
- [ ] Known vulnerability scanning
- [ ] Weak credential detection
- [ ] Open service warnings
- [ ] Security scoring per device

### Phase 5: Advanced Capabilities
- [ ] Packet capture management
- [ ] Wireless analysis (if hardware supports)
- [ ] Network health dashboard
- [ ] Automated reporting
- [ ] REST API for integrations

## Network Environment

### Current Setup
- **Router:** Firewalla Gold (192.168.156.1)
- **Network:** 192.168.156.0/24
- **WiFi APs:** Asus ZenWifi XT9 (AP mode)
  - Primary: darkstar (WPA2/WPA3)
  - IoT: morpheus (WPA2)
- **Protocols Enabled:**
  - ICMP (ping)
  - mDNS Relay
  - SSDP Relay
  - IGMP Proxy
  - IPv6 (dual-stack)

## Ethical Guidelines

### Acceptable Use
✅ Scanning your own home network
✅ Networks you own or manage
✅ Networks with explicit written authorization
✅ Educational purposes on isolated lab networks
✅ Security research on your own infrastructure

### Prohibited Use
❌ Scanning networks without authorization
❌ Port scanning public internet ranges
❌ Exploiting discovered vulnerabilities on others' systems
❌ Using for malicious purposes
❌ Circumventing security measures you don't own

## Security Considerations

- Store scan results locally (never cloud without encryption)
- Protect credentials in environment variables
- Use `.env` files (never commit to git)
- Implement role-based access if multi-user
- Log all scanning activities
- Regular security updates of dependencies

## Dependencies

### System Packages
```bash
sudo apt install -y \
  nmap \
  masscan \
  tshark \
  arp-scan \
  aircrack-ng \
  postgresql \
  redis-server \
  python3.11 \
  python3-pip \
  git
```

### Python Packages
See `requirements.txt` and `pyproject.toml`

## Current Status

**Created:** 2025-11-30
**Status:** Initial project setup
**Next Steps:** Install dependencies, implement device discovery

## Notes

- WiFi optimizations applied (power management disabled)
- Connected to darkstar SSID (5GHz, WPA3)
- Firewalla configured for scanning (ICMP enabled)
- Ready for development

---

**Remember: With great power comes great responsibility. Scan ethically.**
