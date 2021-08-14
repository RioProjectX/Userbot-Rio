import requests

from userbot import CMD_HELP
from userbot.events import register


@register(pattern=r"^\.asupan$", outgoing=True)
async def _(event):
    lol = await event.edit("`Processing...`")
    try:
        response = requests.get("https://tede-api.herokuapp.com/api/asupan/ptl").json()
        return await event.client.send_file(event.chat_id, response['url'])
        await lol.delete()
    except Exception:
        await lol.edit("**Tidak bisa menemukan video asupan.**")


@register(pattern=r"^\.wibu$", outgoing=True)
async def _(event):
    lol = await event.edit("`Processing...`")
    try:
        response = requests.get("https://tede-api.herokuapp.com/api/asupan/wibu").json()
        return await event.client.send_file(event.chat_id, response['url'])
        await lol.delete()
    except Exception:
        await lol.edit("**Tidak bisa menemukan video wibu.**")


@register(pattern=r"^\.chika$", outgoing=True)
async def _(event):
    lol = await event.edit("`Processing...`")
    try:
        response = requests.get("https://tede-api.herokuapp.com/api/chika").json()
        return await event.client.send_file(event.chat_id, response['url'])
        await lol.delete()
    except Exception:
        await lol.edit("**Tidak bisa menemukan video chikakiku.**")


CMD_HELP.update(
    {
        "asupan": "**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `.asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `.wibu`\
        \n  •  **Function : **Untuk Mengirim video wibu secara random.\
        \n\n  •  **Syntax :** `.chika`\
        \n  •  **Function : **Untuk Mengirim video chikakiku secara random.\
    "
    }
)
