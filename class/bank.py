class BankAccount:
    def __init__(self, account_number,account_holder,balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Amount must be greater than 0.")
# =============================================================
# inheritance
class SavingsAccount(BankAccount):
    def __init__(self,account_number,account_holder,balance=0.0,interest_rate=0.2):
        super().__init__(account_number,account_holder,balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added {interest} interest. New balance is {self.balance}.")
# =============================================================
account = BankAccount("123456", "John Doe", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(1500.0)
print("========================================================")
savings = SavingsAccount("654321", "Jane Smith", 5000.0, 0.05)
savings.deposit(1000.0)
savings.withdraw(200.0)
savings.add_interest()