from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client
from helper.fsub import ForceSub
from plugins.utils.functions import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()


@Client.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    FSub = await ForceSub(_, message)
    if FSub == 400:
        return
    if not message.reply_to_message:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    user_id = message.from_user.id
    m = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ..")
    await message.reply_photo(
        photo=carbon,
        caption="**MADE WITH ❤️ BY >JEOL**",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("JOIN CHANNEL", url="https://t.me/beta_boTZ")                  
            ]]
        )
    )
    await m.delete()
    carbon.close()
