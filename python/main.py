from loader.mongo import connect_to_db, load_minutes

## THREADS for each collection
#
# main runner for loading data
#
if __name__ == '__main__':
    db = connect_to_db()
    load_minutes(db)
