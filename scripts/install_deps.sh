#!/bin/bash

# Network Scanner - System Dependencies Installation Script
# This script installs all required system packages for network scanning

set -e

echo "=================================================="
echo "Network Scanner - System Dependencies Installation"
echo "=================================================="
echo ""

# Check if running with sudo
if [ "$EUID" -ne 0 ]; then 
    echo "❌ Please run this script with sudo:"
    echo "   sudo ./scripts/install_deps.sh"
    exit 1
fi

# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
    VER=$VERSION_ID
else
    echo "❌ Cannot detect OS. This script supports Ubuntu/Debian."
    exit 1
fi

echo "✓ Detected OS: $OS $VER"
echo ""

# Update package lists
echo "📦 Updating package lists..."
apt update

# Install core system packages
echo ""
echo "🔧 Installing core system packages..."
apt install -y \
    build-essential \
    git \
    curl \
    wget \
    software-properties-common \
    ca-certificates \
    gnupg \
    lsb-release

# Install Python 3.11+
echo ""
echo "🐍 Installing Python 3.11..."
add-apt-repository -y ppa:deadsnakes/ppa 2>/dev/null || true
apt update
apt install -y \
    python3.11 \
    python3.11-dev \
    python3.11-venv \
    python3-pip \
    python-is-python3

# Install network scanning tools
echo ""
echo "🌐 Installing network scanning tools..."
apt install -y \
    nmap \
    masscan \
    arp-scan \
    net-tools \
    iproute2 \
    iputils-ping \
    dnsutils \
    tcpdump \
    aircrack-ng

# Install Wireshark/tshark
echo ""
echo "📊 Installing packet analysis tools..."
DEBIAN_FRONTEND=noninteractive apt install -y \
    wireshark \
    tshark

# Allow non-root users to capture packets
echo ""
echo "🔓 Configuring packet capture permissions..."
dpkg-reconfigure -p critical wireshark-common 2>/dev/null || true
usermod -a -G wireshark $SUDO_USER 2>/dev/null || true

# Install PostgreSQL
echo ""
echo "🗄️  Installing PostgreSQL..."
apt install -y \
    postgresql \
    postgresql-contrib \
    libpq-dev

# Install Redis
echo ""
echo "⚡ Installing Redis..."
apt install -y redis-server

# Start and enable services
echo ""
echo "🚀 Starting services..."
systemctl start postgresql
systemctl enable postgresql
systemctl start redis-server
systemctl enable redis-server

# Install Poetry (Python dependency manager)
echo ""
echo "📦 Installing Poetry..."
if ! command -v poetry &> /dev/null; then
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="/root/.local/bin:$PATH"
    echo 'export PATH="/root/.local/bin:$PATH"' >> /home/$SUDO_USER/.bashrc
else
    echo "✓ Poetry already installed"
fi

# Install additional useful tools
echo ""
echo "🛠️  Installing additional tools..."
apt install -y \
    jq \
    htop \
    tmux \
    neovim \
    fzf \
    ripgrep

# Cleanup
echo ""
echo "🧹 Cleaning up..."
apt autoremove -y
apt clean

echo ""
echo "=================================================="
echo "✅ Installation Complete!"
echo "=================================================="
echo ""
echo "Next steps:"
echo "1. Log out and back in (for wireshark group membership)"
echo "2. Run: cd /home/$SUDO_USER/Projects/network-scanner"
echo "3. Run: poetry install"
echo "4. Run: ./scripts/setup_db.sh"
echo "5. Run: ./scripts/first_run.sh"
echo ""
echo "⚠️  IMPORTANT: This tool is for authorized use only!"
echo "   See docs/ETHICS.md for guidelines."
echo ""
