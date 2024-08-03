

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
BOT_TOKEN = getenv("BOT_TOKEN", default=None)


SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6735289775").split()))
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
