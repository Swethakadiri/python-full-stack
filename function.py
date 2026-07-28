a=[12,3,4,4,9]
b=list(filter(lambda x: x%2 !=0,a))
print(b)

#map
a=[1,12,5,7,9]
b=list(filter(lambda x: x %2 !=0,a))
c=list(map(lambda x:x**2,a))
print(b)
print(c)

#recursion
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(8))



#fibonacci
def fibonacci(n):
    if n==0  or n==1:
        return 1
    return fact(n-1),(n-2)
print(fact(1))


#set
s={1,3,7,8,9}
s.add(4)
s.remove(3)
print(s)

#dictionary
d={
    "id":8,
    "name":"swetha",
    "course":"mca"
  }
print(d)


#list
a=[2,5,7,8,9,9,9,5]
for i in a:
    print(i)

#string
s="hello"
print(s[::2])

s="hello world"
print(s.title())
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.find('python'))
print(s.startswith("hel"))


#VOWELS
a="swetha"
count=0
for i in a:
    if i in "aeiou":
        count=count+1
        print(i,"vowels")
    else:
        print(i,"consonants")
print("no of vowels:",count)

