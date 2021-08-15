# https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
# import sqlalchemy
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)
# print("Версия SQLAlchemy:", sqlalchemy.__version__)
#
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# metadata = MetaData()
# users_table = Table('tasks', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('task_name', String),
#     Column('task_text', String),
#     Column('task_rating', String),
#     Column('task_category', String),
#     Column('task_status', String)
# )
# metadata.create_all(engine)
#
# class Task(object):
#     def __init__(self, task_name, task_text, task_rating, task_category, task_status):
#         self.task_name = task_name
#         self.task_text = task_text
#         self.task_rating = task_rating
#         self.task_category = task_category
#         self.task_status = task_status
#
#     def __repr__(self):
#         return "<Task('%s', '%s', '%s', '%s', '%s')>" % (self.task_name, self.task_text, self. task_rating, self.task_category, self.task_status)
#
#

# https://ru.wikibooks.org/wiki/SQLAlchemy
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine('sqlite:///bot_database.db')
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
tasks_table = Table('tasks', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('description', String)
                    )

metadata.create_all(engine)


class Task(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.description)

mapper(Task, tasks_table)

def add_task(name, description):
    task = Task(name,description)
    session.add(task)
    session.commit()
    print(("'")+str(name)+("'")+'-task is written to the database')



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
    add_task(str(msg.text), 'task description')
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)