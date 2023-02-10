from pyrogram import Client, filters, enums
from pyrogram.errors import UserNotParticipant 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from variables import FORCE_SUB


async def not_subscribed(_, c, m):
   if not c.force_channel:
      return False
   try:             
      user = await c.get_chat_member(c.force_channel, m.from_user.id)
   except UserNotParticipant:
      pass
   else:
      if user.status != enums.ChatMemberStatus.BANNED:                       
         return False 
   return True



@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="🤖 Join Our Channel", url=f"https://t.me/{FORCE_SUB}") ]]                 
    text = "**sorry dude you're not joined my channel. So please join our channel to continue**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
