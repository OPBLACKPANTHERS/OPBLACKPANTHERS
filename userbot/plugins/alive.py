
# Thanks to @D3_krish
# Porting in BlackPantherBot by @DANISH_BABA

import asyncio
import random
from telethon import events, version
from userbot import blackpantherversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ππΈπ½ππΈπΉππ"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

blackpanther = bot.uid

BLACKPANTHER_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/e97d640332ce5eadb3f89.mp4"
pm_caption = "  __**π₯π₯πππππ πππ ππ ππππππ₯π₯**__\n\n"

pm_caption += f"**ββββββββββββββββββββ**\n\n"
pm_caption += (
    f"                 ππππππππ\n  **γπ[{DEFAULTUSER}](tg://user?id={blackpanther})πγ**\n\n"
)
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += f"β£β’β³β  `Telethon:` `{version.__version__}` \n"
pm_caption += f"β£β’β³β  `Version:` `{blackpantherversion}`\n"
pm_caption += f"β£β’β³β  `Sudo:` `{sudou}`\n"
pm_caption += f"β£β’β³β  `Channel:` [α΄α΄ΙͺΙ΄](https://t.me/BlackPantherBot_Support)\n"
pm_caption += f"β£β’β³β  `Creator:` [Himanshu](https://t.me/DANISH_BABA)\n"
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += " [π₯REPOπ₯](https://github.com/BlackPantherBotOP/BlackPantherBot) πΉ [πLicenseπ](https://github.com/BlackPantherBotOP/BlackPantherBot/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, BLACKPANTHER_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
