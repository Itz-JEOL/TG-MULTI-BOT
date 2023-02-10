from variables import DB_URL, DB_NAME, LOG_TEXT, LOG_CHANNEL
import motor.motor_asyncio, datetime


class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,            
            join_date=datetime.date.today().isoformat(),           
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count
  
    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

 
db = Database(DB_URL, DB_NAME)


async def add_user(bot, msg):
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id)
        if LOG_CHANNEL is not None:            
            await bot.send_message(LOG_CHANNEL,
                text=LOG_TEXT.format(id=msg.from_user.id,
                    dc_id=msg.from_user.dc_id,
                    first_name=msg.from_user.first_name,
                    username=msg.from_user.username,
                    bot=bot.mention)
            )

               





