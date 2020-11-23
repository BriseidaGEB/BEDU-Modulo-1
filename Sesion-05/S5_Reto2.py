import re
from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://Briseida011:BEDU011@bedu011.ltaio.mongodb.net/test?authSource=admin&replicaSet=atlas-q4k03o-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'number_of_reviews': {
        '$gte': 50
    }, 
    'review_scores.review_scores_rating': {
        '$gte': 80
    }, 
    'amenities': {
        '$in': [
            re.compile(r"Ethernet(?i)")
        ]
    }, 
    'address.country_code': 'BR'
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)