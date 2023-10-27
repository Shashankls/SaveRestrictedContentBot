#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID","29400566")
API_HASH = config("API_HASH", "8fd30dc496aea7c14cf675f59b74ec6f")
AUTH = config("AUTH","6084381887")
FORCESUB = config("FORCESUB","ndkkkknm")
BOT_TOKEN = config("BOT_TOKEN","6653186136:AAElR4rlBQi5JrIdltqvHLpPc8y1MmMeh10")
SESSION = config("SESSION","BQHAnfYAOwvL2Q9e3JKxHdfKinsy2imimDYWePZUQ9QqhT11pmMxEkz0qQlJxfyKZPhrYK-E3-_YzTiKpwCffFH_UsvP3rN6dfoEeF6vR1-M2e9yCMvFLZE1t5pPYVwAOgei7ePLKR3nlz8PFAfmM8qKLllsrWMctg0H0d7FLS_D6j2IV41hlsgTOw6iK6aS5XliBQhRRZqvipo07uiRrcOQpF_BfrQ-LUH5dnOq5JTMs77iJeJRhNVUW3sBU10WV7pT9MvNSZsD-__X1LKlbEWwjkeLLYAXm0wnt1oz4vC9BHi1Cns0u8g6VCKy5DnZTD-EgT-mBa9ZbRJKjK_S74dlRA6oxAAAAAFqqEy_AA")

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
