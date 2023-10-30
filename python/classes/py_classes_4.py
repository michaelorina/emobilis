# Inheritance Override

class Account:
    def __init__(self, name, number, balance):
        self.acc_name = name
        self.acc_number = number
        self.acc_balance = balance

    def deposit(self, amount):
        self.acc_balance += amount

    def withdraw(self, amount):
        if amount > self.acc_balance:
            print(f"Insufficient funds. Balance is {self.acc_balance}")
        else:
            self.acc_balance -= amount

    def __str__(self):
        return f"name: {self.acc_name}, accNO: {self.acc_number}, balance {self.acc_number}"


class DollarAccounts(Account):
    def rates(self):
        return 153.89

    def deposit(self, amount):
        usd = amount / self.rates()
        self.acc_balance += usd


dc1 = DollarAccounts("Mike", "d-004", 4500)
dc1.withdraw(500)
print(dc1.acc_balance)
print(dc1.rates())
dc1.deposit(20000)
print(dc1.acc_balance)

acc1 = Account("Michael", "001", 13000)
acc1.deposit(5000)
print(acc1.acc_balance)
print(acc1)

# # Named Parameters
# acc2 = Account(balance=3400, name="Meave", number="911")
# acc2.deposit(600)
# print(acc2.acc_balance)
