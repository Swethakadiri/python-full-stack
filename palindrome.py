a = int(input("Enter a number: "))
temp = a
c = 0

while a > 0:
    b = a % 10
    c = c * 10 + b
    a = a // 10

if temp == c:
    print("Palindrome")
else:
    print("Not Palindrome")