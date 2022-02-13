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
    _watchlist = watchlist.find({'username': username})
    _watchlist_ = []
    for stock in _watchlist:
        del stock['_id']
        _watchlist_.append(stock)
    # del _watchlist['_id']
    print(_watchlist_)
    # return {'watchlist': _watchlist}
    return _watchlist_

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

@app.get('/status/market')
def get_market_status():
    return 'OFF'

@app.get('/instruments')
def get_instruments():
    instruments = db['instruments']
    _instruments = instruments.find()
    _instruments_ = []
    for instrument in _instruments:
        del instrument['_id']
        _instruments_.append(instrument)
    return _instruments_