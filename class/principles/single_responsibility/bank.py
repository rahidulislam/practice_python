# without SRP
class BankAccount:
    def __init__(self, account_number:str, balance:float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount:float):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount:float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient Balance")
    def log_transaction(self,transaction_type:str, amount:float):
        print(f"Logged: {transaction_type} of {amount}")

# Instantiate the class
account = BankAccount("123456789", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
account.log_transaction("Deposit", 500.0)

# with SRP
class BankAccount:
    def __init__(self, account_number:str, balance:float):
        self.account_number = account_number
        self.balance = balance

class BankAccountManager:
    @staticmethod
    def deposit(account:BankAccount, amount:float):
        account.balance += amount
        print(f"Deposited {amount}. New Balance: {account.balance}")

    @staticmethod
    def withdraw(account:BankAccount, amount:float):
        if account.balance >= amount:
            account.balance -= amount
            print(f"Withdrew {amount}. New Balance: {account.balance}")
        else:
            print("Insufficient Balance")

class TransactionLogger:
    @staticmethod
    def log_transaction(account:BankAccount, transaction_type:str, amount:float):
        print(f"Logged: {transaction_type} of {amount} for {account.account_number}")

# Instantiate the class
account = BankAccount("123456789", 1000.0)
BankAccountManager.deposit(account, 500.0)
BankAccountManager.withdraw(account, 200.0)
TransactionLogger.log_transaction(account, "Deposit", 500.0)