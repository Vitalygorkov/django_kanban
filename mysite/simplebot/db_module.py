# https://docs.sqlalchemy.org/en/14/core/engines.html

from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
engine = create_engine('sqlite:///mydatabase.db')

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

# mapper(Task, tasks_table)
print(mapper(Task, tasks_table))