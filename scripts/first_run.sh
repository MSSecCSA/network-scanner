#!/bin/bash

# Network Scanner - First Run Setup Wizard
# Interactive setup for first-time users

set -e

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
cat << "EOF"
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║         NETWORK SCANNER - FIRST RUN SETUP             ║
║                                                       ║
║     Ethical Network Security & Monitoring Suite      ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Ethical use warning
echo -e "${RED}"
echo "⚠️  ═══════════════════════════════════════════════════"
echo "   CRITICAL LEGAL & ETHICAL WARNING"
echo "═══════════════════════════════════════════════════════${NC}"
echo ""
echo "This tool is designed for scanning networks that you OWN"
echo "or have EXPLICIT WRITTEN PERMISSION to test."
echo ""
echo -e "${RED}Unauthorized network scanning is ILLEGAL and may result in:"
echo "  • Criminal prosecution"
echo "  • Civil lawsuits"
echo "  • Imprisonment"
echo "  • Substantial fines${NC}"
echo ""
echo "By continuing, you acknowledge that:"
echo "  1. You will ONLY scan authorized networks"
echo "  2. You understand the legal risks"
echo "  3. You accept full responsibility for your actions"
echo "  4. The authors are NOT liable for misuse"
echo ""
read -p "Do you understand and agree? (yes/no): " AGREEMENT

if [ "$AGREEMENT" != "yes" ]; then
    echo ""
    echo -e "${RED}❌ Setup cancelled. You must agree to continue.${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}✓ Agreement acknowledged${NC}"
echo ""

# Check prerequisites
echo -e "${CYAN}📋 Checking prerequisites...${NC}"
echo ""

# Check Python version
if command -v python3.11 &> /dev/null; then
    PYTHON_VERSION=$(python3.11 --version)
    echo -e "${GREEN}✓${NC} Python: $PYTHON_VERSION"
else
    echo -e "${RED}❌ Python 3.11+ not found${NC}"
    echo "   Run: sudo ./scripts/install_deps.sh"
    exit 1
fi

# Check Poetry
if command -v poetry &> /dev/null; then
    POETRY_VERSION=$(poetry --version)
    echo -e "${GREEN}✓${NC} Poetry: $POETRY_VERSION"
else
    echo -e "${RED}❌ Poetry not found${NC}"
    echo "   Run: sudo ./scripts/install_deps.sh"
    exit 1
fi

# Check nmap
if command -v nmap &> /dev/null; then
    NMAP_VERSION=$(nmap --version | head -1)
    echo -e "${GREEN}✓${NC} Nmap: $NMAP_VERSION"
else
    echo -e "${YELLOW}⚠${NC}  Nmap not found (optional but recommended)"
fi

# Check PostgreSQL
if systemctl is-active --quiet postgresql; then
    echo -e "${GREEN}✓${NC} PostgreSQL: Running"
else
    echo -e "${RED}❌ PostgreSQL not running${NC}"
    echo "   Run: sudo systemctl start postgresql"
    exit 1
fi

# Check Redis
if systemctl is-active --quiet redis-server; then
    echo -e "${GREEN}✓${NC} Redis: Running"
else
    echo -e "${YELLOW}⚠${NC}  Redis not running (optional)"
fi

echo ""

# Network configuration
echo -e "${CYAN}🌐 Network Configuration${NC}"
echo ""

# Get current network
CURRENT_IP=$(ip -4 addr show | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | grep -v '127.0.0.1' | head -1)
CURRENT_NETWORK=$(echo $CURRENT_IP | sed 's/\.[0-9]*$/.0/')

echo "Detected IP: $CURRENT_IP"
echo "Suggested network: $CURRENT_NETWORK/24"
echo ""

read -p "Network to scan (e.g., 192.168.156.0/24) [$CURRENT_NETWORK/24]: " USER_NETWORK
NETWORK=${USER_NETWORK:-$CURRENT_NETWORK/24}

read -p "Gateway IP [$CURRENT_NETWORK.1]: " USER_GATEWAY
GATEWAY=${USER_GATEWAY:-$CURRENT_NETWORK.1}

echo ""
echo -e "${GREEN}✓${NC} Network: $NETWORK"
echo -e "${GREEN}✓${NC} Gateway: $GATEWAY"

# Update .env file
if [ -f ".env" ]; then
    sed -i "s|DEFAULT_NETWORK=.*|DEFAULT_NETWORK=$NETWORK|" .env
    sed -i "s|DEFAULT_GATEWAY=.*|DEFAULT_GATEWAY=$GATEWAY|" .env
    echo -e "${GREEN}✓${NC} Updated .env file"
fi

echo ""

# Install Python dependencies
echo -e "${CYAN}📦 Installing Python dependencies...${NC}"
echo ""

poetry install

echo ""
echo -e "${GREEN}✓${NC} Dependencies installed"
echo ""

# Create data directories
echo -e "${CYAN}📁 Creating data directories...${NC}"
mkdir -p data/scans data/reports logs
touch data/scans/.gitkeep data/reports/.gitkeep logs/.gitkeep

echo -e "${GREEN}✓${NC} Data directories created"
echo ""

# Final summary
echo -e "${CYAN}"
echo "═══════════════════════════════════════════════════"
echo "  ✅ SETUP COMPLETE!"
echo "═══════════════════════════════════════════════════"
echo -e "${NC}"
echo ""
echo "Your network scanner is ready to use!"
echo ""
echo "Quick Start Commands:"
echo ""
echo "  # Run interactive TUI:"
echo -e "  ${GREEN}poetry run python -m src.ui.app${NC}"
echo ""
echo "  # Run quick discovery scan:"
echo -e "  ${GREEN}poetry run python -m src.scanner.discovery${NC}"
echo ""
echo "  # Start API server:"
echo -e "  ${GREEN}poetry run uvicorn src.api.main:app --reload${NC}"
echo ""
echo "  # Run tests:"
echo -e "  ${GREEN}poetry run pytest${NC}"
echo ""
echo "Documentation:"
echo "  • Usage Guide: docs/USAGE.md"
echo "  • API Docs: docs/API.md"
echo "  • Ethics: docs/ETHICS.md"
echo ""
echo -e "${YELLOW}⚠️  REMEMBER: Only scan networks you own or have permission to test!${NC}"
echo ""
echo "Happy (ethical) scanning! 🔍"
echo ""
