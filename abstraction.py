from abc import ABC, abstractmethod

# Defining and abstract class
class Banking(ABC):

    @abstractmethod
    def check_balance(self):
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def deposit(self):
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def withdraw(self):
        raise NotImplementedError("Not implemented")

# Defining a subclass
class Bank(Banking):

    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is: {self.balance}")
        return

    def deposit(self, money):
        self.balance += money
        print(f"Your new balance is: {self.balance}")
        return

    def withdraw(self, money):
        self.balance -= money
        print(f"Your new balance is: {self.balance}")
        return

# User menu 
def menu():
    choice = int(input(""" 
    Please select the action you would like to perform:
    1. Check balance
    2. Deposit
    3. Withdraw
    4. Exit
    """))

    if choice == 1:
        realbank.check_balance()
        menu()
    elif choice == 2:
        deposit = int(input("Please enter the amount you wish to deposit: "))
        realbank.deposit(deposit)
        menu()
    elif choice == 3:
        withdraw = int(input("Please enter the amount you wish to withdraw: "))
        realbank.withdraw(withdraw)
        menu()
    elif choice == 4:
        return
    else:
        print("Please make a valid choice")
        menu()

# Instantiate a bank object
realbank = Bank()

# The app starts from the menu() function
menu()
