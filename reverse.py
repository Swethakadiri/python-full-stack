a = int(input("Enter a number: "))
reverse = 0
while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10
print("Reversed Number =", reverse)