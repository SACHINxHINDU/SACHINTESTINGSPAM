from telethon import __version__, events, Button

from config import SACHIN0, SACHIN1, SACHIN2, SACHIN3, SACHIN4, SACHIN5, SACHIN6, SACHIN7, SACHIN8, SACHIN9


START_OP = [
    [
        Button.url("🍁 sᴀᴄʜɪɴ", "https://t.me/V_VIP_OWNER"),
        Button.url("ᴜsᴇʀʙᴏᴛ 🕸️", "https://t.me/SANATANI_X_ROBOT")
    ],
    [
        Button.inline("🥀 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 🥀", data="help_back")
    ],
    [
        Button.url("✨ ᴜᴘᴅᴀᴛᴇ", "https://t.me/All_SANATANI_BOT"),
        Button.url("sᴜᴘᴘᴏʀᴛ ❄️", "https://t.me/+Ckzm2ypQyIIzZTll")
    ],
    [
        Button.url("🌸 ᴊᴏɪɴ ғᴏʀ sᴜᴅᴏ 🌸", "https://t.me/+Ckzm2ypQyIIzZTll")
    ],
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
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        TEXT = f"**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤͟͟͞͞‌‌‌‌★**\n**┆**\n**┊◍ ʜᴇʏ : [{event.sender.first_name}] **\n**┆◍ ɪ ᴀᴍ : [{bot_name}](tg://user?id={bot_id}) **\n**┊**\n**┆● sᴀɴᴀᴛᴀɴɪ ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `0.2`\n**┊● ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `8.2.5.1.01`\n**╰─────────────────────────**\n**──────────────────────────**\n**⦿ Oᴡɴᴇʀ - [🦋⃟‌🇸ʌᷟᴄᷣʜɪ֟፝η 🌸](https://t.me/v_vip_owner) | [🦋⃟‌🇸ʌᷟᴄᷣʜɪ֟፝η 🌸](https://t.me/sachin_owner) **\n**──────────────────────────**\n**    ❖ Uᴘᴅᴀᴛᴇ's ⏤͟͟͞͞‌‌‌‌ [❖ ∣ Sᴀɴᴀᴛᴀɴɪ Tᴇᴄʜ ∣ ❖](https://t.me/all_sanatani_bot) **\n**──────────────────────────**"
        await event.client.send_file(
                    event.chat_id,  
                    "https://telegra.ph//file/7cfeff721589b61a2f634.jpg",
                    caption=TEXT, 
                    buttons=START_OP
                )
