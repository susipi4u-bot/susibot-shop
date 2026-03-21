import psutil
import yaml
import time
from datetime import datetime
import os

CONFIG_FILE = "config.yaml"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return yaml.safe_load(f)
    return {"check_interval": 60, "alert_threshold": 90}

def check_cpu():
    return psutil.cpu_percent(interval=1)

def check_memory():
    return psutil.virtual_memory().percent

def check_disk():
    return psutil.disk_usage('/').percent

def check_services():
    services = ["ssh", "nginx", "mysql"]
    status = {}
    for svc in services:
        # Simplified check
        status[svc] = "running"
    return status

def main():
    config = load_config()
    print("🔔 HealthCheck Started")
    print(f"Check Interval: {config['check_interval']}s")
    
    while True:
        cpu = check_cpu()
        mem = check_memory()
        disk = check_disk()
        
        print(f"[{datetime.now()}] CPU: {cpu}% | MEM: {mem}% | DISK: {disk}%")
        
        if cpu > 90 or mem > 90:
            print("⚠️ Alert: High resource usage!")
        
        time.sleep(config['check_interval'])

if __name__ == "__main__":
    main()