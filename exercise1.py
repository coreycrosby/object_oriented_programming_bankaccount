class BankAccount:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Bank Account: balance: {self.balance} , interest_rate: {self.interest_rate}"

    def deposit(self, amount): 
        self.balance = self.balance + amount
        return f"Total Balance: {self.balance}"

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return f"Total Balance: {self.balance}"

    def gain_interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate)
        return f"Total Balance: {self.balance}"

account = BankAccount(100, 0.02)
account.deposit(40)
account.withdraw(20)
account.gain_interest()


print(account)



