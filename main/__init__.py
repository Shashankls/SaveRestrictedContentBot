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
SESSION = config("SESSION","BQHAnfYAVj1B5AmesL3dnL6T-7z5yp2OWOFKqvEMnA58GyKQLmN451esbxmMR_3cl8GIQKG8tPtDAQy4sLd_NU_eTdsnyTALJCvN8hhXhS-iYPmyIKbLkYzMGa38I70-a6dGsITR0h6MDwYagG0zn0APj7YBDefrzHPFEh180zcMnQFYhnWoW_syB5EtKuOuRH8jaHh71Qa5DtESz8vv8jNhbplurEH184leVZtVz6Oc4xI6M9jUgx0XQuZv-xKs-Z_do5ZC399t21244Sku2UXNq7qrqRsbKD-6006zqpCXpyQXWZQHnqXFzkU1bGIUtHmJo9SklfDn2kMCYdv4WAXcU_QxDwAAAAFqqEy_AA")

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
