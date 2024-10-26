import multiprocessing


def worker_function(shared_data):
    shared_data.append(42)


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        shared_data = manager.list()
        processes = []
        for _ in range(4):
            p = multiprocessing.Process(target=worker_function, args=(shared_data,))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        print(shared_data)  # Вывод результата
