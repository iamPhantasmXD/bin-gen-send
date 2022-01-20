import os
import telethon
import re
import time
import asyncio
import json
import requests
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import events

SESSION = 'AQBh36xXdWtu3MWAHMKMsosqvk4wX2oD87iwW7e4MrmlD6YTxiOOGkQwRGlmJqE3HRNvnu7Zx0byewlU2U_ney4envSmTMdiZIdgv6S4WV5shg0d4bDsphQFPPWIUXWxsOiUpAfIi3BSo4XWMDrhdpx84LH5b_CQKhl4rsjLEIm0EQWm9HaKZsasSc2tItJT9J3EPuFwikNQeTNdXe89Ds74rtAeM5Orp_wguIx4ALcuJSypg6oIcTs7OMt8LbBqaBzfzzV9D3PMGiF6uivfi5tK2-1ZfhgpWvo1V9_9dkDWV02PbPtnGyoWWljr4kqTtOvHpDndhQxc7OR3SIF2xbS9AAAAASuuk5sA'
API_ID = '18261436'
API_HASH = '3889e30c185133e374bbf2eebacdb85a'
LOG_GROUP = -602987124


bot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
bot.start()

def get_cc(amount,bin):
    
    req = requests.get(f'https://rezothcc.herokuapp.com/cc.php?bin={bin}&count={amount}&json')
    if json.loads(req.content)["ok"]:
        return json.loads(req.content)["data"]

@bot.on(events.NewMessage(pattern='/go'))
async def runner(event):
    bin = 429617
    l_bin = 502000
    
    while bin <= l_bin:
        #print(bin)   
        t = get_cc(1,bin)
        for card in t:
            #print(card)
            final_card = f'''/chk {card}
{bin}'''
            await bot.send_message(LOG_GROUP, final_card)
            bin = bin + 1
            time.sleep(20)
    mention = '@Phantasm_XD'
    await bot.send_message(LOG_GROUP, mention)

bot.run_until_disconnected()
