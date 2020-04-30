from peewee import *
import datetime
from flask_login import UserMixin


DATABASE = SqliteDatabase('recipes.sqlite')

class Creator(UserMixin, Model):
	username=CharField(unique = True)
	email=CharField(unique = True)
	password=CharField()

	class Meta:
		database = DATABASE

class Recipe(Model):
	name = CharField()
	ingredients = TextField()
	directions = TextField()
	vegan = BooleanField()
	gluten_free = BooleanField()
	creator = ForeignKeyField(Creator, backref='recipes')
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Creator,Recipe], safe=True)
	print("Connected to db and created tables, unless they already exist")
	DATABASE.close()