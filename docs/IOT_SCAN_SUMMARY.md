# 🏠 IoT Device Scan Summary - November 30, 2025

## Quick Stats
- **Total IoT Devices:** 14 identified
- **Fully Secure:** 5 (Wyze cameras)
- **Needs Attention:** 7 (TP-Link, Thermostat, Tuya)
- **Moderate Risk:** 3 (Google, Samsung TVs)

---

## 📸 CAMERAS (5) - ✅ ALL SECURE

| Device | IP | Ports | Status |
|--------|-----|-------|--------|
| Wyze Cam Pan | .85 | NONE | ✅ Secure |
| Wyze Cam v1 #1 | .126 | NONE | ✅ Secure |
| Wyze Cam v1 #2 | .184 | NONE | ✅ Secure |
| Wyze Cam v1 #3 | .34 | NONE | ✅ Secure |
| Wyze Cam v3 Pro | .36 | NONE | ✅ Secure |

**All cameras properly firewalled - no exposed ports!**

---

## 🔌 TP-LINK DEVICES (4) - ⚠️ PORT 9999 OPEN

| Device | IP | Model | Port 9999 |
|--------|-----|-------|-----------|
| Smart Plug | .120 | HS103 | ⚠️ OPEN |
| Unknown | .176 | ? | ⚠️ OPEN |
| Smart Plug | .96 | HS105 | ⚠️ OPEN |
| Smart Bulb | .251 | KL125 | ⚠️ OPEN |

**Protocol:** TP-Link Kasa (encrypted JSON)  
**Risk:** Moderate - protocol is encrypted but port should be blocked from internet  
**Action:** Consider IoT VLAN isolation

---

## 🎭 SMART HOME (3)

### Google Nest Audio - ⚠️ MODERATE
- **IP:** 192.168.156.198
- **Open Ports:** 8008, 8009, 8443, 9000, 10001
- **Services:** Chromecast, Google Home
- **Status:** Normal for Google devices (all encrypted)

### Sensi Thermostat - ⚠️ WARNING
- **IP:** 192.168.156.25
- **Open Port:** 80 (HTTP)
- **Status:** HTTP interface exposed - needs investigation
- **Action:** Check if web interface requires authentication

### Tuya Device - ❓ UNKNOWN
- **IP:** 192.168.156.196
- **Open Port:** 6668
- **Status:** Generic Tuya device - identify via Smart Life app
- **Action:** Determine device type and purpose

---

## 📺 SAMSUNG TVs (2) - ⚠️ MODERATE

### Master Bedroom (DU700D)
- **IP:** 192.168.156.84
- **Ports:** 7000, 8001, 8002, 8080, 8883, 8884
- **Features:** AirPlay, SmartThings Hub, Matter
- **Serial:** 0H093CRXC01796W

### Living Room (Q80BD 75")
- **IP:** 192.168.156.90
- **Ports:** 7000, 8001, 8002, 8080
- **Features:** AirPlay, SmartThings
- **Serial:** 0DVB3CDT405445R

**Status:** Multiple ports required for smart features (AirPlay, SmartThings)

---

## 🎯 ACTION ITEMS

### High Priority
1. **Investigate Sensi Thermostat (192.168.156.25)**
   - Port 80 HTTP open
   - Verify authentication required
   - Check for firmware updates

2. **Identify Tuya Device (192.168.156.196)**
   - Open Smart Life or Tuya app
   - Determine device type
   - Check security settings

3. **ID Unknown TP-Link (192.168.156.176)**
   - Check Kasa app for device list
   - Match MAC 84:d8:1b:cb:47:a0

### Medium Priority
4. **Consider IoT VLAN Segmentation**
   - Move all IoT to 192.168.157.0/24
   - Block IoT-to-IoT communication
   - Allow only outbound HTTPS/DNS

5. **Update All Firmware**
   - Wyze cameras (via app)
   - TP-Link devices (via Kasa)
   - Samsung TVs (via settings)
   - Sensi thermostat

### Low Priority
6. **Enable 2FA on Cloud Accounts**
   - Wyze account
   - TP-Link/Kasa account
   - Samsung account
   - Google Home account

---

## 📊 PORT SUMMARY

| Port | Device Count | Purpose |
|------|--------------|---------|
| 80 | 1 | HTTP (Thermostat) |
| 6668 | 1 | Tuya protocol |
| 7000 | 2 | AirPlay (Samsung TVs) |
| 8001-8002 | 2 | Samsung WebSocket API |
| 8008-8009 | 1 | Chromecast (Google) |
| 8080 | 2 | HTTP (Samsung TVs) |
| 8883-8884 | 1 | MQTT/SmartThings (Samsung) |
| 9000 | 1 | Google Home |
| 9999 | 4 | TP-Link Kasa |
| 10001 | 1 | Google Zone |

---

## 🔍 TRACKING DATABASE

All device details saved to:
- **CSV:** `data/scans/iot_tracking_database.csv`
- **Full Report:** `data/reports/iot_inventory_20251130.md`

**Unique identifiers captured:**
- MAC addresses (permanent)
- Serial numbers (where available)
- mDNS service IDs
- Model numbers
- Firmware versions

---

## 📅 NEXT STEPS

1. **Immediate:** Investigate Thermostat & Tuya device
2. **This Week:** Update all IoT firmware
3. **This Month:** Plan IoT VLAN implementation
4. **Ongoing:** Weekly scans to track changes

**Next Scan:** December 7, 2025 (weekly)

---

**Scan completed:** 2025-11-30 17:00 EST  
**Tools:** nmap, arp-scan, avahi-browse, netcat  
**Devices scanned:** 14 IoT devices identified and documented

---

## 🔄 UPDATE: Sensi Thermostat Investigation Complete

**Device:** Emerson Sensi Touch ST55 (192.168.156.25)

### ✅ SECURITY VERDICT: SECURE

**Initial Concern:** Port 80 open showing "File / not_found"

**Investigation Results:**
- ✅ **HomeKit Accessory Protocol (HAP)** - Apple's smart home protocol
- ✅ **Encrypted communication** - End-to-end encryption after pairing
- ✅ **No web interface** - Port 80 only responds to HAP, not browsers
- ✅ **Pairing required** - Physical access needed for 8-digit pairing code
- ✅ **Expected behavior** - All HTTP paths return 404 (by design)

**Device Information:**
- Model: ST55 (Sensi Touch)
- HomeKit ID: 5A:E3:C1:6A:7D:00
- Protocol Version: HAP 1.1
- Category: Thermostat (ci=9)

**The "File / not_found" message is NORMAL for HomeKit devices.**

### Updated Security Status

**Before:** ⚠️ WARNING - HTTP port 80 open  
**After:** ✅ SECURE - HomeKit protocol verified

**No action required** - device is operating correctly and securely.

---

**Update Date:** 2025-11-30 20:19 EST
