#!/usr/bin/env python3
import psutil, platform, time
from datetime import datetime

def main():
    print("=" * 40)
    print("🍓 Pi Stats - Raspberry Pi Monitor")
    print("=" * 40)
    print(f"🖥️  Host: {platform.node()}")
    print(f"⏰ Zeit: {datetime.now().strftime('%H:%M:%S')}")
    print(f"📊 CPU:  {psutil.cpu_percent()}%")
    print(f"💾 RAM:  {psutil.virtual_memory().percent}%")
    print(f"💿 Disk: {psutil.disk_usage('/').percent}%")
    
    # CPU temps if available
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            for name, entries in temps.items()[:1]:
                print(f"🌡️  Temp: {entries[0].current}°C")
    except: pass
    
    print("=" * 40)

if __name__ == "__main__":
    main()
