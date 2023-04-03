from pyrogram import Client
from variables import *
from aiohttp import web
from route import web_server

class App(Client):

    def __init__(self):
        super().__init__(
            "tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.id = me.id
        self.name = me.first_name
        self.mention = me.mention
        self.username = me.username
        self.force_channel = FORCE_SUB if FORCE_SUB else None        
        print(f'{me.first_name} is Started...🍃')

    async def stop(self, *args):
        await super().stop()      
        print("Bot restarting.....")
        
                           
  
bot = App()
bot.run()


        










