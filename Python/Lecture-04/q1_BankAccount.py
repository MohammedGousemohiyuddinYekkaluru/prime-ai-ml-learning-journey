# Create a BankAccount class with attributes account_number, owner_name, and balance. Add methods to deposit, withdraw, and check balance

class BankAccount:

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, dep_money):
        self.balance += dep_money
        return f"Deposited {dep_money}. New balance: {self.balance}"

    def withdraw(self, withdraw_money):
        if withdraw_money > self.balance:
            return "Insufficient balance!"
        self.balance -= withdraw_money
        return f"Withdrew {withdraw_money}. New balance: {self.balance}"

    def get_balance(self):
        return f"Current balance: {self.balance}"
    

AccountOne = BankAccount(1234, "Gouse", 800)

print(AccountOne.deposit(200))
print(AccountOne.withdraw(500))
print(AccountOne.get_balance())


