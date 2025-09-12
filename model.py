from pymongo import MongoClient

class MyRecipeModel:
    def __init__(self, db_name, connection_uri="mongodb://localhost:27017/"):
        self.client = MongoClient(connection_uri)
        self.db = self.client[db_name]
        self.collection = self.db["recipes"]
