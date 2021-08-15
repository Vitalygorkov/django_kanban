# https://docs.sqlalchemy.org/en/14/core/engines.html
# https://ru.wikibooks.org/wiki/SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine('sqlite:///mydatabase.db')
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
# metadata.create_all(engine)


class Task(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.description)

# mapper(Task, tasks_table)
print(mapper(Task, tasks_table))

# task1 = Task('make a bot for processing tasks', 'master the use of orm databases, write command handlers and bot logic')
# session.add(task1)
# session.commit()

# ourTask = session.query(Task).first()

def add_task(name, description):
    task = Task(name,description)
    session.add(task)
    session.commit()
    print(("'")+str(name)+("'")+'-task is written to the database')

add_task('new task', 'new task description')

# print(ourTask)
# print(task1)
# print(task1.id)