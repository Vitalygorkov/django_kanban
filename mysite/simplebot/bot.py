# https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
# https://ru.wikibooks.org/wiki/SQLAlchemy
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN

import sqlalchemy
# from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
print("Версия SQLAlchemy:", sqlalchemy.__version__)

# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users_table = Table('tasks', metadata,
    Column('id', Integer, primary_key=True),
    Column('task_name', String),
    Column('task_text', String),
    Column('tsk_rating', String),
    Column('tsk_category', String),
    Column('tsk_status', String)
)
metadata.create_all(engine)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)