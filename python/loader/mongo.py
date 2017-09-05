import logging
from timeit import default_timer as timer
from pymongo import MongoClient
from loader import generate_minutes, generate_hourly, generate_daily, generate_monthly, generate_yearly

# TODO: clean up timing

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


def connect_to_db(uri):
    client = MongoClient(uri)
    return client.get_database()


def load_docs(db, coll, function, number_of_batches, size_of_batches):
    logging.info('loading data into collection: %s' % coll)
    batches_ran = 0
    total_inserts = 0
    total_runtime = 0
    global_start = timer()
    while batches_ran < number_of_batches:
        docs = []
        batch_start = timer()
        for i in function(size_of_batches):
            docs.append(i)
        batch_end = timer()
        db[coll].insert_many(docs)
        insert_end = timer()
        logging.debug('insert 100 (doc_gen:%.4fus, insert:%.4fus, batch_run:%.4fus)', (batch_end-batch_start), (insert_end-batch_end), (insert_end-batch_start))
        batches_ran += 1

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