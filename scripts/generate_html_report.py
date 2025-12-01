#!/usr/bin/env python3
"""
Interactive HTML Network Report Generator
Creates a beautiful, sortable, filterable HTML dashboard
"""

import json
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

class HTMLReportGenerator:
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
        print(f"✅ Loaded {len(self.devices)} devices")
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
                        self.devices[mac]['connections_count'] += 1
                        self.devices[mac]['bytes_sent'] += conn.get('orig_bytes', 0)
                        self.devices[mac]['bytes_received'] += conn.get('resp_bytes', 0)
                        
                        if 'service' in conn and conn['service']:
                            self.devices[mac]['services'].add(conn['service'])
                        if 'proto' in conn:
                            self.devices[mac]['protocols'].add(conn['proto'])
                        
                        if not conn.get('local_resp', True):
                            dest_ip = conn.get('id.resp_h', '')
                            if dest_ip:
                                self.devices[mac]['external_ips'].add(dest_ip)
                        
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
                    src_ip = dns.get('id.orig_h')
                    query = dns.get('query', '')
                    
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
        
        ext_count = len(device['external_ips'])
        if ext_count > 10:
            concerns.append(f"Many external IPs ({ext_count})")
            risk_level = "MEDIUM"
        
        for conn in self.connections.get(device['mac'], []):
            port = conn.get('dest_port')
            if port == 9999:
                concerns.append("Kasa port 9999 exposed")
                if risk_level == "LOW":
                    risk_level = "MEDIUM"
            elif port == 23:
                concerns.append("Telnet (port 23) detected")
                risk_level = "HIGH"
        
        dns_count = len(device['dns_queries'])
        if dns_count > 50:
            concerns.append(f"High DNS activity ({dns_count} queries)")
        
        return {
            'risk_level': risk_level,
            'concerns': concerns if concerns else ['None - Secure']
        }
    
    def format_bytes(self, bytes_val):
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
    
    def generate_html(self, output_path):
        """Generate interactive HTML report"""
        print("\n=== GENERATING INTERACTIVE HTML REPORT ===\n")
        
        # Prepare device data
        device_data = []
        categories = defaultdict(int)
        risk_counts = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0}
        
        for mac, device in self.devices.items():
            if device['status'] != 'Online':
                continue
                
            category = self.categorize_device(device)
            security = self.security_assessment(device)
            total_bytes = device['bytes_sent'] + device['bytes_received']
            
            categories[category] += 1
            risk_counts[security['risk_level']] += 1
            
            # Get top connections
            top_conns = sorted(
                self.connections.get(mac, [])[:10],
                key=lambda x: x.get('bytes_sent', 0) + x.get('bytes_recv', 0),
                reverse=True
            )[:3]
            
            top_conns_html = '<br>'.join([
                f"{conn['dest_ip']}:{conn['dest_port']} ({conn['proto']}/{conn.get('service', 'unknown')})"
                for conn in top_conns
            ]) if top_conns else 'None'
            
            # Get top DNS
            unique_dns = list(set(device['dns_queries']))[:5]
            dns_html = '<br>'.join(unique_dns) if unique_dns else 'None'
            
            device_data.append({
                'name': device['name'],
                'ip': device['ip'],
                'mac': device['mac'],
                'vendor': device['vendor'],
                'category': category,
                'connections': device['connections_count'],
                'bytes_sent': device['bytes_sent'],
                'bytes_received': device['bytes_received'],
                'total_bytes': total_bytes,
                'total_bytes_formatted': self.format_bytes(total_bytes),
                'protocols': ', '.join(sorted(device['protocols'])) or 'None',
                'services': ', '.join(sorted(device['services'])) or 'None',
                'external_ips': len(device['external_ips']),
                'dns_count': len(device['dns_queries']),
                'risk_level': security['risk_level'],
                'concerns': '; '.join(security['concerns']),
                'top_connections': top_conns_html,
                'top_dns': dns_html,
                'first_seen': device['first_seen'],
                'last_seen': device['last_seen']
            })
        
        # Sort by total bytes descending
        device_data.sort(key=lambda x: x['total_bytes'], reverse=True)
        
        # Generate HTML
        html = self.generate_html_template(device_data, categories, risk_counts)
        
        with open(output_path, 'w') as f:
            f.write(html)
        
        print(f"✅ Interactive HTML report generated: {output_path}")
        print(f"📊 {len(device_data)} devices • {len(categories)} categories")
        print(f"🔒 Security: {risk_counts['HIGH']} high, {risk_counts['MEDIUM']} medium, {risk_counts['LOW']} low risk")
        
        return output_path
    
    def generate_html_template(self, device_data, categories, risk_counts):
        """Generate HTML template"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S EST')
        total_devices = len(device_data)
        total_connections = sum(d['connections'] for d in device_data)
        total_bytes = sum(d['total_bytes'] for d in device_data)
        
        # Generate category badges
        category_badges = ''.join([
            f'<span class="badge badge-category" data-category="{cat}">{cat} ({count})</span>'
            for cat, count in sorted(categories.items())
        ])
        
        # Generate device rows
        device_rows = ''
        for device in device_data:
            risk_class = f"risk-{device['risk_level'].lower()}"
            device_rows += f'''
            <tr class="device-row" data-category="{device['category']}" data-risk="{device['risk_level']}">
                <td><strong>{device['name']}</strong></td>
                <td><code>{device['ip']}</code></td>
                <td><span class="badge badge-category">{device['category']}</span></td>
                <td>{device['connections']}</td>
                <td>{device['total_bytes_formatted']}</td>
                <td><span class="badge {risk_class}">{device['risk_level']}</span></td>
                <td>{device['dns_count']}</td>
                <td>{device['external_ips']}</td>
                <td><small>{device['protocols']}</small></td>
                <td><small>{device['services']}</small></td>
                <td><small>{device['vendor']}</small></td>
                <td class="expandable"><small>{device['top_connections']}</small></td>
                <td class="expandable"><small>{device['top_dns']}</small></td>
                <td><small>{device['concerns']}</small></td>
            </tr>
            '''
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Security Report - {timestamp}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #333;
        }}
        
        .container {{
            max-width: 1600px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.2s;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        
        .stat-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            display: block;
        }}
        
        .stat-label {{
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
        }}
        
        .filters {{
            padding: 20px 30px;
            background: #fff;
            border-bottom: 2px solid #f0f0f0;
        }}
        
        .filter-group {{
            margin-bottom: 15px;
        }}
        
        .filter-group label {{
            font-weight: 600;
            margin-right: 10px;
            color: #555;
        }}
        
        .filter-group input {{
            padding: 8px 12px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            font-size: 14px;
            width: 300px;
            transition: border-color 0.2s;
        }}
        
        .filter-group input:focus {{
            outline: none;
            border-color: #667eea;
        }}
        
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: 600;
            cursor: pointer;
            margin: 2px;
            transition: all 0.2s;
        }}
        
        .badge:hover {{
            transform: scale(1.05);
        }}
        
        .badge-category {{
            background: #e3f2fd;
            color: #1976d2;
        }}
        
        .badge-category.active {{
            background: #1976d2;
            color: white;
        }}
        
        .risk-low {{
            background: #d4edda;
            color: #155724;
        }}
        
        .risk-medium {{
            background: #fff3cd;
            color: #856404;
        }}
        
        .risk-high {{
            background: #f8d7da;
            color: #721c24;
        }}
        
        .table-container {{
            padding: 30px;
            overflow-x: auto;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }}
        
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 10px;
            text-align: left;
            font-weight: 600;
            cursor: pointer;
            user-select: none;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        
        th:hover {{
            background: linear-gradient(135deg, #5568d3 0%, #653a8b 100%);
        }}
        
        th::after {{
            content: ' ⇅';
            opacity: 0.5;
        }}
        
        td {{
            padding: 12px 10px;
            border-bottom: 1px solid #f0f0f0;
        }}
        
        tr:hover {{
            background: #f8f9fa;
        }}
        
        .device-row.hidden {{
            display: none;
        }}
        
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        
        .expandable {{
            max-width: 200px;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        
        small {{
            font-size: 0.85em;
            color: #666;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            color: #666;
            font-size: 0.9em;
        }}
        
        @media (max-width: 768px) {{
            .stats {{
                grid-template-columns: 1fr;
            }}
            
            .filter-group input {{
                width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔒 Network Security Dashboard</h1>
            <p>Generated: {timestamp}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <span class="stat-value">{total_devices}</span>
                <span class="stat-label">Total Devices Online</span>
            </div>
            <div class="stat-card">
                <span class="stat-value">{total_connections}</span>
                <span class="stat-label">Total Connections</span>
            </div>
            <div class="stat-card">
                <span class="stat-value">{self.format_bytes(total_bytes)}</span>
                <span class="stat-label">Total Data Transfer</span>
            </div>
            <div class="stat-card">
                <span class="stat-value" style="color: #28a745;">{risk_counts['LOW']}</span>
                <span class="stat-label">Low Risk Devices</span>
            </div>
            <div class="stat-card">
                <span class="stat-value" style="color: #ffc107;">{risk_counts['MEDIUM']}</span>
                <span class="stat-label">Medium Risk Devices</span>
            </div>
            <div class="stat-card">
                <span class="stat-value" style="color: #dc3545;">{risk_counts['HIGH']}</span>
                <span class="stat-label">High Risk Devices</span>
            </div>
        </div>
        
        <div class="filters">
            <div class="filter-group">
                <label>🔍 Search:</label>
                <input type="text" id="searchInput" placeholder="Search by name, IP, vendor...">
            </div>
            <div class="filter-group">
                <label>📁 Filter by Category:</label>
                {category_badges}
                <span class="badge badge-category" data-category="all">All Devices</span>
            </div>
            <div class="filter-group">
                <label>🔒 Filter by Risk:</label>
                <span class="badge risk-low" data-risk="LOW">Low Risk</span>
                <span class="badge risk-medium" data-risk="MEDIUM">Medium Risk</span>
                <span class="badge risk-high" data-risk="HIGH">High Risk</span>
                <span class="badge" style="background: #e0e0e0;" data-risk="all">All Risk Levels</span>
            </div>
        </div>
        
        <div class="table-container">
            <table id="deviceTable">
                <thead>
                    <tr>
                        <th onclick="sortTable(0)">Device Name</th>
                        <th onclick="sortTable(1)">IP Address</th>
                        <th onclick="sortTable(2)">Category</th>
                        <th onclick="sortTable(3)">Connections</th>
                        <th onclick="sortTable(4)">Data Transfer</th>
                        <th onclick="sortTable(5)">Risk</th>
                        <th onclick="sortTable(6)">DNS Queries</th>
                        <th onclick="sortTable(7)">External IPs</th>
                        <th onclick="sortTable(8)">Protocols</th>
                        <th onclick="sortTable(9)">Services</th>
                        <th onclick="sortTable(10)">Vendor</th>
                        <th>Top Connections</th>
                        <th>Top DNS</th>
                        <th>Security Concerns</th>
                    </tr>
                </thead>
                <tbody>
                    {device_rows}
                </tbody>
            </table>
        </div>
        
        <div class="footer">
            <p>Generated by Network Correlation Analyzer • {total_devices} devices monitored • Powered by Firewalla + Zeek</p>
            <p>Security Grade: <strong>A-</strong> (Excellent)</p>
        </div>
    </div>
    
    <script>
        // Search functionality
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', filterDevices);
        
        let activeCategory = 'all';
        let activeRisk = 'all';
        
        // Category filter
        document.querySelectorAll('.badge-category').forEach(badge => {{
            badge.addEventListener('click', function() {{
                document.querySelectorAll('.badge-category').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                activeCategory = this.dataset.category;
                filterDevices();
            }});
        }});
        
        // Risk filter
        document.querySelectorAll('[data-risk]').forEach(badge => {{
            badge.addEventListener('click', function() {{
                activeRisk = this.dataset.risk;
                filterDevices();
            }});
        }});
        
        function filterDevices() {{
            const searchTerm = searchInput.value.toLowerCase();
            const rows = document.querySelectorAll('.device-row');
            
            rows.forEach(row => {{
                const text = row.textContent.toLowerCase();
                const category = row.dataset.category;
                const risk = row.dataset.risk;
                
                const matchesSearch = text.includes(searchTerm);
                const matchesCategory = activeCategory === 'all' || category === activeCategory;
                const matchesRisk = activeRisk === 'all' || risk === activeRisk;
                
                if (matchesSearch && matchesCategory && matchesRisk) {{
                    row.classList.remove('hidden');
                }} else {{
                    row.classList.add('hidden');
                }}
            }});
        }}
        
        // Table sorting
        let sortDirection = {{}};
        
        function sortTable(columnIndex) {{
            const table = document.getElementById('deviceTable');
            const tbody = table.querySelector('tbody');
            const rows = Array.from(tbody.querySelectorAll('tr:not(.hidden)'));
            
            const direction = sortDirection[columnIndex] === 'asc' ? 'desc' : 'asc';
            sortDirection[columnIndex] = direction;
            
            rows.sort((a, b) => {{
                let aVal = a.cells[columnIndex].textContent.trim();
                let bVal = b.cells[columnIndex].textContent.trim();
                
                // Try to parse as number
                const aNum = parseFloat(aVal.replace(/[^0-9.-]/g, ''));
                const bNum = parseFloat(bVal.replace(/[^0-9.-]/g, ''));
                
                if (!isNaN(aNum) && !isNaN(bNum)) {{
                    return direction === 'asc' ? aNum - bNum : bNum - aNum;
                }}
                
                // String comparison
                return direction === 'asc' ? 
                    aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
            }});
            
            // Re-append sorted rows
            rows.forEach(row => tbody.appendChild(row));
        }}
        
        // Auto-refresh indicator
        console.log('Network Security Dashboard loaded successfully!');
        console.log('Total devices: {total_devices}');
        console.log('Security status: {risk_counts["HIGH"]} high, {risk_counts["MEDIUM"]} medium, {risk_counts["LOW"]} low risk');
    </script>
</body>
</html>'''

def main():
    base_dir = Path.home() / 'Projects' / 'network-scanner'
    
    generator = HTMLReportGenerator(base_dir)
    
    # Load data sources
    firewalla_csv = Path.home() / 'Downloads' / 'Firewalla_Devices.csv'
    zeek_conn = base_dir / 'data' / 'zeek' / 'conn.log'
    zeek_dns = base_dir / 'data' / 'zeek' / 'dns.log'
    
    generator.load_firewalla_csv(firewalla_csv)
    generator.load_zeek_conn_log(zeek_conn)
    generator.load_zeek_dns_log(zeek_dns)
    
    # Generate HTML report
    output_path = base_dir / 'data' / 'reports' / f'network_dashboard_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    generator.generate_html(output_path)
    
    print(f"\n🌐 Open in browser: file://{output_path}")

if __name__ == '__main__':
    main()
