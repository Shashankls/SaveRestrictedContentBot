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
SESSION = config("SESSION","BQHAnfYAVfhUxrAuaf9FznfVW6JsQOJAF3mPb_sgNo1rbF0mIq4x6-pOl4V4n6k07rEzviyIdKq_C88BEVj6xBZ-g_yFC-0VGKLeaenNjl7b4E-EzalSRsGM0xsCg3nz7NRScqTz8Ef1sqDlaylB4r5vtfc0g2X5H91fKslovDrlrI9h8QjxR3GFY90ORvcInqERTVj2OO0FE6qLUUHvY5whs-HEI6U0dLLVMd3hkSdXrUpLAnmgaph7xF2YxYB9x7yB1HP7hl15A_zRMkN602b4ues2OVmL2HUFvtfoFkk5gw6ujjMDHO7t_SZiEgOygeC-xrsKSwBwbyxmFzashFfEyUgLuAAAAAFqqEy_AA")

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
