import socket
import time
import subprocess
from datetime import datetime

TARGETS = ["8.8.8.8", "1.1.1.1", "google.com"]
CHECK_INTERVAL = 30

def ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', '-W', '2', host], 
                              capture_output=True, text=True, timeout=3)
        return result.returncode == 0
    except:
        return False

def check_port(host, port=80):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    print("📡 NetWatch Started")
    
    while True:
        print(f"\n[{datetime.now()}] Checking targets...")
        for target in TARGETS:
            status = "✓ UP" if ping(target) else "✗ DOWN"
            print(f"  {target}: {status}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()