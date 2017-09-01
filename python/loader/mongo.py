import logging
from pymongo import MongoClient
from datetime import datetime as dt
from loader import generate_minutes, generate_hourly, generate_daily, generate_monthly, generate_yearly

MONGO_DEFAULT_URI = 'mongodb://localhost:27017/sample'

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


def connect_to_db(uri=MONGO_DEFAULT_URI):
    client = MongoClient(uri)
    return client.get_database()


def load_minutes(db, number_of_batches=100, size_of_batches=100):
    logging.info('load_minutes started')
    batches_ran = 0
    while batches_ran < number_of_batches:
        docs = []
        for i in generate_minutes(size_of_batches):
            docs.append(i)
        db['minutes'].insert_many(docs)
        logging.debug('inserted 100 documents in minutes collection')
        batches_ran += 1


def load_hourly(db, number_of_batches=100, size_of_batches=100):
    logging.info('load_hourly started')
    batches_ran = 0
    while batches_ran < number_of_batches:
        docs = []
        for i in generate_hourly(size_of_batches):
            docs.append(i)
        db['hourly'].insert_many(docs)
        logging.debug('inserted 100 documents in hours collection')
        batches_ran += 1


def load_daily(db, number_of_batches=100, size_of_batches=100):
    logging.info('load_daily started')
    batches_ran = 0
    while batches_ran < number_of_batches:
        docs = []
        for i in generate_daily(size_of_batches):
            docs.append(i)
        db['daily'].insert_many(docs)
        logging.debug('inserted 100 documents in daily collection')
        batches_ran += 1


def load_monthly(db, number_of_batches=100, size_of_batches=100):
    logging.info('load_monthly started')
    batches_ran = 0
    while batches_ran < number_of_batches:
        docs = []
        for i in generate_monthly(size_of_batches):
            docs.append(i)
        db['monthly'].insert_many(docs)
        logging.debug('inserted 100 documents in monthly collection')
        batches_ran += 1


def load_yearly(db, number_of_batches=100, size_of_batches=100):
    logging.info('load_yearly started')
    batches_ran = 0
    while batches_ran < number_of_batches:
        docs = []
        for i in generate_yearly(size_of_batches):
            docs.append(i)
        db['yearly'].insert_many(docs)
        logging.debug('inserted 100 documents in yearly collection')
        batches_ran += 1


def temp_agg(db):
    db['minutes'].aggregat([
            {'$match': {'date': {'$gte': dt.now() - 367, '$lte': dt.now()}}}

        ])