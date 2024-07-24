from queue import Queue
import random
import threading
from time import sleep


class Table:
    def __init__(self, number, is_busy=False):
        self.number: int = number
        self.is_busy: bool = is_busy


class Cafe:

    def __init__(self, table_s, schedule=4, maximum=25):
        self.tables = table_s
        self.__customers = None
        self.serve_customer_thread = None
        self.estimated_shifting_maximum_number_of_clients = maximum
        self.schedule = schedule  # часов работы
        self.queue_customers = Queue()
        self.close_cafe = False

    def customer_arrival(self):  # - моделирует приход посетителя(каждую секунду).
        self.serve_customer_thread = threading.Thread(target=self.serve_customer)
        self.serve_customer_thread.start()
        index = 1
        while True:
            chance_of_getting_a_client = (random.randint(1, 100) % 2 == 1)
            if chance_of_getting_a_client:
                __customer = Customer(index)
                self.queue_customers.put(__customer)
                index += 1
            self.schedule -= 0.1
            if self.schedule <= 0:
                break
            sleep(1)

        self.close_cafe = True
        print("Кафе закрывается!")
        self.serve_customer_thread.join()
        print("Все клиенты ушли!")

    def __get_free_table(self):
        for table in tables:
            if not table.is_busy:
                return table.number
        return 0

    def __set_free_table(self, number):
        for table in tables:
            if table.number == number:
                table.is_busy = False

    def __take_a_table(self, number):
        for table in tables:
            if table.number == number:
                table.is_busy = True
                return True
        return False

    def serve_customer(self):  # - моделирует обслуживание посетител
        customers = []

        print("Начали обслуживание клиентов")
        while True:
            customers_next = []
            if not self.queue_customers.empty():
                for _ in range(0, self.queue_customers.qsize()):
                    customer = self.queue_customers.get()
                    customers.append(customer)
            for customer in customers:
                if customer.status == customer.status_empty:
                    continue
                else:
                    customers_next.append(customer)
                if customer.status == customer.status_arrived:
                    table = self.__get_free_table()
                    if table != 0:
                        customer.table = table
                        customer.up_status()
                        self.__take_a_table(table)
                    else:
                        customer.await_status()
                    continue
                customer.up_status()
                if customer.status == customer.status_ate_and_left:
                    self.__set_free_table(customer.table)

            sleep(6)
            customers = customers_next
            if self.queue_customers.empty() and len(customers) == 0 and self.close_cafe:
                break


class Customer:
    __enums = ("прибыл", "сел за стол", "покушал и ушёл", "")
    __name_default = "Посетитель номер"

    @property
    def status_arrived(self):
        return self.__enums[0]

    @property
    def status_sat_down_at_the_table(self):
        return self.__enums[1]

    @property
    def status_ate_and_left(self):
        return self.__enums[2]

    @property
    def status_empty(self):
        return self.__enums[3]

    def __init__(self, index, name=__name_default):
        self.index = index
        self.__status_index = -1
        self.status = Customer.__enums[self.__status_index]
        self.name = name
        self.wait = False
        self.table = -1
        self.up_status()

    def get_table(self):
        if self.table != -1:
            return self.table
        else:
            return ""

    def up_status(self):
        self.wait = False
        self.__status_index += 1
        self.status = Customer.__enums[self.__status_index]
        if self.__status_index < (len(Customer.__enums) - 1):

            if self.name == Customer.__name_default:
                print(f"{self.name} {self.index} {self.status} {self.get_table()}")
            else:
                print(f"{self.name} {self.status}")
        else:
            pass

    def await_status(self):
        self.wait = True
        await_str = "ожидает свободный стол"
        if self.name == Customer.__name_default:
            print(f"{self.name} {self.index} {await_str}")
        else:
            print(f"{self.name} {await_str}")


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
