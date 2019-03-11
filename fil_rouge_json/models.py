from peewee import *

db1 = SqliteDatabase('Game_Servers1.db')

class Game_Servers1(Model):
    adresse_ip = IntegerField()
    name = CharField()
    game = 'Morpion'

    class Meta:
        database = db


db2 = SqliteDatabase('Game_Servers2.db')


class Game_Servers2(Model):
    adresse_ip = IntegerField()
    name = CharField()
    game = '4_en_ligne'

    class Meta:
        database = db2



