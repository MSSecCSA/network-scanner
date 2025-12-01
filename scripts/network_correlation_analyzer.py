#!/usr/bin/env python3
"""
Network Correlation Analyzer
Ingests Zeek logs, Firewalla data, and nmap scans to build comprehensive device reports
"""

import json
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import socket

class NetworkCorrelationAnalyzer:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.devices = {}
        self.connections = defaultdict(list)
        self.dns_queries = defaultdict(list)
        
    def load_firewalla_csv(self, csv_path):
        """Load Firewalla device export"""
        print(f"Loading Firewalla devices from {csv_path}...")
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                mac = row['MAC Address'].lower()
                self.devices[mac] = {
                    'name': row['Device Name'],
                    'ip': row['IP Address'],
                    'vendor': row['Vendor'],
                    'status': row['Status'],
                    'network': row['Network'],
                    'first_seen': row['First Seen'],
                    'last_seen': row['Last Seen'],
                    'mac': mac,
                    'connections_count': 0,
                    'bytes_sent': 0,
                    'bytes_received': 0,
                    'protocols': set(),
                    'external_ips': set(),
                    'dns_queries': [],
                    'services': set()
                }
        print(f"✅ Loaded {len(self.devices)} devices from Firewalla")
        return len(self.devices)
    
    def load_zeek_conn_log(self, log_path):
        """Load Zeek connection logs"""
        print(f"Loading Zeek connections from {log_path}...")
        conn_count = 0
        with open(log_path, 'r') as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                try:
                    conn = json.loads(line)
                    mac = conn.get('orig_l2_addr', '').lower()
                    
                    if mac and mac in self.devices:
                        # Update device stats
                        self.devices[mac]['connections_count'] += 1
                        self.devices[mac]['bytes_sent'] += conn.get('orig_bytes', 0)
                        self.devices[mac]['bytes_received'] += conn.get('resp_bytes', 0)
                        
                        if 'service' in conn and conn['service']:
                            self.devices[mac]['services'].add(conn['service'])
                        if 'proto' in conn:
                            self.devices[mac]['protocols'].add(conn['proto'])
                        
                        # Track external connections (not local)
                        if not conn.get('local_resp', True):
                            dest_ip = conn.get('id.resp_h', '')
                            if dest_ip:
                                self.devices[mac]['external_ips'].add(dest_ip)
                        
                        # Store connection
                        self.connections[mac].append({
                            'dest_ip': conn.get('id.resp_h'),
                            'dest_port': conn.get('id.resp_p'),
                            'proto': conn.get('proto'),
                            'service': conn.get('service'),
                            'bytes_sent': conn.get('orig_bytes', 0),
                            'bytes_recv': conn.get('resp_bytes', 0),
                            'duration': conn.get('duration', 0),
                            'timestamp': conn.get('ts')
                        })
                        conn_count += 1
                except json.JSONDecodeError:
                    continue
        print(f"✅ Processed {conn_count} connections")
        return conn_count
    
    def load_zeek_dns_log(self, log_path):
        """Load Zeek DNS queries"""
        print(f"Loading DNS queries from {log_path}...")
        dns_count = 0
        with open(log_path, 'r') as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                try:
                    dns = json.loads(line)
                    # DNS logs don't have MAC, so match by IP
                    src_ip = dns.get('id.orig_h')
                    query = dns.get('query', '')
                    
                    # Find device by IP
                    for mac, device in self.devices.items():
                        if device['ip'] == src_ip:
                            device['dns_queries'].append(query)
                            dns_count += 1
                            break
                except json.JSONDecodeError:
                    continue
        print(f"✅ Processed {dns_count} DNS queries")
        return dns_count
    
    def categorize_device(self, device):
        """Determine device category"""
        name = device['name'].lower()
        vendor = device['vendor'].lower()
        
        if 'wyze' in name or 'wyze' in vendor:
            return 'Security Camera'
        elif 'tp-link' in vendor or any(x in name for x in ['kl125', 'hs103', 'hs105', 'ep40']):
            return 'Smart Plug/Bulb'
        elif 'samsung' in vendor and 'tv' in name:
            return 'Smart TV'
        elif 'lg' in name or ('ohsung' in vendor and any(x in name for x in ['washer', 'dryer'])):
            return 'Smart Appliance'
        elif 'google' in vendor or 'nest' in name:
            return 'Smart Speaker'
        elif 'apple' in vendor or 'iphone' in name or 'watch' in name:
            return 'Mobile Device'
        elif 'microsoft' in vendor or 'xbox' in name:
            return 'Gaming/Computer'
        elif 'asus' in vendor or 'zenwifi' in name:
            return 'Network Infrastructure'
        elif 'firewalla' in name:
            return 'Security Gateway'
        elif 'sensi' in name or 'thermostat' in name:
            return 'Smart Thermostat'
        elif 'tuya' in vendor or 'espressif' in vendor:
            return 'IoT Device'
        elif 'amazon' in vendor:
            return 'Smart Home Device'
        elif 'brother' in vendor:
            return 'Printer'
        else:
            return 'Unknown'
    
    def security_assessment(self, device):
        """Assess device security posture"""
        concerns = []
        risk_level = "LOW"
        
        # Check for excessive external connections
        ext_count = len(device['external_ips'])
        if ext_count > 10:
            concerns.append(f"Many external IPs ({ext_count})")
            risk_level = "MEDIUM"
        
        # Check for known risky ports
        for conn in self.connections.get(device['mac'], []):
            port = conn.get('dest_port')
            if port == 9999:
                concerns.append("Kasa port 9999 exposed")
                if risk_level == "LOW":
                    risk_level = "MEDIUM"
            elif port == 23:
                concerns.append("Telnet (port 23) detected")
                risk_level = "HIGH"
        
        # Check DNS query count
        dns_count = len(device['dns_queries'])
        if dns_count > 50:
            concerns.append(f"High DNS activity ({dns_count} queries)")
        
        return {
            'risk_level': risk_level,
            'concerns': concerns if concerns else ['None - Secure']
        }
    
    def generate_report(self, output_path):
        """Generate comprehensive network report"""
        print("\n=== GENERATING NETWORK CORRELATION REPORT ===\n")
        
        report = []
        report.append("=" * 100)
        report.append("COMPREHENSIVE NETWORK DEVICE REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S EST')}")
        report.append(f"Total Devices: {len([d for d in self.devices.values() if d['status'] == 'Online'])}")
        report.append("=" * 100)
        report.append("")
        
        # Group devices by category
        categories = defaultdict(list)
        for mac, device in self.devices.items():
            if device['status'] == 'Online':
                category = self.categorize_device(device)
                categories[category].append(device)
        
        # Generate report by category
        for category in sorted(categories.keys()):
            devices = sorted(categories[category], key=lambda x: x['name'])
            
            report.append("\n" + "=" * 100)
            report.append(f"📁 {category.upper()} ({len(devices)} devices)")
            report.append("=" * 100)
            
            for device in devices:
                security = self.security_assessment(device)
                
                report.append(f"\n┌─ {device['name']}")
                report.append(f"│  IP Address:      {device['ip']}")
                report.append(f"│  MAC Address:     {device['mac']}")
                report.append(f"│  Vendor:          {device['vendor']}")
                report.append(f"│  Status:          {device['status']}")
                report.append(f"│  First Seen:      {device['first_seen']}")
                report.append(f"│  Last Active:     {device['last_seen']}")
                
                # Network activity
                report.append(f"│")
                report.append(f"│  📊 NETWORK ACTIVITY (Last 3 minutes)")
                report.append(f"│  Connections:     {device['connections_count']}")
                report.append(f"│  Data Sent:       {self.format_bytes(device['bytes_sent'])}")
                report.append(f"│  Data Received:   {self.format_bytes(device['bytes_received'])}")
                report.append(f"│  Protocols:       {', '.join(sorted(device['protocols'])) or 'None detected'}")
                report.append(f"│  Services:        {', '.join(sorted(device['services'])) or 'None detected'}")
                report.append(f"│  External IPs:    {len(device['external_ips'])} unique destinations")
                
                # DNS activity
                if device['dns_queries']:
                    unique_domains = set(device['dns_queries'])
                    report.append(f"│")
                    report.append(f"│  🌐 DNS QUERIES")
                    report.append(f"│  Total Queries:   {len(device['dns_queries'])}")
                    report.append(f"│  Unique Domains:  {len(unique_domains)}")
                    report.append(f"│  Top Domains:     {', '.join(sorted(unique_domains)[:3])}")
                
                # Security assessment
                report.append(f"│")
                report.append(f"│  🔒 SECURITY ASSESSMENT")
                report.append(f"│  Risk Level:      {security['risk_level']}")
                report.append(f"│  Concerns:        {'; '.join(security['concerns'])}")
                
                # Top connections
                top_conns = sorted(
                    self.connections.get(device['mac'], [])[:5],
                    key=lambda x: x.get('bytes_sent', 0) + x.get('bytes_recv', 0),
                    reverse=True
                )[:3]
                
                if top_conns:
                    report.append(f"│")
                    report.append(f"│  🔗 TOP CONNECTIONS")
                    for i, conn in enumerate(top_conns, 1):
                        total_bytes = conn.get('bytes_sent', 0) + conn.get('bytes_recv', 0)
                        report.append(
                            f"│  {i}. {conn['dest_ip']}:{conn['dest_port']} "
                            f"({conn['proto']}/{conn.get('service', 'unknown')}) - "
                            f"{self.format_bytes(total_bytes)}"
                        )
                
                report.append("└─" + "─" * 98)
        
        # Summary statistics
        report.append("\n\n" + "=" * 100)
        report.append("📈 NETWORK SUMMARY STATISTICS")
        report.append("=" * 100)
        
        total_devices = len([d for d in self.devices.values() if d['status'] == 'Online'])
        total_connections = sum(d['connections_count'] for d in self.devices.values())
        total_bytes = sum(d['bytes_sent'] + d['bytes_received'] for d in self.devices.values())
        
        report.append(f"\nTotal Online Devices:     {total_devices}")
        report.append(f"Total Connections:        {total_connections}")
        report.append(f"Total Data Transfer:      {self.format_bytes(total_bytes)}")
        report.append(f"\nDevices by Category:")
        for category in sorted(categories.keys()):
            report.append(f"  • {category:25s} {len(categories[category]):3d} devices")
        
        # Risk summary
        high_risk = sum(1 for d in self.devices.values() 
                       if d['status'] == 'Online' and 
                       self.security_assessment(d)['risk_level'] == 'HIGH')
        medium_risk = sum(1 for d in self.devices.values() 
                         if d['status'] == 'Online' and 
                         self.security_assessment(d)['risk_level'] == 'MEDIUM')
        low_risk = total_devices - high_risk - medium_risk
        
        report.append(f"\nSecurity Risk Distribution:")
        report.append(f"  • High Risk:                {high_risk:3d} devices")
        report.append(f"  • Medium Risk:              {medium_risk:3d} devices")
        report.append(f"  • Low Risk:                 {low_risk:3d} devices")
        
        report.append("\n" + "=" * 100)
        report.append(f"Report saved to: {output_path}")
        report.append("=" * 100)
        
        # Write to file
        with open(output_path, 'w') as f:
            f.write('\n'.join(report))
        
        # Also print to console
        print('\n'.join(report))
        
        return output_path
    
    @staticmethod
    def format_bytes(bytes_val):
        """Format bytes to human readable"""
        if bytes_val == 0:
            return "0 B"
        units = ['B', 'KB', 'MB', 'GB']
        unit_index = 0
        value = float(bytes_val)
        while value >= 1024 and unit_index < len(units) - 1:
            value /= 1024
            unit_index += 1
        return f"{value:.2f} {units[unit_index]}"

def main():
    base_dir = Path.home() / 'Projects' / 'network-scanner'
    
    analyzer = NetworkCorrelationAnalyzer(base_dir)
    
    # Load data sources
    firewalla_csv = Path.home() / 'Downloads' / 'Firewalla_Devices.csv'
    zeek_conn = base_dir / 'data' / 'zeek' / 'conn.log'
    zeek_dns = base_dir / 'data' / 'zeek' / 'dns.log'
    
    analyzer.load_firewalla_csv(firewalla_csv)
    analyzer.load_zeek_conn_log(zeek_conn)
    analyzer.load_zeek_dns_log(zeek_dns)
    
    # Generate report
    output_path = base_dir / 'data' / 'reports' / f'network_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    analyzer.generate_report(output_path)

if __name__ == '__main__':
    main()
