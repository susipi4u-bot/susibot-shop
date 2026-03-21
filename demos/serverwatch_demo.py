#!/usr/bin/env python3
import psutil, platform
from datetime import datetime

print("🖥️ SERVERWATCH - System Monitoring")
print("=" * 50)
print(f"Hostname:    {platform.node()}")
print(f"OS:          {platform.system()} {platform.release()}")
print(f"Uptime:      {psutil.boot_time() / 86400:.1f} days")
print("-" * 50)
print(f"CPU Load:    {psutil.cpu_percent(interval=1)}%")
print(f"Memory:      {psutil.virtual_memory().percent}%")
print(f"Disk Root:   {psutil.disk_usage('/').percent}%")
print(f"Network:     {psutil.net_io_counters().bytes_sent/1024/1024:.1f} MB sent")
print("-" * 50)
print("Process Count:", len(psutil.pids()))
print("=" * 50)
