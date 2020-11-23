import re
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://Briseida011:BEDU011@bedu011.ltaio.mongodb.net/test?authSource=admin&replicaSet=atlas-q4k03o-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$project': {
            '_id': 0, 
            'amenities': 1
        }
    }, {
        '$match': {
            'amenities': {
                '$in': [
                    re.compile(r"Wifi(?i)"), re.compile(r"Ethernet(?i)")
                ]
            }
        }
    }, {
        '$count': 'Total'
    }
])