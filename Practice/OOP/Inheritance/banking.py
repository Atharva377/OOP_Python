# Parent class: BankAccount
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")

# Child class: SavingsAccount inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_holder, balance)  # Inheriting from the parent class
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")
        
check = SavingsAccount("Atharva",5000)
print(check.account_holder)
print(check.balance)
check.add_interest()