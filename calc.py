def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a == 0:
        return "cannot divide by zero"
    return a/b
def  mod(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a%b
def power(a,b):
    return a**b
while True:
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.mod")
    print("6.power")
    print("7.exit")
    choice=int(input("enter a choice:"))
    if choice == 7:
        print("calculator closed")
        break
    if choice < 1 or choice > 7:
        print("Invalid input")
        continue
    num1=float(input("enter a number:"))
    num2=float(input("enter a number:"))
    if choice == 1:
        print("Result: ",add(num1,num2))
    elif choice == 2:
        print("Result: ",sub(num1,num2)) 
    elif  choice == 3:
        print("Result: ",mul(num1,num2)) 
    elif  choice == 4:
            print("Result: ",div(num1,num2))
    elif  choice == 5:
                print("Result: ",mod(num1,num2))
    elif  choice == 6:
                    print("Result: ",power(num1,num2))
               