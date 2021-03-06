import threading
import yaml
from loader.mongo import connect_to_db, load_minutes, load_hourly, load_daily, load_monthly, load_yearly,\
    create_profiles, load_hourly_flat, load_daily_flat, load_minutes_flat, load_monthly_flat, load_yearly_flat

#
# main runner for loading data
# TODO: introduce timer and statistics
#
if __name__ == '__main__':
    with open('config.yaml', 'r') as y:
        cfg = yaml.load(y)

    db = connect_to_db(cfg['mongodb']['url'])

    threads = [
        'load_minutes', 'load_hourly', 'load_daily', 'load_monthly', 'load_yearly', 'load_hourly_flat',
        'load_daily_flat', 'load_minutes_flat', 'load_monthly_flat', 'load_yearly_flat'
    ]
    running = []

    #create_profiles(db)
    for t in threads:
        #db.drop_collection(t)
        thrd = threading.Thread(name=t, target=locals().get(t), kwargs={'db': db}, daemon=True)
        thrd.start()
        running.append(thrd)

    for r in running:
        r.join()