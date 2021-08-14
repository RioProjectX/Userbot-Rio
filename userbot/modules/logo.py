# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.logo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Give a name too!`")
    else:
        p = await event.edit("`Processing`")
    chat = "@tdtapibot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message(f"/logo {text}")
            r = await conv.get_response()
            details = await conv.get_response()
            logo = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await p.edit(
                "**Error: Mohon Buka Blokir** @tdtapibot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(1)
        await p.edit("`Done!`")
        await bot.send_file(event.chat_id, logo)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, r.id, details.id, logo.id]
        )
        await event.delete()


CMD_HELP.update(
    {
        "logo": "**Plugin : **`logo`\
        \n\n  •  **Syntax :** `.logo` <text>\
        \n  •  **Function : **Membuat logo dari Teks yang diberikan\
    "
    }
)
