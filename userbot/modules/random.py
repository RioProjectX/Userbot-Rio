# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register


@register(
    outgoing=True,
    pattern=r"^\.r(neko|feet|yuri|trap|futanari|hololewd|lewdkemo)?(.*)"
)
async def _(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(2)
    chat = "@tdtapibot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/{text}")
            response = await conv.get_response()
            file = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @tdtapibot **Dan Coba Lagi!**"
            )
            return
        await event.client.send_file(
            event.chat_id,
            file
        )
        await event.client.delete_messages(
            conv.chat_id, [msg.id, response.id, file.id]
        )
        await event.delete()


CMD_HELP.update(
    {
        "lewd": "**Plugin : **`lewd`\
        \n\n  •  **Syntax :** `.r neko` <text>\
        \n  •  **Function : **idk\
    "
    }
)
