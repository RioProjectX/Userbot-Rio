import requests

from userbot import CMD_HELP
from userbot.events import register


@register(pattern=r"^\.asupan$", outgoing=True)
async def _(event):
    await event.edit("`Processing...`")
    response = requests.get("https://tede-api.herokuapp.com/api/asupan/ptl").json()
    if not response:
        await event.edit("**Tidak bisa menemukan video asupan.**")
        return
    await event.client.send_file(event.chat_id, response['url'])
    await event.delete()


@register(pattern=r"^\.wibu$", outgoing=True)
async def _(event):
    await event.edit("`Processing...`")
    response = requests.get("https://tede-api.herokuapp.com/api/asupan/wibu").json()
    if not response:
        await event.edit("**Tidak bisa menemukan video wibu.**")
        return
    await event.client.send_file(event.chat_id, response['url'])
    await event.delete()


@register(pattern=r"^\.chika$", outgoing=True)
async def _(event):
    await event.edit("`Processing...`")
    response = requests.get("https://tede-api.herokuapp.com/api/chika").json()
    if not response:
        await event.edit("**Tidak bisa menemukan video chikakiku.**")
        return
    await event.client.send_file(event.chat_id, response['url'])
    await event.delete()


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
