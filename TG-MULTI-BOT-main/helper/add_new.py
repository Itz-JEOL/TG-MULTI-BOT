# Kanged from @AbirHasan2005 uyi❤️‍🔥

from variables import LOG_TEXT, LOG_CHANNEL
from helper.database import db
from pyrogram import Client
from pyrogram.types import Message


async def add_user(bot: Client, msg: Message):
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id)
        if LOG_CHANNEL is not None:            
            await bot.send_message(LOG_CHANNEL, text=LOG_TEXT.format(id=msg.from_user.id, dc_id=msg.from_user.dc_id, first_name=msg.from_user.first_name, username=msg.from_user.username, bot=bot.mention))

                













