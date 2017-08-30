import threading
from loader.mongo import connect_to_db, load_minutes, load_hourly, load_daily, load_monthly, load_yearly

#
# main runner for loading data
# TODO: cleanup threads - make it nicer
# TODO: introduce timer and statistics
#
if __name__ == '__main__':
    db = connect_to_db()

    threads = ['load_minutes', 'load_hourly', 'load_daily', 'load_monthly', 'load_yearly']
    running = []
    for t in threads:
        db.drop_collection(t)
        thrd = threading.Thread(name=t, target=locals().get(t), kwargs={'db': db}, daemon=True)
        thrd.start()
        running.append(thrd)

    for r in running:
        r.join()