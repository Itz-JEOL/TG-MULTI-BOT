import pyrogram, asyncio, random, time, os
from pyrogram import Client, filters
from helper.fsub import ForceSub 
from pyrogram.types import *
from helper.add_new import add_user
from variables import PICS, ADMIN
from plugins.utils.http import get
from plugins import txt

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return 
    await add_user(bot, message)               
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=txt.STAT.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🍁 ꜱᴜᴩᴩᴏʀᴛ", url="https://t.me/BETA_SUPPORT"),
            InlineKeyboardButton("📯 ᴜᴩᴅᴀᴛᴇꜱ", url="https://t.me/Beta_BoTZ")
            ],[            
            InlineKeyboardButton("ℹ️ ʜᴇʟᴩ", callback_data="help"),
            InlineKeyboardButton("📡 ᴀʙᴏᴜᴛ", callback_data="about")
            ],[
            InlineKeyboardButton("❤️‍🔥 ᴅᴇᴠᴇʟᴏᴩᴇʀꜱ ❤️‍🔥", callback_data="source")   
            ]]
            )
        )
       
                                              
@Client.on_message(filters.command(["id", "info"]))
async def media_info(bot, m): 
    FSub = await ForceSub(bot, m)
    if FSub == 400:
        return
    message = m
    ff = m.from_user
    md = m.reply_to_message
    if md:
       try:
          if md.photo:
              await m.reply_text(text=f"**your photo id is **\n\n`{md.photo.file_id}`") 
          if md.sticker:
              await m.reply_text(text=f"**your sticker id is **\n\n`{md.sticker.file_id}`")
          if md.video:
              await m.reply_text(text=f"**your video id is **\n\n`{md.video.file_id}`")
          if md.document:
              await m.reply_text(text=f"**your document id is **\n\n`{md.document.file_id}`")
          if md.audio:
              await m.reply_text(text=f"**your audio id is **\n\n`{md.audio.file_id}`")
          if md.text:
              await m.reply_text("**hey man please reply with ( photo, video, sticker, documents, etc...) Only media **")  
          else:
              await m.reply_text("[404] Error..🤖")                                                                                      
       except Exception as e:
          print(e)
          await m.reply_text(f"[404] Error {e}")
                                        
    if not md:
        buttons = [[
            InlineKeyboardButton("✨️ Support", url="https://t.me/BETA_SUPPORT"),
            InlineKeyboardButton("📢 Updates", url="https://t.me/Beta_BoTZ")
        ]]       
        await m.reply("please wait....")
        await asyncio.sleep(3)
        if ff.photo:
           user_dp = await bot.download_media(message=ff.photo.big_file_id)
           await m.reply_photo(
               photo=user_dp,
               caption=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode="html",
               disable_notification=True
           )          
           os.remove(user_dp)
        else:  
           await m.reply_text(
               text=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode="html",
               disable_notification=True
           )

@Client.on_message(filters.command("repo"))
async def repo(client, message):
    users = await get("https://api.github.com/repos/jeolpaul/TG-MULTI-BOT/contributors")
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (f"**{count}.** [{user['login']}]({user['html_url']})\n")       
        count += 1
    text = f"""[Github](https://github.com/Jeolpaul/TG-MULTI-BOT) | [Updates](t.me/beta_botz)\n```----------------\n| Contributors |\n----------------```\n{list_of_users}"""
    await client.send_message(chat_id=message.chat.id, text=text, disable_web_page_preview=True)

    
