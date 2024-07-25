from multiprocessing import Pool, Manager, Process, Array, Queue, Lock


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request, q, lock):
        product, action, amount = request
        with lock:
            if not q.empty():
                self.data = q.get()
            _amount = 0
            if product in self.data:
                _amount = self.data[product]
            if action == "receipt":
                _amount += amount
            elif action == "shipment":
                _amount -= amount
            self.data[product] = _amount

            self.__finalization(q)
            q.put(self.data)

    def __finalization(self, q):
        while not q.empty():
            _data = q.get()
            for key in _data:
                if key in self.data:
                    self.data[key] += _data[key]
                else:
                    self.data[key] = _data[key]

    def run(self, requests):
        q = Queue()
        lock = Lock()
        processes = []
        for request in requests:
            p = Process(target=self.process_request, args=(request, q, lock))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        for _ in processes:
            if not q.empty():
                self.data = q.get()


if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)
    # manager.send_command()
    # Выводим обновленные данные о складских запасах
    print(manager.data)
    # Вывод наконсоль:
    # {"product1": 70, "product2": 100, "product3": 200}
