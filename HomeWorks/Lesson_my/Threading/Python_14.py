import multiprocessing
import random
import time


def get_text(g):
    g.put("test")


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    pr = multiprocessing.Process(target=get_text, args=(queue,))
    pr.start()
    print(queue.get())
    pr.join()
