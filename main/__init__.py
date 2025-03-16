#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 4857766
API_HASH = "6c3c6facf5598a4b318e138f8c407028"
BOT_TOKEN = "7038431984:AAFHdIhCf33k-eGhgTDWyM1uuC0gd7ywS9M"
SESSION = "BQFTZuMAo_EtgtYPpUclUSUjSCOcghhn0kRo4YUMswdUf3_LrgYuuIKfAIQUH94liIw9j2FwI2t7iu8fbqJTemrtAHEwBHCQw7IGbyc3iD_K-UTN21ZEkm5KGFsCGcc6aNbjPSiLkugGkrD9h_FX81AwBhM_itGs1mwl5IlxPzSkcfttPWngJtJ4L5aUqms9cKUy4S76_9cK9niojlUNYCUOWBurY2l-QOCzf27_wOPboNQ_UA_ZWojmy6a8NMNBiOsNWnKzg83PWn38KjELNHhoNmarcngiyiqFdXNQifyBCyt-FdaXeCjHuJuYG5D6xR-QcVSW3BEozFm0lXs6XHRmASigAAAAA5g3ELAA"
FORCESUB = "SharkToonsIndia"
AUTH = 6066102279

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
