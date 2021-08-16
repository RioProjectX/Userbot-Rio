# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


lol = {
    "neko": {
        "cmd": "/neko",
        "help": "idk test aja",
    },
    "feet": {
        "cmd": "/feet",
        "help": "idk test aja",
    },
    "yuri": {
        "cmd": "/yuri",
        "help": "idk test aja",
    },
    "trap": {
        "cmd": "/trap",
        "help": "idk test aja",
    },
    "futanari": {
        "cmd": "/futanari",
        "help": "idk test aja",
    },
    "hololewd": {
        "cmd": "/hololewd",
        "help": "idk test aja",
    },
}


@register(
    outgoing=True,
    pattern=r"^\.r(neko|feet|yuri|trap|futanari|hololewd|lewdkemo)?(.*)"
)
async def _(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    chat = "@tdtapibot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/{text}")
            response = await conv.get_response()
            poto = await conv.get_response()
            """ - don't spam notif - """
            #await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @tdtapibot **Dan Coba Lagi!**"
            )
            return
        await event.client.send_file(
            event.chat_id,
            poto
        )
        #await event.client.delete_messages(
            #conv.chat_id, [msg.id, response.id, logo.id]
        #")
        await event.delete()


CMD_HELP.update(
    {
        "nsfw": "**Plugin : **`nsfw`\
        \n\n  •  **Syntax :** `.r neko`\
        \n  •  **Function : **idk\
    "
    }
)
