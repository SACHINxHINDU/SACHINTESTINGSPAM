import asyncio

from random import choice

from telethon import events
from pyrogram import enums

from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from SACHIN.data import RAID, REPLYRAID, SAPNA, MRAID, SRAID, CRAID, SAPNA

REPLY_RAID = []


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in SAPNA:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ xsᴘᴀᴍ'ꜱ ᴏᴡɴᴇʀ.")
            elif uid == OWNER_ID:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif uid in SUDO_USERS:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"❖ {username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐑𝐚𝐢𝐝 ➥ {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


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
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in SAPNA:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ xsᴘᴀᴍ'ꜱ ᴏᴡɴᴇʀ.")
            elif user_id == OWNER_ID:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif user_id in SUDO_USERS:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("✦ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")
        except NameError:
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝 ➥ {hl}rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("✦ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")
        except NameError:
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝 ➥ {hl}drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def mraid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(MRAID)
                caption = f"❖ {username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝗠𝗥𝗮𝗶𝗱 ➥ {hl}mraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}mraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def sraid(e):
     if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(SRAID)
                caption = f"❖ {username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝗦𝗥𝗮𝗶𝗱 ➥ {hl}sraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}sraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def craid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in SAPNA:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ xsᴘᴀᴍ'ꜱ ᴏᴡɴᴇʀ.")
            elif uid == OWNER_ID:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif uid in SUDO_USERS:
                await e.reply("✦ ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(CRAID)
                    caption = f"❖ {username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐂𝗥𝗮𝗶𝗱 ➥ {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)
      
