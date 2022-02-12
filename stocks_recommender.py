from fastapi import FastAPI
import uvicorn

from pymongo import MongoClient
import pymongo
from pydantic import BaseModel

class RecommenderConfig(BaseModel):
    'instrument_token': str
    'interval': int

class Recommenders(BaseModel):
    'recommenders': list[RecommenderConfig]


app = FastAPI()
client = MongoClient('mongodb://localhost:27017/')
db = client['kiteconnect']
stocks_actions_recommendations = db['stocks_actions_recommendations']

@app.get('/instruments')
def get_instruments():
    instruments_collection = db['instruments']
    instruments = []
    for instrument in instruments_collection.find():
        del instrument['_id']
        instruments.append(instrument)
    return {'instruments': instruments}

@app.post('/recommender')
def create_recommender(recommenders: Recommenders):
    recommenders_mongo = db['recommenders']
    recommenders_mongo.insert_many(recommenders)

@app.get('/recommendations')
def get_recommendations():
    recommenders_mongo = db['recommenders']
    recommendations = db['action_recommendations']
    for recommender in recommenders_mongo.find():
        recommender['']