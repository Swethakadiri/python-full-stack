actualamout=int(input("enter a number:"))
removeamount=int(input("enter a number:"))
if removeamount <= actualamout:
    availablebalance=actualamout - removeamount
    print("available balance:",availablebalance)
else:
    print("insufficient balance")