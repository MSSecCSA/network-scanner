# Zeek Network Analysis Options for Firewalla Integration

## Current Status

**Firewalla Gold:** 192.168.156.1
- **SSH Port 22:** ✅ OPEN
- **Port 8833:** ✅ OPEN (Firewalla API/Management)
- **Zeek:** Firewalla runs Zeek internally for flow analysis

**Local Ubuntu Machine:**
- **Zeek:** Not installed (available in repos)
- **tcpdump:** ✅ Installed (v4.99.4)
- **tshark:** Not installed
- **Wireshark:** Not available (TUI environment)

---

## Option 1: SSH into Firewalla (RECOMMENDED)

### Accessing Firewalla's Zeek Data

**Firewalla Gold runs Zeek internally** for:
- Connection logging
- Protocol analysis
- Anomaly detection
- Threat intelligence correlation

### How to Enable SSH Access on Firewalla:

#### Method A: Via Firewalla Mobile App
1. Open Firewalla app on phone
2. Go to **Settings** → **Advanced** → **Developer Tools**
3. Enable **Developer Mode** or **SSH Access**
4. Note the SSH credentials provided

#### Method B: Via Web Interface
1. Access Firewalla at https://my.firewalla.com
2. Login with your account
3. Select your Firewalla Gold
4. Navigate to Advanced Settings
5. Enable Developer/SSH access

**Typical Firewalla SSH:**
```bash
# Default SSH (if enabled)
ssh pi@192.168.156.1
# OR
ssh firewalla@192.168.156.1

# Password: Usually shown in app or web interface
```

### Once SSH'd into Firewalla:

**Zeek log locations** (typical):
```bash
# Zeek connection logs
/log/zeek/conn.log
/log/zeek/dns.log
/log/zeek/http.log
/log/zeek/ssl.log

# OR possibly
/home/pi/.firewalla/run/zeek/
/firewalla/run/zeek/

# Flow data
/home/pi/.firewalla/run/
```

**Commands to try:**
```bash
# Find Zeek processes
ps aux | grep zeek

# Find Zeek logs
find / -name "conn.log" 2>/dev/null
find /log -type f -name "*.log" 2>/dev/null
find /home -name zeek -type d 2>/dev/null

# Check Zeek version
zeek --version

# View connection logs
tail -f /log/zeek/conn.log
```

---

## Option 2: Install Zeek Locally

### Installing Zeek on Ubuntu

**Zeek is available in Ubuntu repos:**

```bash
# Install Zeek
sudo apt update
sudo apt install zeek zeek-aux zkg

# Verify installation
zeek --version

# Default install location
/opt/zeek/
```

### Limitations of Local Zeek:

**Problem:** Zeek needs to see ALL network traffic

**Options for traffic capture:**

#### A. Mirror/SPAN Port (BEST for complete visibility)
- Configure Firewalla to mirror traffic to your Ubuntu machine
- Requires managed switch with port mirroring
- OR configure Firewalla to forward traffic copy

#### B. Tap Network Interface
```bash
# Capture on your laptop's interface (sees only local traffic)
sudo zeek -i wlp5s0 local

# Limited - only sees traffic to/from this laptop
```

#### C. Use tcpdump for Spot Analysis
```bash
# Capture traffic and analyze with Zeek
sudo tcpdump -i wlp5s0 -w capture.pcap
zeek -r capture.pcap
```

**Verdict:** Local Zeek is LIMITED without port mirroring

---

## Option 3: Hybrid Approach (RECOMMENDED)

### Combine Firewalla's Zeek + Local Tools

**Architecture:**
```
Network Traffic
    ↓
Firewalla (runs Zeek internally)
    ↓ (SSH access)
Copy Zeek logs to local machine
    ↓
Analyze locally with Zeek scripts
```

**Workflow:**

1. **SSH to Firewalla:**
   ```bash
   ssh pi@192.168.156.1
   ```

2. **Locate Zeek logs:**
   ```bash
   cd /log/zeek  # or wherever they are
   ls -lh
   ```

3. **Copy logs to local machine:**
   ```bash
   # On your Ubuntu laptop
   scp pi@192.168.156.1:/log/zeek/conn.log ~/Projects/network-scanner/data/zeek/
   scp pi@192.168.156.1:/log/zeek/*.log ~/Projects/network-scanner/data/zeek/
   ```

4. **Analyze locally:**
   ```bash
   # Install zeek-cut for log parsing
   sudo apt install zeek-aux
   
   # Parse connection logs
   cat conn.log | zeek-cut id.orig_h id.resp_h id.resp_p proto service
   
   # Or use Python/grep for analysis
   ```

---

## Option 4: Use Firewalla's Built-in Features

### Firewalla Already Provides Zeek Insights!

**Via Firewalla App:**
- Connection logs
- Top talkers
- Suspicious activity alerts
- Protocol analysis
- DNS queries
- SSL/TLS inspection

**Via Firewalla API:**
```bash
# Port 8833 is open - likely API access
curl -k https://192.168.156.1:8833/api/v1/status

# Requires authentication token from app
```

**Access Firewalla Data:**
1. Mobile app - Most comprehensive
2. Web interface - my.firewalla.com
3. API access (advanced)
4. SSH access (developer mode)

---

## RECOMMENDED APPROACH

### Step-by-Step Plan:

#### Phase 1: Enable Firewalla SSH (This Week)
1. ✅ Open Firewalla app
2. ✅ Enable Developer/SSH access
3. ✅ SSH in and explore
4. ✅ Locate Zeek log files
5. ✅ Document log locations

#### Phase 2: Automated Log Collection (Next Week)
1. ✅ Create SSH key for passwordless access
2. ✅ Script to rsync Zeek logs hourly/daily
3. ✅ Parse logs locally with Python
4. ✅ Build dashboard from Zeek data

#### Phase 3: Advanced Analysis (Future)
1. Install Zeek locally for scripting
2. Write custom Zeek scripts
3. Run against Firewalla's logs
4. Correlate with nmap scan data

---

## Comparison Matrix

| Option | Pros | Cons | Effort | Completeness |
|--------|------|------|--------|--------------|
| **SSH to Firewalla** | • Full network visibility<br>• Zeek already running<br>• No setup | • Need SSH access<br>• Firewalla-specific paths | Low | ⭐⭐⭐⭐⭐ |
| **Local Zeek** | • Full control<br>• Custom scripts | • Only sees local traffic<br>• Needs port mirror | High | ⭐⭐ |
| **Hybrid (SSH + Local)** | • Best of both<br>• Offline analysis | • Two systems | Medium | ⭐⭐⭐⭐⭐ |
| **Firewalla App** | • Easy<br>• Built-in | • Limited customization | None | ⭐⭐⭐⭐ |

---

## Security Considerations

### Enabling Firewalla SSH:

**Risks:**
- ⚠️ Opens access to Firewalla internals
- ⚠️ Could void warranty
- ⚠️ Potential for misconfiguration

**Mitigations:**
- ✅ Use SSH keys (not password)
- ✅ Only enable when needed
- ✅ Read-only access initially
- ✅ Don't modify Firewalla config
- ✅ Backup before experimenting

**Note:** Firewalla officially supports developer mode for power users

---

## Next Steps

### Immediate (Tonight):
1. Open Firewalla app
2. Check if Developer/SSH mode is available
3. Enable if comfortable
4. Test SSH connection

### Tomorrow:
1. SSH into Firewalla
2. Explore filesystem
3. Locate Zeek logs
4. Copy sample logs
5. Document structure

### This Week:
1. Set up automated log sync
2. Build Python parser
3. Create Zeek log dashboard
4. Integrate with network scanner

---

## Alternative: tcpdump Analysis (Available Now)

**Since tcpdump is already installed:**

```bash
# Capture 1000 packets for analysis
sudo tcpdump -i wlp5s0 -c 1000 -w sample.pcap

# View in real-time
sudo tcpdump -i wlp5s0 -n

# Filter by device
sudo tcpdump -i wlp5s0 host 192.168.156.85

# Filter by port
sudo tcpdump -i wlp5s0 port 9999

# DNS queries
sudo tcpdump -i wlp5s0 port 53
```

**Limitations:** Only sees traffic to/from this laptop

---

## Summary

**Best Path Forward:**

1. **Enable Firewalla SSH** - Get access to Zeek data ⭐
2. **Copy Zeek logs locally** - For analysis
3. **Use tcpdump for spot checks** - Immediate capability
4. **Consider local Zeek** - Only if you need custom scripts

**Firewalla's Zeek is already doing the heavy lifting!** You just need access to it.

---

**Document Created:** 2025-12-01 01:57 EST  
**Status:** Ready to enable Firewalla SSH access  
**Next Action:** Check Firewalla app for developer mode
