from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://Briseida011:BEDU011@bedu011.ltaio.mongodb.net/test?authSource=admin&replicaSet=atlas-q4k03o-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$project': {
            'property_type': 1, 
            'price': 1, 
            'bedrooms': 1, 
            'address.country': 1
        }
    }, {
        '$match': {
            'property_type': 'House', 
            'bedrooms': {
                '$gte': 1
            }
        }
    }, {
        '$addFields': {
            'costo_por_habitacion': {
                '$divide': [
                    '$price', '$bedrooms'
                ]
            }
        }
    }, {
        '$group': {
            '_id': '$address.country', 
            'promedio_costo_habitacion': {
                '$avg': '$costo_por_habitacion'
            }
        }
    }
])