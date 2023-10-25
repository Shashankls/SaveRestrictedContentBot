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
SESSION = config("SESSION","BQHAnfYABKr5ctlNYKgQEJ_VSKA89UPCtmnBJ0Bfl5FenxnonVBJ74ETSYB-r1Ou3DRXLrQvsUcIC4jS4_0980rTWUfop2TawTOHLUmBd5Hkzib7DNeb6jjRTMfSQN630KyzKoWfiAYsRDqpNFh86IEH5WeZ1PIGVMMmvUIDyOaN3owqJ3DvKO8Bu3F1y8RtTvTHWlZEnTKiKG-MCpy9YwX9ihRNOPUbGDAuqCCpLUY4tMeklFDzs0sM-Vtyw31hwqNOec5RS3AvVeQO501jFSxiSGB_vWmlmdqXDBwpkLaifnqOPOofcsg3IsARO5x1lMDsaGbTZCcgl9qh4pYtYEFqx2oDqAAAAAGMj5BYAQ")

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
