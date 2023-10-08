#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID","16621664")
API_HASH = config("API_HASH", "8b283f2943729318995738b5963f0bcc")
BOT_TOKEN = config("BOT_TOKEN","6525864792:AAHoeiRNOQmdRD4GFyRo4Ht0vZtccEOWk10")
SESSION = config("SESSION","BQAmu0kIAT0Mp5sgBqoZjz-tAitArne5i42mSGQOVENlZ7yZLGYTeimX2E309DmqTm85UbBmieOnOqCxfLL0rM1gwviLTRCKon6tP5exOUC3bUSofedfxl2bi-6lOnj3pVBjnasyD39tRixGa1YR-khIA3rcY1njugoeLMavf8SCmlI95c9da0ibzIiyV1rfPcNos40xIomH4CubpWdUGXrv2GXN5ChnNMpQ5biHYcODpdpIX0G1kPSM3A4BHlS8O9qVinBGV_-e01F6excrMnb9Fo1PO_MtODDIGSIQAw7IRe5nL5Qwqan30Sw7ydDVSgm4oVxf9GYlXuhoMmyO_rDXAAAAAYcb09AA")
FORCESUB = config("FORCESUB","-1001845208748",cast=int)
AUTH = config("AUTH","6561715152")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
