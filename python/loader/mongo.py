from pymongo import MongoClient
from loader import generate_minutes

MONGO_DEFAULT_URI = 'mongodb://localhost:27017/sample'

def connect_to_db(uri=MONGO_DEFAULT_URI):
    client = MongoClient(uri)
    return client.get_database()


def load_minutes(db, number_of_batches=10, size_of_batches=100):
    batches_ran = 0
    while batches_ran < number_of_batches:
        docs = []
        for i in generate_minutes(size_of_batches):
            docs.append(i)
        db['minutes'].insert_many(docs)
        batches_ran += 1

