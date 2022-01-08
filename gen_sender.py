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

SESSION = '1BVtsOJEBu1VguGFMLAhCTt-jP_MEDqy_CwXGFRbLOyrqYxcBUjh-nLk6avtgUCdhmlm57bPaYieajHDTSevFFKsuksOA9ASP0oswDu0cmzCQelPL4ZiPdo8i1XkSRuNeYms4euT-qNDKCeXT_QVO64Kdt-Y5MwYpFyWP4I9r0amjGzwnlDdAiX4cqT6Jj4YpUZtFFLr5p0t0nEdyEcqt-82VQKXK7oibQArjw5Hqsd6sIZVTFXI0Ag-pDS8_nIZ4mGdCtiNGReTeqC0Vn1ecF44beb0siQ0oy799rxS6PYtPeaGvVvDmuwbcA0ekFcdCldUIGBIZDX9fg5fvQEeV-TtsXAl50p8='
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
    bin = 500962
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
