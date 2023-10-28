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
SESSION = config("SESSION","BQHAnfYAIUwRE9hScRtYOnpN-slz5kXTtLV57Bs_hTwpBlkJ-KDxbmw_xfXvSB5oM-8Iq4Ju7iH0OWgkNkl7FQ7wigd4HjnWdCzTRB9orDS7YpJtm2GS8AiF80dgLgRIoXG-kpPOqcF3nxymKtetFmnkBig1l9RjAYd771ObCzgb7EcwsBt9CxnBaheqYQwRz60yGLVysvy2Qh0rYGI45JtcETUghvcCHj_7CX1ncuKRghaVaGK2BKQlwF-iu1se7VhxgK7N2JxpUfy5lTBcoFF71sQh2bNfTlc47rBxV1aoQ-L4i4k4Mak0WG26JJYOTt9fLUDKUYTe4hTvc84k48UUvihI1wAAAAFqqEy_AA")

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
