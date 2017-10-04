import logging
import time
from timeit import default_timer as timer
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from loader import generate_minutes, generate_hourly, generate_daily, generate_monthly, generate_yearly, generate_profiles, \
    generate_flat_daily, generate_flat_hourly, generate_flat_minutes, generate_flat_monthly, generate_flat_yearly

# TODO: clean up timing

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


def connect_to_db(uri):
    client = MongoClient(uri)
    return client.get_database()


def create_profiles(db, coll='profile', number_of_profiles=5000):
    logging.info('creating %d profiles', number_of_profiles)
    for i in generate_profiles(number_of_profiles):
        try:
            ret = db[coll].insert_one(i)
        except:
            pass

        while db[coll].count() < number_of_profiles:
            for i in generate_profiles(db[coll].count()):
                try:
                    ret = db[coll].insert_one(i)
                except:
                    pass


def load_docs(db, coll, function, number_of_batches, size_of_batches):
    logging.info('loading data into collection: %s', coll)
    batches_ran = 0
    while batches_ran < number_of_batches:
        docs = []
        batch_start = timer()
        for i in function(db, size_of_batches):
            docs.append(i)
        batch_end = timer()
        try_insert_many(db, coll, docs)

        insert_end = timer()
        logging.debug('%d: insert %d (doc_gen:%.4fus, insert:%.4fus, batch_run:%.4fus)', number_of_batches, size_of_batches, (batch_end-batch_start), (insert_end-batch_end), (insert_end-batch_start))
        batches_ran += 1


def try_insert_many(db, coll, docs):
    success  = False
    attempts = 0
    while not success:
        try:
            db[coll].insert_many(docs)
            success = True
        except PyMongoError as e:
            logging.error('failed to insert (code:%s): %s', e.code, e.details)
            for d in docs:
                if '_id' in d:
                    del(d['_id'])
            attempts += 1
        if attempts >= 10:
            logging.error('failed in 10 attempts: will save')
            success = True
        time.sleep(attempts)

def load_minutes(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'minutes', generate_minutes, number_of_batches, size_of_batches)


def load_hourly(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'hourly', generate_hourly, number_of_batches, size_of_batches)


def load_daily(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'daily', generate_daily, number_of_batches, size_of_batches)


def load_monthly(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'monthly', generate_monthly, number_of_batches, size_of_batches)


def load_yearly(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'yearly', generate_yearly, number_of_batches, size_of_batches)


def load_minutes_flat(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'minutes_flat', generate_flat_minutes, number_of_batches, size_of_batches)


def load_hourly_flat(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'hourly_flat', generate_flat_hourly, number_of_batches, size_of_batches)


def load_daily_flat(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'daily_flat', generate_flat_daily, number_of_batches, size_of_batches)


def load_monthly_flat(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'monthly_flat', generate_flat_monthly, number_of_batches, size_of_batches)


def load_yearly_flat(db, number_of_batches=100, size_of_batches=100):
    load_docs(db, 'yearly_flat', generate_flat_yearly, number_of_batches, size_of_batches)