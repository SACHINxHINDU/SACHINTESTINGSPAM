from telethon import __version__, events, Button

from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9


START_BUTTON = [
    [
        Button.url("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", "https://t.me/avishaxbot?startgroup=true")
    ],
    [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/the_friendz"),
        Button.url("ʀᴇᴘᴏ", "https://github.com/tinaarobot/XSPAM")
    ],
    [
        Button.inline("ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", data="help_back")
    ]
]

@SACHIN0.on(events.NewMessage(pattern="/start"))
@SACHIN1.on(events.NewMessage(pattern="/start"))
@SACHIN2.on(events.NewMessage(pattern="/start"))
@SACHIN3.on(events.NewMessage(pattern="/start"))
@SACHIN4.on(events.NewMessage(pattern="/start"))
@SACHIN5.on(events.NewMessage(pattern="/start"))
@SACHIN6.on(events.NewMessage(pattern="/start"))
@SACHIN7.on(events.NewMessage(pattern="/start"))
@SACHIN8.on(events.NewMessage(pattern="/start"))
@SACHIN9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        Altbot = await event.client.get_me()
        bot_name = Altbot.first_name
        bot_id = Altbot.id
        TEXT = f"**❖ ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ.\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n● ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id}) ʙᴏᴛ.**\n\n"
        TEXT += f"● **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ ➥** `M3.9/V8`\n"
        TEXT += f"● **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥** `3.11.8`\n"
        TEXT += f"● **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥** `{__version__}`\n\n"
        TEXT += f"❖ **ᴛʜɪs ɪs ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ xsᴘᴀᴍ ʙᴏᴛ ғᴏʀ ɴᴏɴ sᴛᴏᴘ sᴘᴀᴍᴍɪɴɢ.**"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/9d0cc6a4aaa021b546323.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
      )
