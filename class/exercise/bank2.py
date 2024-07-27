class Bank:
    """
    Exercise 3: Encapsulation and Getters/Setters

    Task: Create a class Account that represents a bank account with the following:

        Attributes:
            account_number (string)
            balance (float, private)

        Methods:
            __init__(self, account_number, initial_balance): Initializes the account number and sets the initial balance.
            deposit(self, amount): Adds the given amount to the balance.
            withdraw(self, amount): Deducts the given amount from the balance if sufficient funds are available.
            get_balance(self): Returns the current balance.

    Challenge: Create an instance of the Account class, deposit some money, withdraw some money, and print the final balance.
    """

    def __init__(self, account_number):
        self.account_number = account_number
        self.__balance = 0.0

    def set_deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be greater than 0")

    def set_withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient balance")
        else:
            print("Amount must be greater than 0")

    def get_balance(self):
        print(f"Balance is {self.__balance}")


# ===============================================
account = Bank("123456")
account.set_deposit(5000)
account.set_withdraw(2000)
account.get_balance()
