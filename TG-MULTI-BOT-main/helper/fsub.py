import asyncio
from variables import FORCE_SUB
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, event: Message):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(FORCE_SUB) if FORCE_SUB.startswith("-100") else FORCE_SUB))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Unable to do Force Subscribe to {FORCE_SUB}\n\nError: {err}\n\nContact Support Group: https://t.me/BETA_SUPPORT")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(FORCE_SUB) if FORCE_SUB.startswith("-100") else FORCE_SUB), user_id=event.from_user.id)
        if user.status == "banned":
            await bot.send_message(
                chat_id=event.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/BETA_SUPPORT).",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=event.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await bot.send_message(
            chat_id=event.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                ]]                
            ),
            parse_mode="markdown",
            reply_to_message_id=event.message_id
        )
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}\n\nContact Support Group: @BETA_SUPPORT")
        return 200
