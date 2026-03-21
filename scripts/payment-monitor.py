#!/usr/bin/env python3
"""Crypto Payment Monitor - Full Automatic"""
import requests, json, os
from datetime import datetime

WALLETS = {
    "ETH": "0x6B332179b0FedD74696A689468aB0ec861b501C",
    "BTC": "bc1q4qf0dj8eh9qylawjrtu90sngap57hq5fjs55vk",
    "SOL": "4ZGDUxWSbHsSuABMEXmjdoprxfqNSeP3Ropy1DucQUo4",
}

def get_state():
    f = "/home/susi/.openclaw/workspace/.payment_state"
    return json.load(open(f)) if os.path.exists(f) else {}

def save_state(s):
    json.dump(s, open("/home/susi/.openclaw/workspace/.payment_state", "w"))

def check_eth():
    try:
        r = requests.post("https://eth.public-rpc.com", 
            json={"jsonrpc":"2.0","method":"eth_getBalance","params":[WALLETS["ETH"],"latest"],"id":1}, timeout=10)
        return int(r.json()["result"], 16) / 1e18
    except: return None

def check_btc():
    try:
        r = requests.get(f"https://blockchain.info/q/addressbalance/{WALLETS['BTC']}", timeout=10)
        return int(r.text) / 1e8
    except: return None

def check_sol():
    try:
        r = requests.post("https://api.mainnet-beta.solana.com",
            json={"jsonrpc":"2.0","id":1,"method":"getBalance","params":[WALLETS["SOL"]]}, timeout=5)
        return r.json()["result"]["value"] / 1e9
    except: return None

state = get_state()
new = []
for name, fn in [("ETH",check_eth),("BTC",check_btc),("SOL",check_sol)]:
    b = fn()
    if b: print(f"{name}: {b:.6f}")
    old = state.get(name,0)
    if b and b>old:
        new.append(f"{name}: {b-old}")
        state[name]=b
save_state(state)
if new:
    print("NEUE ZAHLUNG:", new)
    open("/home/susi/.openclaw/workspace/.payment_alert","w").write(f"{datetime.now()}\nZAHLUNG!\n"+"\n".join(new))
else: print("Keine neuen Zahlungen")
