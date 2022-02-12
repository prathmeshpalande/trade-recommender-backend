from collections import UserDict
from fastapi import FastAPI
from pymongo import MongoClient
import pymongo

app = FastAPI()

client = MongoClient('mongodb://localhost:27017/')
db = client['uaot-recommender']
@app.get('/watchlist')
def get_watchlist(username: str):
    watchlist = db['watchlist']
    _watchlist = watchlist.find({'username': username}).next()
    del _watchlist['_id']
    print(_watchlist)
    # return {'watchlist': _watchlist}
    return _watchlist

@app.get('/recommendations')
def get_recommendations(stock: str, interval: int):
    recommendations = db['recommendations']
    _recommendations = recommendations.find({'stock': stock.lower(), 'interval': interval})
    _recommendations_ = []
    for recommendation in _recommendations:
        del recommendation['_id']
        _recommendations_.append(recommendation)
    print(_recommendations_)
    return _recommendations_
