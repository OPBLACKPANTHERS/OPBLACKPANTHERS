from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, blackpantherversion
from pathlib import Path
import asyncio
import telethon.utils

BLACKPANTHER_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/e97d640332ce5eadb3f89.mp4"

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting BlackPantherBot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("BlackPantherBot Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""BLACKPANTHERBOT IS ON!!! BLACKPANTHERBOT VERSION :- {blackpantherversion} YOUR ππΈπ½ππΈπΉππ IS READY TO USE! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @BlackPantherBot_Support .""")
async def blackpanther_is_on():
    try:
        if Config.BLACKPANTHERBOT_LOGGER != 0:
            await bot.send_file(
                Config.BLACKPANTHERBOT_LOGGER,
                BLACKPANTHER_PIC,
                caption=f"ΰΌΚΙΙ’ΙΥΌΙaΚΚ α΄? α΄α΄?Ιͺα΄Κα΄α΄ΰΌ\n\n**ππ΄πππΈπΎπ½ βͺ {blackpantherversion}**\n\nππ²π©π `.ping` or `.alive` π­π¨ ππ‘πππ€! \n\nπΉπΎπΈπ½ [πΌπ°π΅πΈπ°π±πΎπ π²π·π°π](t.me/BLACKPANTHERBOT_CHIT_CHAT) ππΎ πππ΄ππ & πΉπΎπΈπ½ [πΌπ°π΅πΈπ° ππΏπ³π°ππ΄π](t.me/BlackPantherBot_Support) ππΎ πΊπ½πΎπ ππ΄πΆππ°π³πΈπ½πΆ ππΏπ³π°ππ΄ π°π½π³ π½π΄ππ π°π±πΎππ πΌπ°π΅πΈπ°π±πΎπ",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(blackpanther_is_on())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
