from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, SUDO_USERS, CMD_HNDLR as hl

from telethon import events
from telethon.tl.functions.channels import LeaveChannelRequest

from pyrogram import enums

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sleavvve(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        if len(e.text) > 7:
            event = await e.reply("✦ ʟᴇᴀᴠɪɴɢ...")
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
                await event.edit(str(e))
        else:
             if e.is_private:
                  alt = f"**✦ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴛʜɪꜱ ʜᴇʀᴇ.**\n\n● {hl}leave ➥ <ᴄʜᴀɴɴᴇʟ/ᴄʜᴀᴛ ɪᴅ> \n● {hl}leave ➥ ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ, ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ."
                  await e.reply(alt)
             else:
                  event = await e.reply("✦ ʟᴇᴀᴠɪɴɢ...")
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(str(e))
                    
