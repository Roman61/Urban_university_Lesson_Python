import threading
import time


def get_data(thr_name, data):
    for i in range(100):
        print(f'{thr_name} - {i} - {data}')
        time.sleep(5)


thr = threading.Thread(group=None, target=get_data,
                       name="thr-1", args=(str(time.time()), 1),
                       kwargs={}, daemon=None)

# thr = threading.Thread(target=get_data, args=(str(time()),), name="thr-1")
thr.start()

for i in range(100):
    print(f"current: {i}")
    time.sleep(1)

    if i % 10 == 0:
        print("active tread:", threading.active_count())
        print("enumerate:", threading.enumerate())
        print("thr-1 is alive:", thr.is_alive())

