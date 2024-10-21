from threading import Thread, Lock
from time import sleep
from random import randint
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            replenishment = randint(50, 500)
            with self.lock:
                self.balance += replenishment
                print(f"Пополнение: {replenishment}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            replenishment = randint(50, 500)
            print(f"Запрос на {replenishment}")
            with self.lock:
                if replenishment <= self.balance:
                    self.balance -= replenishment
                    print(f"Снятие: {replenishment}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')