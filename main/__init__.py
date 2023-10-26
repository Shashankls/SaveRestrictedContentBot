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
SESSION = config("SESSION","BQB3RY2Hhx7cxywMOBq66Fpws56L4nOagIsoCqvy5PGoVzFTOhFcXBNtX64k9I--BrLKqqNFFpcuLcIUZ9rK5szQsmWRkEz2GGrfxBAG0BLV3ahTi2ymYVgv2FfdK3USkD6cN0Fw-DlDisNi3GqO0aQSYCPe4HkI7Du3NgC1Tbztg4lQmxp0C5oAPGXN-TqpYTbmtjAEwx3UCYTNt-KIrtK5Edz_lA-zRsqWHhnL8FcLVL0P1c7OL9_CETugZU6PTmAIh6o5YS-lAaHzmScfEjxGuw95Zq26YnoevyGVomCyjRrv4OZKYl_iqR5plPV1KAkKQk7Mi6Bo1uBQNpQhGvQWAAAAAWqoTL8A")

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
