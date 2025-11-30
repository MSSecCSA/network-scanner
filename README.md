# Network Scanner - Personal Network Security Suite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive, ethical network scanning and monitoring solution for personal home network security assessment and device management.

---

## ⚠️ **ETHICAL USE WARNING**

**THIS TOOL IS FOR AUTHORIZED USE ONLY**

By downloading, installing, or using this software, you acknowledge and agree that:

1. ✅ You will **ONLY** scan networks you own or have explicit written permission to test
2. ✅ Unauthorized network scanning is **ILLEGAL** under:
   - Computer Fraud and Abuse Act (CFAA) - United States
   - Computer Misuse Act - United Kingdom
   - Similar laws in other jurisdictions
3. ✅ You accept **full responsibility** for your actions
4. ✅ The authors are **NOT LIABLE** for any misuse of this software

**Violation of these terms may result in criminal prosecution.**

For detailed ethical guidelines, see [docs/ETHICS.md](docs/ETHICS.md)

---

## 🚀 Features

### Current (Phase 1)
- 🔍 **Device Discovery**: ARP scanning, ICMP ping sweeps, mDNS/SSDP detection
- 📊 **Live Dashboard**: Real-time TUI interface with device status
- 🗄️ **Historical Tracking**: PostgreSQL-backed device history
- 🔄 **Passive Monitoring**: Non-intrusive network observation

### Planned
- 🔐 **Port Scanning**: Comprehensive service enumeration (nmap, masscan)
- 🖥️ **OS Detection**: Fingerprinting and device classification
- 🛡️ **Vulnerability Scanning**: CVE database integration
- 🔥 **Firewalla Integration**: Traffic analysis and flow data correlation
- 📡 **Wireless Analysis**: WiFi security assessment (optional)
- 📈 **Reporting**: Automated security reports and recommendations

---

## 📋 Prerequisites

### System Requirements
- **OS**: Linux (Ubuntu 20.04+, Debian 11+, or similar)
- **Python**: 3.11 or higher
- **RAM**: 2GB minimum, 4GB recommended
- **Disk**: 500MB for application, 5GB+ for scan data
- **Network**: Access to target network (LAN)

### Required Permissions
- `sudo` access for packet capture and privileged scanning
- Network administrator rights on target network

---

## 🛠️ Installation

### 1. Clone Repository
```bash
cd ~/Projects
git clone https://github.com/yourusername/network-scanner.git
cd network-scanner
```

### 2. Run Installation Script
```bash
chmod +x scripts/install_deps.sh
./scripts/install_deps.sh
```

This will install:
- System packages (nmap, masscan, tshark, etc.)
- PostgreSQL and Redis
- Python dependencies via Poetry

### 3. Configure Environment
```bash
cp .env.example .env
nano .env  # Edit with your settings
```

### 4. Initialize Database
```bash
./scripts/setup_db.sh
```

### 5. Run First-Time Setup
```bash
./scripts/first_run.sh
```

---

## 🎯 Quick Start

### Interactive TUI Mode
```bash
poetry run python -m src.ui.app
```

### Run Quick Network Scan
```bash
poetry run python -m src.scanner.discovery --network 192.168.1.0/24
```

### Start API Server
```bash
poetry run uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

---

## 📚 Documentation

- [Setup Guide](docs/SETUP.md) - Detailed installation instructions
- [Usage Guide](docs/USAGE.md) - How to use the scanner
- [API Reference](docs/API.md) - REST API documentation
- [Ethical Guidelines](docs/ETHICS.md) - Responsible use policies
- [Architecture](docs/ARCHITECTURE.md) - System design and components

---

## 🧪 Development

### Setup Development Environment
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install
```

### Run Tests
```bash
poetry run pytest
```

### Code Quality
```bash
# Format code
poetry run black src/ tests/

# Sort imports
poetry run isort src/ tests/

# Lint
poetry run flake8 src/ tests/

# Type check
poetry run mypy src/
```

---

## 🏗️ Project Structure

```
network-scanner/
├── src/                  # Source code
│   ├── scanner/          # Scanning engines
│   ├── detector/         # Detection & fingerprinting
│   ├── integrations/     # External integrations
│   ├── ui/               # TUI interface
│   └── api/              # REST API
├── tests/                # Unit & integration tests
├── scripts/              # Utility scripts
├── data/                 # Scan results & reports
├── docs/                 # Documentation
└── logs/                 # Application logs
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes using [Conventional Commits](https://www.conventionalcommits.org/)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Note**: All contributions must adhere to ethical use guidelines.

---

## 🔒 Security

### Reporting Vulnerabilities
If you discover a security vulnerability, please email: security@yourdomain.com

**Do NOT** create a public GitHub issue.

### Data Protection
- All scan results are stored **locally only**
- Credentials are stored in `.env` (never committed)
- Database is encrypted at rest (optional)
- Logs are rotated and sanitized

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

**Disclaimer**: This license does NOT grant permission to scan networks you do not own or have authorization to test.

---

## 🙏 Acknowledgments

- [nmap](https://nmap.org/) - Network exploration and security auditing
- [masscan](https://github.com/robertdavidgraham/masscan) - Fast port scanner
- [Textual](https://textual.textualize.io/) - Modern TUI framework
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Firewalla](https://firewalla.com/) - Network security appliance

---

## 📞 Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/yourusername/network-scanner/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/network-scanner/discussions)

---

## ⚖️ Legal Notice

This tool is provided for **educational and authorized security testing purposes only**. Users are solely responsible for compliance with all applicable laws and regulations. The authors assume no liability for misuse or damage caused by this software.

**Scan responsibly. Scan ethically. Scan legally.**

---

**Built with ❤️ for network security professionals and enthusiasts**
