#!/usr/bin/env python3
"""Crypto Payment Monitor - checks ETH, BTC, SOL"""
import requests
from datetime import datetime

ETHERSCAN_API_KEY = "2IW9PFGQWDVJFC6ZR6XRCUQNSWEFAPFD9H"

WALLETS = {
    "ETH": "0x6B332179b0FedD74696A689468aB0ec861b501C",
    "BTC": "bc1q4qf0dj8eh9qylawjrtu90sngap57hq5fjs55vk",
    "SOL": "4ZGDUxWSbHsSuABMEXmjdoprxfqNSeP3Ropy1DucQUo4",
}

LAST_BALANCES = {}

def check_eth():
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={WALLETS['ETH']}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    try:
        data = requests.get(url, timeout=10).json()
        if data.get("status") == "1":
            return int(data["result"]) / 1e18
    except: pass
    return None

def check_btc():
    try:
        url = f"https://blockchain.info/q/addressbalance/{WALLETS['BTC']}"
        return int(requests.get(url, timeout=10).text) / 1e8
    except: pass
    return None

def check_sol():
    try:
        resp = requests.post("https://api.mainnet-beta.solana.com",
            json={"jsonrpc":"2.0","id":1,"method":"getBalance","params":[WALLETS['SOL']]},
            headers={"Content-Type":"application/json"}, timeout=5)
        if resp.status_code == 200:
            return resp.json().get("result",{}).get("value",0) / 1e9
    except: pass
    return None

def main():
    print(f"[{datetime.now()}] 🔍 Payment Check")
    new = []
    
    for name, check_fn in [("ETH", check_eth), ("BTC", check_btc), ("SOL", check_sol)]:
        bal = check_fn()
        if bal:
            print(f"{name}: {bal:.6f}")
            if bal > LAST_BALANCES.get(name, 0):
                new.append(f"{name}: {bal - LAST_BALANCES.get(name, 0)}")
            LAST_BALANCES[name] = bal
    
    if new:
        print("💰 NEUE ZAHLUNGEN:", new)
    else:
        print("Keine neuen Zahlungen")

if __name__ == "__main__":
    main()
