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
SESSION = config("SESSION","BQHAnfYAkiOqEsHqbwH1ALpmLGUWOU99D93AFr7DhS_5GePPGtMzyvmIWIY2uk9hH5BmtHo0HSWka3pSSdZ37HOvfDAf1ADtMxNOwIAdIsK3S7GG85T_szbcqCRJO9JDvQlsmT-V3DN5wMtb6bUfvsuIJ6x6j3H9-n5gp1NMyvVEyjDpLTHU6-7JIyfuZmv22_4jmUCiqBzrlIpszDo9PPJ5zUqdM0hWb6_RGjxCMXCNx4ceMGvsvAM7LQ8EDy9DO5g-PV5OiymHRiXENPyHulHKWi1epU8or6Vm62PPW8A7bvN_y_A9YPfwxiAg3-3xYixsRQ7tr6pz7rZ74bCST5rskg-GlQAAAAFqqEy_AA")

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
