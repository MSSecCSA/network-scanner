# 🔍 Network Scan Summary - Nov 30, 2025

## Quick Stats
- **Total Devices:** 29
- **Wyze Cameras:** 5 ✅ All secure
- **Unknown Devices:** 6 ⚠️ Need investigation
- **Privacy Concerns:** 2 devices with MAC randomization

## 📸 Wyze Camera Status: ✅ SECURE

All 5 Wyze cameras have **no exposed ports** - they're properly firewalled!

| Camera | IP | Model | Status |
|--------|-----|-------|--------|
| wyze_cakp2jfus | 192.168.156.85 | Wyze Cam Pan | ✅ Secure |
| wyzec1-jz-502e | 192.168.156.126 | Wyze Cam v1 | ✅ Secure |
| wyzec1-jz-6938 | 192.168.156.184 | Wyze Cam v1 | ✅ Secure |
| wyzec1-jz-22f2 | 192.168.156.34 | Wyze Cam v1 | ✅ Secure |
| hl_cam3p | 192.168.156.36 | Wyze Cam v3 Pro | ✅ Secure |

**Security Assessment:**
- ✅ No HTTP/HTTPS interfaces exposed
- ✅ No RTSP streams accessible
- ✅ All traffic goes through Wyze cloud (outbound only)
- ✅ Firewalla properly blocking inbound connections

## 🔒 Privacy Alert: MAC Randomization

**2 Apple devices** have MAC randomization enabled:
1. Apple Watch (192.168.156.2)
2. iPhone (192.168.156.171)

**Why this matters:**
- Can't track devices consistently
- Wastes DHCP pool addresses
- Makes firewall rules difficult
- Complicates network troubleshooting

**Fix:** Settings → Wi-Fi → (i) next to "darkstar" → Toggle OFF "Private Wi-Fi Address"

## ⚠️ Action Items

1. **Identify 6 unknown devices:**
   - 192.168.156.103
   - 192.168.156.128  
   - 192.168.156.168
   - 192.168.156.97
   - 192.168.156.28
   - Check Firewalla device list

2. **Disable MAC randomization** on iOS devices

3. **Update Wyze cameras** via Wyze app

4. **Enable 2FA** on Wyze account

## 📊 Full Report

See: `data/reports/scan_report_20251130_1641.md`

**All scan data saved to:** `data/scans/`
