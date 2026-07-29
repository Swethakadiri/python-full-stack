class Name:
    def __init__(self, name):
        self.name = name
class Marks(Name):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks
s1 = Marks("Ravi", 92)
print("Name:", s1.name)
print("Marks:", s1.marks)


#example
class Wallet:
    def __init__(self, deposit, show_money):
        self.__deposit = deposit
        self.__show_money = show_money

    def display(self):
        print("Deposit:", self.__deposit)
        print("Show Money:", self.__show_money)
s = Wallet(500, 1500)
s.display()



#examples
class Atm:
    def __init__(self, deposit):
        self.__deposit = deposit

    def get_deposit(self):
        return self.__deposit

class Deduct(Atm):
    def __init__(self, deposit, withdraw):
        super().__init__(deposit)
        self.__withdraw = withdraw

    def balance(self):
        remaining = self.get_deposit() - self.__withdraw
        print("Deposit:", self.get_deposit())
        print("Withdraw:", self.__withdraw)
        print("Remaining Balance:", remaining)

s = Deduct(10000, 3000)
s.balance()
