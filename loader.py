from aiogram import Bot, Dispatcher
from os import getenv
from data_base import DataBase
# from config import db_path

# memory = MemoryStorage()

bot = Bot(getenv('TOKEN'))
dp = Dispatcher(bot)
db = DataBase()

# async def on_startup(_):
#     try:
#         db.create_table_users()
#         db.create_table_events()
#         db.create_table_locations()
#         print('DB connected ... OK!')
#     except:
#         print('DB failure!')
#
# async def on_shutdownn(_):
#     db.disconnect()
