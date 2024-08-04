import asyncio
import heroku3
from pymongo import MongoClient
from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9, MONGO_DB_URI, SUDO_USERS, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME, CMD_HNDLR as hl
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError
from telethon.tl.custom import Button

# MongoDB configuration
client = MongoClient(MONGO_DB_URI)
db = client['bot_database']
stats_collection = db['stats']

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await legend.reply(
                legend.chat_id,
                "✦ First Set These Vars In Heroku ➥ `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await legend.reply(
                "✦ Make Sure Your Heroku API Key & App Name Are Configured Correctly In Heroku."
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await legend.reply(f"✦ Fetching Logs...")
    
        with open("Sachin.txt", "w") as logfile:
            logfile.write("✦ SANATANI SPAM ⚡ [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await SACHIN0.send_file(legend.chat_id, "Sachin.txt", caption=f"✦ **SANATANI SPAM BOT LOGS** ⚡\n\n● **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ ➥** `{ms} ꜱᴇᴄᴏɴᴅꜱ`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"✦ An Exception Occured, ERROR ➥ {str(e)}")

    elif legend.sender_id in SUDO_USERS:
        await legend.reply("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
                         

@SACHIN0.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN1.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN2.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN3.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN4.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN5.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN6.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN7.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN8.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
@SACHIN9.on(events.NewMessage(incoming=True, pattern=r"\%sbroadcast(?: |$)(.*)" % hl))
async def broadcast(event):
    if event.sender_id == OWNER_ID:
        reply = await event.get_reply_message()
        message = event.pattern_match.group(1)

        if not message and not reply:
            await event.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ.")
            return
        
        users = stats_collection.find({'type': 'user'})
        groups = stats_collection.find({'type': 'group'})

        user_count = 0
        group_count = 0

        for user in users:
            try:
                if reply:
                    await X1.send_message(user['id'], message or reply.text, file=reply.media)
                else:
                    await X1.send_message(user['id'], message)
                user_count += 1
            except ForbiddenError:
                pass  # Ignore if the bot is blocked
            except Exception as e:
                print(f"Error sending message to {user['id']}: {str(e)}")
        
        for group in groups:
            try:
                if reply:
                    await X1.send_message(group['id'], message or reply.text, file=reply.media)
                else:
                    await X1.send_message(group['id'], message)
                group_count += 1
            except ForbiddenError:
                pass  # Ignore if the bot is removed from the group
            except Exception as e:
                print(f"Error sending message to {group['id']}: {str(e)}")
        
        await event.reply(f"ʙʀᴏᴀᴅᴄᴀsᴛ ʜᴀs ʙᴇᴇɴ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.\n\nᴍᴇssᴀɢᴇ sᴇɴᴛ ᴛᴏ {user_count} ᴜsᴇʀs ᴀɴᴅ {group_count} ɢʀᴏᴜᴘs.")
    else:
        await event.reply("ᴏɴʟʏ sᴀɴᴀᴛᴀɴɪ ᴄᴀɴ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ.")
                              
