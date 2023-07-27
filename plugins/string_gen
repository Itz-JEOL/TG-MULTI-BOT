from pyromod import listen
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery  
from asyncio.exceptions import TimeoutError
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

ERROR_MESSAGE = "Oops! An exception occurred! \n\n**Error** : {}"
           



@Client.on_message(filters.private & filters.command('generate'))
async def main(_, msg):
    await msg.reply(
        "Please choose the python library you want to generate string session for",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Pyrogram", callback_data="pyrogram"),
            InlineKeyboardButton("Telethon", callback_data="telethon")
        ]])
    )


async def generate_session(bot, msg, telethon=False):
    await msg.reply("Starting {} Session Generation...".format("Telethon" if telethon else "Pyrogram"))
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'Please send your `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('Not a valid API_ID (which must be an integer). Please start generating session again.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'Please send your `API_HASH`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    api_hash = api_hash_msg.text
    phone_number_msg = await bot.ask(user_id, 'Now please send your `PHONE_NUMBER` along with the country code. \nExample : `+917936482542`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("Sending OTP...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(":memory:", api_id, api_hash)
    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('`API_ID` and `API_HASH` combination is invalid. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('`PHONE_NUMBER` is invalid. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = await bot.ask(user_id, "Please check for an OTP in official telegram account. If you got it, send OTP here after reading the below format. \nIf OTP is in the form ~ `12345`, **please send it as** `1 2 3 4 5`.", filters=filters.text, timeout=600)
        if await cancelled(api_id_msg):
            return
    except TimeoutError:
        await msg.reply('Time limit reached of 10 minutes. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, phone_code, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply('OTP is invalid. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply('OTP is expired. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(user_id, 'Your account has enabled two-step verification. Please provide the password.', filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply('Time limit reached of 5 minutes. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        try:
            password = two_step_msg.text
            if telethon:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
            if await cancelled(api_id_msg):
                return
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply('Invalid Password Provided. Please start generating session again.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
    if telethon:
        string_session = client.session.save()
        try:
            await client.send_message("me", "**{} - STRING SESSION** \n\n`{}`\n\n• __Dont Share String Session With Anyone__\n• __Dont Invite Anyone To Heroku__".format("TELETHON" if telethon else "PYROGRAM", string_session))
        except KeyError:
            pass
        try:
            await client(JoinChannelRequest("@LegendBot_AI"))
        except BaseException:
            pass
        try:
            await client(LeaveChannelRequest("@Legend_Userbot"))
        except BaseException:
            pass
        try:
            await client(LeaveChannelRequest("@Official_LegendBot"))
        except BaseException:
            pass
    else:
        string_session = await client.export_session_string()
        try:
            await client.send_message("me", "**{} ~ STRING SESSION** \n\n`{}` \n\n• __Dont Share String Session With Anyone__\n• __Dont Invite Anyone To Heroku__".format("TELETHON" if telethon else "PYROGRAM", string_session))
        except KeyError:
            pass
    await client.disconnect()
    await phone_code_msg.reply("Successfully String  Session Has Been Generated {} \n\nPlease check your saved messages!".format("TELETHON" if telethon else "PYROGRAM"), reply_markup=InlineKeyboardMarkup(Data.support_button))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Cancelled the Process!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Restarted the Bot!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Cancelled the generation process!", quote=True)
        return True
    else:
        return False
    
    
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="hy",
            )
    elif query == "generate":
        await callback_query.message.reply(
            "Please choose the python library you want to generate string session for",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Pyrogram", callback_data="pyrogram"),
                InlineKeyboardButton("Telethon", callback_data="telethon")
            ]])
        )
    elif query in ["pyrogram", "telethon"]:
        await callback_query.answer()
        try:
            if query == "pyrogram":
                await generate_session(bot, callback_query.message)
            else:
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
