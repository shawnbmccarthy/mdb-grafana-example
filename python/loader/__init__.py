import random

from datetime import datetime as dt
from datetime import timedelta as td
from loader.data import CAST_OF_CHARACTERS, ACCT_STATUSES, ACCT_TYPES,\
    INTERNET_DOMAINS, DAYS_IN_YEAR, DIRECTIONS, DOB_YRS, HOURS_IN_YEAR, REPS, STATES, \
    MINUTES_IN_YEAR, MAX_DIMENSION, MIN_VALUE, MAX_VALUE

#
# will generate data over something like 3 years
# TODO: Change data format to a flat structure with idx's
#


def random_first_name():
    return random.choice(CAST_OF_CHARACTERS)[0]


def random_last_name():
    return random.choice(CAST_OF_CHARACTERS)[1]


def generate_username():
    name = random.choice(CAST_OF_CHARACTERS)
    return (name[0][1] + '.' + name[1]).replace(' ', '.')


# will need to see how this works
def generate_profiles(n):
    m = 0
    while m < n:
        doc = {}
        doc['name'] = { 'first': random_first_name(), 'last': random_last_name() }
        doc['_id'] = (doc['name']['first'][0] + '.' + doc['name']['last']).replace(' ', '.')
        # create 1 - 5 years back randomly
        doc['created_on'] = dt.now() - td(minutes=random.randint(MINUTES_IN_YEAR, MINUTES_IN_YEAR * 5))
        doc['updated_on'] = dt.now() - td(minutes=random.randint(0, MINUTES_IN_YEAR - 60))
        doc['id_num'] = m
        # just mask it for right now
        doc['password'] = '***********'
        # leave it pretty flat right now - will work on it later
        yield doc
        m += 1


def generate_flat_doc(db, date, delta):
    doc = {}
    uDoc = None
    cond = True
    while cond:
        uDoc = db['profile'].find_one({'id_num': random.randint(0,4999)})
        if uDoc != None:
            cond = False

    userId = uDoc['_id']
    doc['userId'] = userId
    doc['date'] = date - delta
    doc['mm'] = doc['date'].minute
    doc['hh'] = doc['date'].hour
    doc['nnas'] = random.uniform(MIN_VALUE, MAX_VALUE)
    doc['dim'] = {
        'rep': random.choice(REPS),
        'dob_yr': random.choice(DOB_YRS),
        'acct_type': random.choice(ACCT_TYPES),
        'state': random.choice(STATES),
        'direction': random.choice(DIRECTIONS),
        'acct_status': random.choice(ACCT_STATUSES)
    }
    return doc

def generate_doc(date, delta, type='minute', extendedData=False):
    doc = {}
    doc['_class'] = 'com.mongodb.BasicDBObject',
    doc['userId'] = generate_username()
    doc['date'] = date - delta
    if type == 'minute':
        doc['mm'] = date.minute
    elif type == 'hour':
        doc['hh'] = date.hour
    doc['val'] = []
    for i in range(0, random.randint(1, MAX_DIMENSION)):
        dim = {}
        dim['dim'] = {}
        dim['value'] = random.uniform(MIN_VALUE, MAX_VALUE)
        dim['dim']['rep'] = random.choice(REPS)
        dim['dim']['dob_yr'] = random.choice(DOB_YRS)
        dim['dim']['acct_type'] = random.choice(ACCT_TYPES)
        dim['dim']['state'] = random.choice(STATES)
        if extendedData:
            dim['dim']['direction'] = random.choice(DIRECTIONS)
            dim['dim']['acct_status'] = random.choice(ACCT_STATUSES)
        if type == 'hour':
            dim['dim']['hh'] = date.hour
        elif type == 'daily' or type == 'monthly' or type == 'yearly':
            dim['dim']['date'] = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
        doc['val'].append(dim)
    return doc


#
# generate some number of documents
#
def generate_minutes(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            minutes=random.randint(0, MINUTES_IN_YEAR),
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_doc(date, delta)
        m += 1


def generate_hourly(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            hours=random.randint(0, HOURS_IN_YEAR),
            minutes=date.minute,
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_doc(date, delta, 'hourly')
        m += 1
    pass


def generate_daily(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            days=random.randint(0, DAYS_IN_YEAR),
            hours=date.hour, minutes=date.minute,
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_doc(date, delta, 'daily', True)
        m += 1
    pass


def generate_monthly(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            days=random.randint(0, DAYS_IN_YEAR),
            hours=date.hour,
            minutes=date.minute,
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_doc(date, delta, 'monthly')
        m += 1
    pass


def generate_yearly(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            days=random.randint(0, DAYS_IN_YEAR),
            hours=date.hour, minutes=date.minute,
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_doc(date, delta, 'yearly')
        m += 1
    pass

#
# generate some number of documents
#
def generate_flat_minutes(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            minutes=random.randint(0, MINUTES_IN_YEAR),
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_flat_doc(db, date, delta)
        m += 1


def generate_flat_hourly(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            hours=random.randint(0, HOURS_IN_YEAR),
            minutes=date.minute,
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_flat_doc(db, date, delta)
        m += 1
    pass


def generate_flat_daily(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            days=random.randint(0, DAYS_IN_YEAR),
            hours=date.hour, minutes=date.minute,
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_flat_doc(db, date, delta)
        m += 1
    pass


def generate_flat_monthly(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            days=random.randint(0, DAYS_IN_YEAR),
            hours=date.hour,
            minutes=date.minute,
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_flat_doc(db, date, delta)
        m += 1
    pass


def generate_flat_yearly(db, n):
    m = 0
    while m < n:
        date = dt.now()
        delta = td(
            days=random.randint(0, DAYS_IN_YEAR),
            hours=date.hour, minutes=date.minute,
            seconds=date.second,
            microseconds=date.microsecond
        )
        yield generate_flat_doc(db, date, delta)
        m += 1
    pass