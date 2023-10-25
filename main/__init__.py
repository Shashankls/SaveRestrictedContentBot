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
BOT_TOKEN = config("BOT_TOKEN","6653186136:AAElR4rlBQi5JrIdltqvHLpPc8y1MmMeh10")
SESSION = config("SESSION","BQD9oGAARBUv3-ZXsxRja5isNJ1dQIKQmZ9pWDlLWlldOQnT11IFeRds0r0EPjRQ80RDuws7vz9ill7RcuLCEy6PYVcakeywLQTalpekCcI6I1Y8C4F3G8mdD1lWQ3Vbm3IZYdY68W5zbEPWCXr9Gl4Yl9NoqzM6jrzIKXvc855TUiMx83rXAF4mnpbh4C5MaCZpR8ewZluwW_hM7_PsCOIgn_G1A14d6qyUpLFjscTCURJLKRaeKH6ZPgmM1hsY2QbfdU-r7Jt_UfcLe5NwvAPfwysuRF2R3p-x4vLV2XAxCX3lk5gbO9wOCFosaAvldJk885pmrE_-0i3eSo0fPfxc45bn1AAAAAGHG9PQAA")

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
