import time
import threading


def test():
    while True:
        print("test")
        time.sleep(1)


thr = threading.Timer(10, test)
thr.start()

for _ in range(3):
    print("111")
    time.sleep(1)

thr.cancel()
print('finish')
