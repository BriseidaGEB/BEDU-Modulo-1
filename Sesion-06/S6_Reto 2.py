from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb+srv://Briseida011:BEDU011@bedu011.ltaio.mongodb.net/test?authSource=admin&replicaSet=atlas-q4k03o-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_mflix']['comments'].aggregate([
    {
        '$lookup': {
            'from': 'users', 
            'localField': 'email', 
            'foreignField': 'email', 
            'as': 'personas'
        }
    }, {
        '$addFields': {
            'usuario_objeto': {
                '$arrayElemAt': [
                    '$personas', 0
                ]
            }
        }
    }, {
        '$addFields': {
            'contraseña': '$usuario_objeto.password'
        }
    }, {
        '$project': {
            '_id': 0, 
            'text': 1, 
            'name': 1, 
            'email': 1, 
            'contraseña': 1
        }
    }
])