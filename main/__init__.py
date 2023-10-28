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
SESSION = config("SESSION","BQD9oGAAgSl66jS7NNBl70W7tOXsaQ-QHx-f07aHM9yO90_u4GUZK700lygudUncNgv4NTWZAtB4kXKRg2iPF99PlV6DzxxNllrcQJ0Sb_lHmzleIovj1rQ_MKQRTV5KR5i6a3_vbR56LwiduYI55SkFm2SuHjjqjUHBuM08jZyYb-XNer592IgbHme59kaUngpMXh-gX6yUCladSSH5tvPqwXvk1sUSh_n2V4OmRsjLgaLk2yNb0H5ZG9IxgubH6PddX3jZI5R3P2xOsbzPiBSz50jpIKRmOieAd7SAwOt_TetQmTFj-7RQoaVynkNT_dnB-waX36PjyqV4NoTsWWClraDjcgAAAAGCvE3CAA")

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
