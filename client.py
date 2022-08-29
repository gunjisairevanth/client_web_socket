#!/usr/bin/python

import websockets
import asyncio
import json



async def ftx_btc():
    url = "wss://ftx.com/ws/"
    async with websockets.connect(url) as ws:
        await ws.send(json.dumps({"op": "subscribe", "channel": "trades", "market": "BTC/USD"}))
        while True:
            print(await ws.recv())

async def ftx_eth():
    url = "wss://ftx.com/ws/"
    async with websockets.connect(url) as ws:
        await ws.send(json.dumps({"op": "subscribe", "channel": "trades", "market": "ETH/USD"}))
        while True:
            print(await ws.recv())

async def ftx_matic():
    url = "wss://ftx.com/ws/"
    async with websockets.connect(url) as ws:
        await ws.send(json.dumps({"op": "subscribe", "channel": "trades", "market": "MATIC/USD"}))
        while True:
            print(await ws.recv())

asyncio.get_event_loop().run_until_complete(ftx_btc())
print("Hello")