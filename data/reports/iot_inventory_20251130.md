# IoT & Smart Home Device Inventory - Deep Scan
## Scan Date: 2025-11-30 16:55 EST

---

## 📸 WYZE CAMERAS (5 Devices)

### Camera 1: Wyze Cam Pan
- **IP Address:** 192.168.156.85
- **MAC Address:** 7c:78:b2:19:ea:5c
- **Hostname:** wyze_cakp2jfus-7c78b219ea5c.lan
- **Model:** Wyze Cam Pan (CAKP2JFUS)
- **MAC Vendor:** Wyze Labs Inc
- **Open Ports:** NONE (all closed - secure)
- **Protocols:** Cloud-only (outbound HTTPS to Wyze servers)
- **SNMP:** Not available
- **Unique Identifiers:**
  - Serial hint in hostname: 7c78b219ea5c
  - Model code: CAKP2JFUS
- **Security Status:** ✅ SECURE - No exposed services
- **Notes:** Pan/tilt camera model, fully firewalled

### Camera 2: Wyze Cam v1
- **IP Address:** 192.168.156.126
- **MAC Address:** 2c:aa:8e:19:50:2e
- **Hostname:** wyzec1-jz-2caa8e19502e.lan
- **Model:** Wyze Cam v1 (WYZEC1-JZ)
- **MAC Vendor:** Wyze Labs Inc
- **Open Ports:** NONE
- **Protocols:** Cloud-only
- **SNMP:** Not available
- **Unique Identifiers:**
  - Serial hint: 2caa8e19502e
  - Model code: WYZEC1-JZ
- **Security Status:** ✅ SECURE
- **Notes:** First generation Wyze Cam

### Camera 3: Wyze Cam v1
- **IP Address:** 192.168.156.184
- **MAC Address:** 2c:aa:8e:2c:69:38
- **Hostname:** wyzec1-jz-2caa8e2c6938.lan
- **Model:** Wyze Cam v1 (WYZEC1-JZ)
- **MAC Vendor:** Wyze Labs Inc
- **Open Ports:** NONE
- **Protocols:** Cloud-only
- **SNMP:** Not available
- **Unique Identifiers:**
  - Serial hint: 2caa8e2c6938
  - Model code: WYZEC1-JZ
- **Security Status:** ✅ SECURE
- **Notes:** First generation Wyze Cam

### Camera 4: Wyze Cam v1
- **IP Address:** 192.168.156.34
- **MAC Address:** 2c:aa:8e:19:22:f2
- **Hostname:** wyzec1-jz-2caa8e1922f2.lan
- **Model:** Wyze Cam v1 (WYZEC1-JZ)
- **MAC Vendor:** Wyze Labs Inc
- **Open Ports:** NONE
- **Protocols:** Cloud-only
- **SNMP:** Not available
- **Unique Identifiers:**
  - Serial hint: 2caa8e1922f2
  - Model code: WYZEC1-JZ
- **Security Status:** ✅ SECURE
- **Notes:** First generation Wyze Cam

### Camera 5: Wyze Cam v3 Pro
- **IP Address:** 192.168.156.36
- **MAC Address:** d0:3f:27:93:59:6d
- **Hostname:** hl_cam3p-d03f2793596d.lan
- **Model:** Wyze Cam v3 Pro (HL_CAM3P)
- **MAC Vendor:** Wyze Labs Inc
- **Open Ports:** NONE
- **Protocols:** Cloud-only
- **SNMP:** Not available
- **Unique Identifiers:**
  - Serial hint: d03f2793596d
  - Model code: HL_CAM3P
- **Security Status:** ✅ SECURE
- **Notes:** Latest generation with color night vision

---

## 🔌 TP-LINK SMART DEVICES (4 Devices)

### TP-Link Device 1: Smart Plug HS103
- **IP Address:** 192.168.156.120
- **MAC Address:** 00:5f:67:d4:de:99
- **Hostname:** hs103.lan
- **Model:** HS103 (Smart Plug)
- **MAC Vendor:** TP-Link Corporation Limited
- **Open Ports:**
  - **9999/tcp** - TP-Link Smart Home Protocol (proprietary)
- **Protocols:**
  - Kasa protocol on port 9999 (JSON over TCP)
  - Cloud connection for remote access
- **SNMP:** Port 161 closed (SNMP not enabled)
- **Unique Identifiers:**
  - Device type: Smart Plug (on/off only)
  - Protocol: TP-Link Kasa
- **Security Status:** ⚠️ WARNING - Port 9999 open
- **Notes:**
  - Local control via Kasa app
  - Responds to port 9999 but doesn't reveal info without encryption
  - Consider isolating to IoT VLAN

### TP-Link Device 2: Unknown Model
- **IP Address:** 192.168.156.176
- **MAC Address:** 84:d8:1b:cb:47:a0
- **Hostname:** tp-link.technologies.co.ltd.lan
- **Model:** Unknown TP-Link device
- **MAC Vendor:** TP-LINK TECHNOLOGIES CO.,LTD.
- **Open Ports:**
  - **9999/tcp** - TP-Link Smart Home Protocol
- **Protocols:** Kasa protocol on port 9999
- **SNMP:** Port 161 closed
- **Unique Identifiers:**
  - MAC prefix: 84:d8:1b (TP-Link)
- **Security Status:** ⚠️ WARNING - Port 9999 open
- **Notes:** Needs identification via Kasa app

### TP-Link Device 3: Smart Plug HS105
- **IP Address:** 192.168.156.96
- **MAC Address:** 84:d8:1b:cb:4d:ba
- **Hostname:** hs105.lan
- **Model:** HS105 (Mini Smart Plug)
- **MAC Vendor:** TP-LINK TECHNOLOGIES CO.,LTD.
- **Open Ports:**
  - **9999/tcp** - TP-Link Smart Home Protocol
- **Protocols:** Kasa protocol on port 9999
- **SNMP:** Port 161 closed
- **Unique Identifiers:**
  - Device type: Mini Smart Plug
- **Security Status:** ⚠️ WARNING - Port 9999 open
- **Notes:** Compact model, no energy monitoring

### TP-Link Device 4: Smart Bulb KL125
- **IP Address:** 192.168.156.251
- **MAC Address:** e8:48:b8:f0:d0:c0
- **Hostname:** kl125.lan
- **Model:** KL125 (Smart Bulb - Color)
- **MAC Vendor:** TP-Link Corporation Limited
- **Open Ports:**
  - **9999/tcp** - TP-Link Smart Home Protocol
- **Protocols:** Kasa protocol on port 9999
- **SNMP:** Port 161 closed
- **Unique Identifiers:**
  - Device type: Color-changing LED bulb
  - Supports dimming and color temperature
- **Security Status:** ⚠️ WARNING - Port 9999 open
- **Notes:** Wi-Fi connected bulb, no hub required

---

## 🔊 GOOGLE/NEST DEVICES (1 Device)

### Google Nest Audio
- **IP Address:** 192.168.156.198
- **MAC Address:** ac:67:84:04:66:56
- **Hostname:** braidens.room.speaker.lan
- **Model:** Nest Audio
- **MAC Vendor:** Google, Inc.
- **Open Ports:**
  - **8008/tcp** - HTTP (Chromecast control)
  - **8009/tcp** - SSL/TLS (Secure Chromecast)
  - **8443/tcp** - HTTPS alternate
  - **9000/tcp** - SSL (Google Home/Nest protocol)
  - **10001/tcp** - SSL (Google Zone discovery)
- **Protocols:**
  - mDNS (_googlecast._tcp, _googlezone._tcp)
  - Chromecast protocol
  - Google Home/Assistant protocol
- **SNMP:** Not applicable
- **Unique Identifiers:**
  - Chromecast ID: 7bded5b1b6c418427dee442e31359b52
  - Device ID: 61B27860C41DCF64C2A742ABBDCD97B4
  - Friendly Name: "Braiden's room speaker"
  - Model: Nest Audio (md=Nest Audio)
  - Version: ve=05
- **mDNS Services:**
  - _googlecast._tcp (port 8009)
  - _googlezone._tcp (port 10001)
  - _googcrossdevice._tcp (port 10101)
- **Security Status:** ⚠️ MODERATE - Multiple open ports (expected for functionality)
- **Notes:**
  - Responds to "Hey Google" voice commands
  - Supports multi-room audio
  - Uses encrypted connections for voice/audio

---

## 📺 SAMSUNG SMART TVs (2 Devices)

### Samsung TV 1: Master Bedroom TV
- **IP Address:** 192.168.156.84
- **MAC Address:** c8:a6:ef:db:bc:57
- **Hostname:** masterbedroomtv.lan / Samsung.local
- **Model:** DU700D (Samsung 4K Smart TV)
- **MAC Vendor:** Samsung Electronics Co.,Ltd
- **Open Ports:**
  - **7000/tcp** - AirPlay (AirTunes RTSP 377.40.00)
  - **8001/tcp** - Samsung WebSocket API (HTTP - returns 403)
  - **8002/tcp** - SSL Samsung WebSocket API (HTTPS - returns 403)
  - **8080/tcp** - HTTP proxy/WebServer
  - **8081/tcp** - SmartThings integration
  - **8883/tcp** - MQTT (SmartThings - TLS)
  - **8884/tcp** - MQTT (SmartThings - mTLS)
- **Protocols:**
  - AirPlay 2 (Apple devices)
  - SmartThings hub functionality
  - Matter smart home protocol
  - mDNS (_smartthings._tcp, _airplay._tcp, _matter._tcp)
- **SNMP:** Not applicable
- **Unique Identifiers:**
  - Serial Number: 0H093CRXC01796W
  - SmartThings Hub ID: 442f1e49-27c5-4da0-bff2-5157f0cdd362
  - SmartThings Device ID: D052A8DCE0940001
  - Matter Device ID: 85C5AA10FCE40CB6-F1D6FAF481F15933
  - AirPlay Device ID: 8D:30:74:BF:13:B9
  - Model: DU700D
  - Firmware: p20.T-KSU2EDAKUC-1310.1
- **mDNS Services:**
  - _smartthings._tcp (port 8081)
  - _smartthings-mqtt._tcp (ports 8883, 8884)
  - _airplay._tcp (port 7000)
  - _matter._tcp (port 58663)
  - _smartthings-hedge._tcp (port 8765)
- **Security Status:** ⚠️ MODERATE - Multiple services exposed (required for smart features)
- **Notes:**
  - Acts as SmartThings hub
  - Supports Apple AirPlay
  - Matter-compatible for smart home control
  - Web interface protected (403 Forbidden)

### Samsung TV 2: Living Room TV
- **IP Address:** 192.168.156.90
- **MAC Address:** 54:44:a3:21:ad:a0
- **Hostname:** samsung.q80bd.75.tv.lan / Samsung-2.local
- **Model:** QBQ8D / Q80BD 75" (Samsung QLED 4K)
- **MAC Vendor:** Samsung Electronics Co.,Ltd
- **Open Ports:**
  - **7000/tcp** - AirPlay (RTSP)
  - **8001/tcp** - Samsung WebSocket API
  - **8002/tcp** - SSL Samsung WebSocket API
  - **8080/tcp** - HTTP WebServer
- **Protocols:**
  - AirPlay 2
  - SmartThings (likely)
  - mDNS (_airplay._tcp)
- **SNMP:** Not applicable
- **Unique Identifiers:**
  - Serial Number: 0DVB3CDT405445R
  - AirPlay Device ID: B4:43:8C:02:E6:37
  - Model: QBQ8D (Q80BD series)
  - Firmware: p20.T-PTMAKUC-1710.0
- **mDNS Services:**
  - _airplay._tcp (port 7000)
  - Likely _smartthings services (not captured in scan)
- **Security Status:** ⚠️ MODERATE - Multiple services for smart features
- **Notes:**
  - QLED (Quantum Dot) display technology
  - 75-inch model
  - Supports Apple AirPlay
  - SmartThings compatible

---

## 🌡️ HVAC/CLIMATE (1 Device)

### White Rodgers Thermostat
- **IP Address:** 192.168.156.25
- **MAC Address:** 34:6f:92:0f:aa:6e
- **Hostname:** Unknown (no hostname resolution)
- **Model:** Unknown White Rodgers model
- **MAC Vendor:** White Rodgers Division (Emerson)
- **Open Ports:** (Scan not completed in output)
- **Protocols:** Likely proprietary Emerson/White Rodgers protocol
- **SNMP:** Unknown (scan incomplete)
- **Unique Identifiers:**
  - MAC OUI: 34:6f:92 (White Rodgers)
- **Security Status:** ⚠️ UNKNOWN - Requires further investigation
- **Notes:**
  - HVAC thermostat
  - Likely Wi-Fi enabled for remote control
  - May support Emerson Sensi app
  - Recommend checking for firmware updates

---

## 🏠 OTHER IoT DEVICES

### Tuya Smart Device
- **IP Address:** 192.168.156.196
- **MAC Address:** d4:a6:51:cc:48:e8
- **Hostname:** Unknown
- **Model:** Generic Tuya-compatible device
- **MAC Vendor:** Tuya Smart Inc.
- **Open Ports:** (Scan not completed)
- **Protocols:** Tuya IoT protocol (cloud-based)
- **SNMP:** Not applicable
- **Unique Identifiers:**
  - MAC OUI: d4:a6:51 (Tuya Smart)
- **Security Status:** ⚠️ UNKNOWN - Tuya devices vary widely
- **Notes:**
  - Tuya is a platform used by many brands
  - Likely controlled via Smart Life or Tuya app
  - Could be: smart plug, bulb, sensor, switch, etc.
  - Recommend identifying specific device type

---

## 🔒 SECURITY RECOMMENDATIONS

### Critical Issues
1. **TP-Link Devices** - Port 9999 exposed on all 4 devices
   - ✅ Protocol is encrypted but still a potential attack vector
   - ✅ Recommend: Create IoT VLAN and isolate from main network
   - ✅ Block port 9999 from internet (should already be blocked by Firewalla)
   - ✅ Disable remote access in Kasa app if not needed

### Medium Priority
2. **Samsung TVs** - Multiple open ports for smart features
   - ✅ Ports are required for AirPlay, SmartThings, Matter
   - ✅ Web interfaces return 403 (good - auth required)
   - ✅ Keep firmware updated via TV settings
   - ✅ Review SmartThings device access permissions

3. **Google Nest Audio** - Multiple SSL ports open
   - ✅ All connections encrypted
   - ✅ Standard for Google/Chromecast devices
   - ✅ Review Google Home app privacy settings
   - ✅ Consider guest network for visitors

### Best Practices
4. **All IoT Devices**
   - ✅ Create dedicated VLAN (192.168.157.0/24) for IoT
   - ✅ Block IoT-to-IoT communication (prevent lateral movement)
   - ✅ Allow only outbound HTTPS (443) and DNS (53)
   - ✅ Monitor outbound connections in Firewalla
   - ✅ Regular firmware updates
   - ✅ Strong unique passwords for each device/app
   - ✅ Enable 2FA on all cloud accounts (Wyze, TP-Link, Samsung, Google)

5. **Wyze Cameras** - Already secure!
   - ✅ No changes needed - properly firewalled
   - ✅ Continue monitoring via Wyze app
   - ✅ Check for firmware updates monthly

---

## 📊 SUMMARY STATISTICS

**Total IoT Devices Scanned:** 15
- Cameras: 5 (Wyze)
- Smart Plugs/Bulbs: 4 (TP-Link)
- Smart Speakers: 1 (Google)
- Smart TVs: 2 (Samsung)
- Thermostat: 1 (White Rodgers)
- Unknown IoT: 1 (Tuya)
- Printer: 1 (Brother - not detailed here)

**Port Summary:**
- Devices with NO open ports: 5 (all Wyze cameras) ✅
- Devices with port 9999 open: 4 (TP-Link) ⚠️
- Devices with multiple ports: 3 (Google, 2x Samsung) ⚠️

**Protocol Summary:**
- Cloud-only: 6 (Wyze cameras, Tuya)
- Local + Cloud: 8 (TP-Link, Google, Samsung, Thermostat)
- SNMP-enabled: 0
- mDNS-advertised: 3 (Google, 2x Samsung)

**Security Status:**
- ✅ SECURE: 5 devices (Wyze cameras)
- ⚠️ MODERATE: 8 devices (TP-Link, Google, Samsung)
- ⚠️ UNKNOWN: 2 devices (Thermostat, Tuya)

---

## 📝 TRACKING IDENTIFIERS

**For future scans, track these key identifiers:**

### Primary Identifiers
1. **MAC Address** - Never changes (unless spoofed)
2. **IP Address** - May change with DHCP
3. **Hostname** - Usually stable

### Secondary Identifiers
4. **Open Ports** - Fingerprint for device type
5. **mDNS Service Names** - Unique IDs in broadcasts
6. **Serial Numbers** - From mDNS or web interfaces
7. **Firmware Versions** - Track update status

### Monitoring Strategy
- **Weekly:** ARP scan to detect new/removed devices
- **Monthly:** Port scan to detect service changes
- **Quarterly:** Full vulnerability scan
- **On Alert:** Immediate deep scan if suspicious activity

---

**Scan Completed:** 2025-11-30 16:57 EST  
**Tools Used:** nmap, arp-scan, avahi-browse, netcat  
**Next Scan Recommended:** 2025-12-07 (weekly)

