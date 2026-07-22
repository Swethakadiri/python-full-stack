balance=10000
while True:
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
    choice=int(input("enter a number"))
    if choice==1:
        print("current balance:",balance)
    elif choice==2:
        amount=float(input("enter amount"))
        balance=balance+amount
        print("new balance",balance)
    elif choice==3:
        amount=float(input("enter a amount"))
        if amount <= balance:
            balance=balance-amount
            print("withdraw balance:", balance)
        else:
            print("insufficient balance")
    elif choice == 4:
        break
    else:
        print("invalid choice")