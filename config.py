

import logging

from telethon import TelegramClient

from os import getenv
from SACHIN.data import SAPNA


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
BOT_TOKEN0 = getenv("BOT_TOKEN0", default="6761879056:AAHkWE1f8gfrI3cPKGKK5cC2YM_BC6vHDzA")
BOT_TOKEN1 = getenv("BOT_TOKEN1", default="7411670289:AAFmfvCFTdHh8e3lseciDtwPIS7d52CcBuM")
BOT_TOKEN2 = getenv("BOT_TOKEN2", default="6828317510:AAHjnL2RVxJcLNS9uiMrxNSxiJ_F4bH4CbU")
BOT_TOKEN3 = getenv("BOT_TOKEN3", default="7093337277:AAGsUqzZRyAIgEtG_PwPen_ZRpFFWPiP62c")
BOT_TOKEN4 = getenv("BOT_TOKEN4", default="6940349431:AAEfcSRCYx9I-vBk8gIqwbmtDBzNI0G_17A")
BOT_TOKEN5 = getenv("BOT_TOKEN5", default="6821867438:AAHV-Y8QeEVO7i2o1fvRW5VOxrJpK0EScvY")
BOT_TOKEN6 = getenv("BOT_TOKEN6", default="6495030968:AAF4RS-E-10Twg-f4f4fN2M8K0-rrYpenVM")
BOT_TOKEN7 = getenv("BOT_TOKEN7", default="6816073538:AAE3wOcPC8wQJMMqunI8F1GEFl2WAFPN5Q0")
BOT_TOKEN8 = getenv("BOT_TOKEN8", default="7246724288:AAEb7L8lwvsmD0rb7n7TF1X50cAoe6oQD5c")
BOT_TOKEN9 = getenv("BOT_TOKEN9", default="7063268907:AAER728IwjbgTdGwWqk-eKeRDdTZOZxxDFU")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5959548791").split()))
for x in SAPNA:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="5959548791"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

SACHIN0 = TelegramClient('SACHIN0', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN1 = TelegramClient('SACHIN1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN2 = TelegramClient('SACHIN2', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN3 = TelegramClient('SACHIN3', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN4 = TelegramClient('SACHIN4', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN5 = TelegramClient('SACHIN5', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN6 = TelegramClient('SACHIN6', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN7 = TelegramClient('SACHIN7', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN8 = TelegramClient('SACHIN8', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
SACHIN9 = TelegramClient('SACHIN9', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
