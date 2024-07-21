from threading import Thread
from threading import Lock

lock = Lock()


class BankAccount:

    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        with lock:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with lock:
            if self.balance < amount:
                raise ValueError('Недостаточно средств')
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")


bank_account = BankAccount()


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


deposit_thread = Thread(target=deposit_task, args=(bank_account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(bank_account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
