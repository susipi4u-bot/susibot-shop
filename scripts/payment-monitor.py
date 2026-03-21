#!/usr/bin/env python3
"""
Crypto Payment Monitor - checks wallets using Etherscan API + Electrum
"""
import requests
from datetime import datetime

# Etherscan API
ETHERSCAN_API_KEY = "2IW9PFGQWDVJFC6ZR6XRCUQNSWEFAPFD9H"

# Wallet Addresses
WALLETS = {
    "ETH": "0x6B332179b0FedD74696A689468aB0ec861b501C",
    "BTC": "bc1q4qf0dj8eh9qylawjrtu90sngap57hq5fjs55vk",
}

LAST_BALANCES = {}

def check_eth_balance(address):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if data.get("status") == "1":
            return int(data["result"]) / 1e18
    except: pass
    return None

def check_btc():
    """Check BTC via blockchain.info"""
    addr = WALLETS["BTC"]
    try:
        url = f"https://blockchain.info/q/addressbalance/{addr}"
        resp = requests.get(url, timeout=10)
        satoshis = int(resp.text)
        return satoshis / 1e8
    except: pass
    return None

def main():
    print(f"[{datetime.now()}] 🔍 Checking payments...")
    
    new_payments = []
    
    # ETH
    balance = check_eth_balance(WALLETS["ETH"])
    if balance:
        print(f"ETH: {balance:.6f}")
        old = LAST_BALANCES.get("ETH", 0)
        if balance > old:
            print(f"💰 NEUE ZAHLUNG: {balance - old} ETH!")
            new_payments.append(f"ETH: {balance - old}")
        LAST_BALANCES["ETH"] = balance
    
    # BTC
    btc = check_btc()
    if btc:
        print(f"BTC: {btc:.8f}")
        old = LAST_BALANCES.get("BTC", 0)
        if btc > old:
            print(f"💰 NEUE ZAHLUNG: {btc - old} BTC!")
            new_payments.append(f"BTC: {btc - old}")
        LAST_BALANCES["BTC"] = btc
    
    if not new_payments:
        print("Keine neuen Zahlungen")

if __name__ == "__main__":
    main()
