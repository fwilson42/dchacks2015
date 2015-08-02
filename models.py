from peewee import *
import json

with open("config.json") as f:
    config = json.load(f)

db = PostgresqlDatabase(config["POSTGRES_USER"], host=config["POSTGRES_HOST"],
        user=config["POSTGRES_USER"],
        password=config["POSTGRES_PASSWORD"])

class BaseModel(Model):
    class Meta:
        database = db

class HistoricalTrainPosition(BaseModel):
    cars = IntegerField()
    line_code = CharField()
    next_station = CharField()
    dest_station = CharField()
    time = IntegerField()
    timestamp = DateTimeField()
    trackgroup = IntegerField()
