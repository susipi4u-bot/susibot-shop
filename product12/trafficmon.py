#!/usr/bin/env python3
"""
TrafficMon - Network Traffic Monitor
Monitor incoming/outgoing traffic on network interfaces
"""
import argparse
import time
import sys

def get_traffic(interface='eth0'):
    """Get traffic stats for interface"""
    try:
        with open(f'/sys/class/net/{interface}/statistics/rx_bytes', 'r') as f:
            rx = int(f.read())
        with open(f'/sys/class/net/{interface}/statistics/tx_bytes', 'r') as f:
            tx = int(f.read())
        return rx, tx
    except:
        return None, None

def format_bytes(b):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if b < 1024:
            return f"{b:.2f} {unit}"
        b /= 1024
    return f"{b:.2f} TB"

def monitor(interface, interval, json_output):
    """Monitor network traffic"""
    rx_prev, tx_prev = get_traffic(interface)
    if rx_prev is None:
        print(f"Error: Interface {interface} not found", file=sys.stderr)
        sys.exit(1)
    
    print(f"Monitoring {interface} (Ctrl+C to stop)")
    
    try:
        while True:
            time.sleep(interval)
            rx, tx = get_traffic(interface)
            
            rx_rate = (rx - rx_prev) / interval
            tx_rate = (tx - tx_prev) / interval
            
            if json_output:
                import json
                print(json.dumps({
                    'rx': rx,
                    'tx': tx,
                    'rx_rate': rx_rate,
                    'tx_rate': tx_rate
                }))
            else:
                print(f"RX: {format_bytes(rx)} | TX: {format_bytes(tx)} | "
                      f"↓ {format_bytes(rx_rate)}/s | ↑ {format_bytes(tx_rate)}/s")
            
            rx_prev, tx_prev = rx, tx
    except KeyboardInterrupt:
        print("\nStopped")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Network Traffic Monitor')
    parser.add_argument('-i', '--interface', default='eth0', help='Network interface')
    parser.add_argument('-t', '--interval', type=float, default=1, help='Update interval in seconds')
    parser.add_argument('-j', '--json', action='store_true', help='JSON output')
    args = parser.parse_args()
    
    monitor(args.interface, args.interval, args.json)