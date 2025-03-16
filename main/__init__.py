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
SESSION = "BQGOk7oAcpTtSbnDkyX-B6GDaOs9CDQEQ7oO5PqjsF8s6Iieqj1bKsZW68L69JbOVyTNSoQiOEp4M023sfwK-wylbN1Tj20EOlOPLzxrQXbRUn2df-tYzlz1JqzgAShpaX9QsUxUWxkLZYbnYP536B-XQ5M54N8WMYlhz1XqVLzR30ObYfXQOklCxFMXRXVuZsJHDR0iJB0dToOWLgpA9jn-BrvnIuvIG95cOEZWlFbCs02GutNwM-CPT7rU5SaWRCjTRpWFWBXp5qx0CIa4bvs1cgD_JYcWbtPSDXP1smYAN2Ayg07FDealj9FdLA38kYnu8F2qI26H419x3gR8BXaB0uqQYgAAAAHja0KYAA "
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
