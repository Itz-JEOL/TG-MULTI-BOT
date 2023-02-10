import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import *
from telegraph import upload_file


@Client.on_message(filters.command("telegraph") & filters.private)
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        return await update.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 𝟻𝙼𝙱.")
    if not ( replied.photo or replied.video ):
        return await update.reply_text("please reply with valid media file")
    text = await update.reply_text("<code>Downloading to My Server ...</code>", disable_web_page_preview=True)   
    media = await replied.download()   
    await text.edit_text("<code>Downloading Completed. Now I am Uploading to telegra.ph Link ...</code>", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        return await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)          
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"<b>Link :-</b>\n\n<code>https://graph.org{response[0]}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="Open Link", url=f"https://graph.org{response[0]}"),
            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{response[0]}")
            ],[
            InlineKeyboardButton(text="✗ Close ✗", callback_data="close")
            ]]
        )
    )

