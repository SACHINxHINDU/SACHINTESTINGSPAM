import sys
import heroku3

from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from pyrogram import enums
from os import execl, getenv
from telethon import events
from datetime import datetime


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sisping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        start = datetime.now()
        altron = await e.reply(f"🐙")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"✦ ᴘɪɴɢ sᴛᴀᴛs ⏤͟͟͞͞★\n➥ `{mp} ᴍꜱ`")


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"✦ `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
        try:
            await SACHIN0.disconnect()
        except Exception:
            pass
        try:
            await SACHIN1.disconnect()
        except Exception:
            pass
        try:
            await SACHIN2.disconnect()
        except Exception:
            pass
        try:
            await SACHIN3.disconnect()
        except Exception:
            pass
        try:
            await SACHIN4.disconnect()
        except Exception:
            pass
        try:
            await SACHIN5.disconnect()
        except Exception:
            pass
        try:
            await SACHIN6.disconnect()
        except Exception:
            pass
        try:
            await SACHIN7.disconnect()
        except Exception:
            pass
        try:
            await SACHIN8.disconnect()
        except Exception:
            pass
        try:
            await SACHIN9.disconnect()
        except Exception:
            pass
        
        execl(sys.executable, sys.executable, *sys.argv)

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"✦ ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("✦ `[HEROKU] ➥" "\n✦ Please Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")
            return

        if str(target) in sudousers:
            await ok.edit(f"✦ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ** ➥ `{target}`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
      
