from abc import ABC, abstractmethod

# Abstract Class
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass


# Bank Account Class
class BankAccount(Person):
    total_account = 0

    def __init__(self, name, account_no, balance):
        super().__init__(name)
        self.account_no = account_no
        self.__balance = balance
        BankAccount.total_account += 1

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Amount cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited Successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.__balance -= amount
            print("Amount Withdrawn Successfully.")

    def check(self):
        print("Current Balance:", self.__balance)

    def display_details(self):
        print("\n------ Account Details ------")
        print("Account Number :", self.account_no)
        print("Account Holder :", self.name)
        print("Balance        :", self.__balance)

    # Implement abstract method
    def display(self):
        self.display_details()

    @classmethod
    def show_total(cls):
        print("Total Accounts:", cls.total_account)

    @staticmethod
    def bank_rules():
        print("\n------ Bank Rules ------")
        print("Minimum Balance : 1000")
        print("Working Days    : Monday - Friday")
        print("Bank Hours      : 9 AM - 5 PM")
        print("Interest Rate   : 5%")


# Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, name, account_no, balance):
        super().__init__(name, account_no, balance)

    def display_details(self):
        super().display_details()


# Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_no = int(input("Enter Account Number: "))
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))

        if account_no in self.accounts:
            print("Account already exists!")
            return

        account = SavingsAccount(name, account_no, balance)
        self.accounts[account_no] = account
        print("Account Created Successfully.")

    def search(self):
        account_no = int(input("Enter Account Number: "))
        if account_no in self.accounts:
            return self.accounts[account_no]
        else:
            print("Account Not Found.")
            return None

    def deposit(self):
        account = self.search()
        if account:
            amount = float(input("Enter Deposit Amount: "))
            account.deposit(amount)

    def withdraw(self):
        account = self.search()
        if account:
            amount = float(input("Enter Withdrawal Amount: "))
            account.withdraw(amount)

    def display(self):
        account = self.search()
        if account:
            account.display_details()


# Main Program
bank = Bank()

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Bank Rules")
    print("6. Total Accounts")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        bank.create_account()

    elif choice == 2:
        bank.deposit()

    elif choice == 3:
        bank.withdraw()

    elif choice == 4:
        bank.display()

    elif choice == 5:
        BankAccount.bank_rules()

    elif choice == 6:
        BankAccount.show_total()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")