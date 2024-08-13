import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client['GracoSoftNataliaML']
collection = db['materias']