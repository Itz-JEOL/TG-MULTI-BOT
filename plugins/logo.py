from pyrogram import Client, filters, idle
import pyrogram, asyncio, random, time
from pyrogram.errors import FloodWait
from pyrogram.types import *
import requests


@Client.on_message(filters.command("logo"))
async def logo(bot, msg: Message):
    if len(message.command) == 1:
       return await msg.reply_text("Usage:\n\n /logo Jeol")
    logo_name = msg.text.split(" ", 1)[1]
    await text.delete()
    API = f"https://api.sdbots.tk/logohq?text={logo_name}"
    req = requests.get(API).url
    await msg.reply_photo(
        photo=f"{req}")
