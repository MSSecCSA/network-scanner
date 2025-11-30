#!/bin/bash

# Network Scanner - Database Setup Script
# Initializes PostgreSQL database and creates schema

set -e

echo "=================================================="
echo "Network Scanner - Database Setup"
echo "=================================================="
echo ""

# Default configuration
DB_NAME="network_scanner"
DB_USER="netscanner"
DB_PASSWORD=${DB_PASSWORD:-$(openssl rand -base64 32)}
DB_HOST="localhost"
DB_PORT="5432"

echo "📊 Database Configuration:"
echo "   Name: $DB_NAME"
echo "   User: $DB_USER"
echo "   Host: $DB_HOST"
echo "   Port: $DB_PORT"
echo ""

# Check if PostgreSQL is running
if ! systemctl is-active --quiet postgresql; then
    echo "❌ PostgreSQL is not running. Starting..."
    sudo systemctl start postgresql
    sleep 2
fi

echo "✓ PostgreSQL is running"
echo ""

# Create database user and database
echo "🔐 Creating database user and database..."
sudo -u postgres psql << EOF
-- Drop existing if recreating
DROP DATABASE IF EXISTS $DB_NAME;
DROP USER IF EXISTS $DB_USER;

-- Create user
CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';

-- Create database
CREATE DATABASE $DB_NAME OWNER $DB_USER;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;

-- Connect to database and set up schema
\c $DB_NAME

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO $DB_USER;

EOF

echo "✓ Database and user created"
echo ""

# Create .env file with database credentials
ENV_FILE="/home/$(logname)/Projects/network-scanner/.env"

if [ ! -f "$ENV_FILE" ]; then
    echo "📝 Creating .env file..."
    cp "/home/$(logname)/Projects/network-scanner/.env.example" "$ENV_FILE"
    
    # Update database URL in .env
    sed -i "s|DATABASE_URL=.*|DATABASE_URL=postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME|" "$ENV_FILE"
    
    chmod 600 "$ENV_FILE"
    chown $(logname):$(logname) "$ENV_FILE"
    
    echo "✓ Created .env file with database credentials"
else
    echo "⚠️  .env file already exists. Update manually if needed:"
    echo "   DATABASE_URL=postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"
fi

echo ""
echo "=================================================="
echo "✅ Database Setup Complete!"
echo "=================================================="
echo ""
echo "Database credentials:"
echo "  URL: postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"
echo ""
echo "⚠️  IMPORTANT: Save these credentials securely!"
echo "   They are stored in .env (not committed to git)"
echo ""
echo "Next steps:"
echo "1. Run: cd /home/$(logname)/Projects/network-scanner"
echo "2. Run: poetry install"
echo "3. Run: poetry run alembic upgrade head"
echo ""
