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
SESSION = config("SESSION","BQCbVGdnfzb3xsTWUIPwovDd_HdHPfvtRLa5p1ufaOYBzz8__mw4AFBspLqw9DT4V9g7ycskoPZxC8kI_PRMaCZQfwlg0x0zaA0EqwHXVMgahZeEz3uiTZbiKUi54sSghO7Np4zhG3PBUSY-uikAJDXVOuoIq0PmVEhJHuxJgrJl06pqy9G7_nxLeNkVrE5VCDk9t8MGXShewoB-TA9usn63-fIqnoeY9YZqeFbWvCZ7QEPUmbjQEGZJN67xp1ffCxZnGW9K08e19DG7_kBTPa1Y3i7K6OkRJEwUC6Bx4h8SPZc7Ga0sSJkh3kG-rsKRIIg5GQxzF3p4fCpixj59fzHWAAAAAYcb09AA")
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
