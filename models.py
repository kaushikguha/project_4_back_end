from peewee import *
import datetime
from flask_login import UserMixin

# DATABASE=SqliteDatabase('pmt.sqlite')
DATABASE=PostgresqlDatabase('pmt', user='kguha')

#Our Model
class User(UserMixin, Model):
    ssn = CharField(max_length=11, unique=True)
    first_name= CharField()
    last_name= CharField()
    email=CharField(unique=True)
    username= CharField(unique=True)
    password=CharField()


    class Meta:
        database=DATABASE


class Pmt(Model):
    ssn= ForeignKeyField(User, backref='my_pmt')
    pmt_date= CharField(max_length=10)
    amt_paid= FloatField()

    class Meta:
        database=DATABASE






def initialize():
    DATABASE.connect()

    DATABASE.create_tables([User, Pmt], safe=True)

    print('Connected to the DB and created tables')

    DATABASE.close()
