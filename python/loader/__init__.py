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
            dim['direction'] = random.choice(DIRECTIONS)
            dim['acct_status'] = random.choice(ACCT_STATUSES)
        if type == 'hour':
            dim['hh'] = date.hour
        elif type == 'daily' or type == 'monthly' or type == 'yearly':
            dim['date'] = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
        doc['val'].append(dim)
    return doc


#
# generate some number of documents
#
def generate_minutes(n):
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


def generate_hourly(n):
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


def generate_daily(n):
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


def generate_monthly(n):
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


def generate_yearly(n):
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