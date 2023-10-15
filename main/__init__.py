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
SESSION = config("SESSION","BQD9oGAAsR3NogdcIMU1o9z6A6oBtlQaZiH1UAfBbTbZczEi2yI5BWEDf7HpMpp0CZyDOWt3yVBJ7tDWnKOz-uZqQm2agLp2iWhWy9kgsVC71twYuu2DI7DMS_M_6oyyHbU3eGO5y3nhthfbY_savmajkz0eLtbcaWuou5f00LTnWAHyF9Sbc0RAGPUfJRWHc3zhAk3NvdhU6lT-mEY3KIcwEeb869gTP6ZUQCdRZlOTW20uKRml2pRmZpxtxKHAogDLBrtzDeutA8kXC98YkJgEGqsILaeb3kOfCESEDP0PEekCHjlFgtnbr_VKWdMwzNrZDhQoB1o8ZX5P27PRhSHM1BOMTAAAAAGHG9PQAA")
FORCESUB = config("FORCESUB","rhenbsb")
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
