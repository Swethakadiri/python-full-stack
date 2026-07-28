class emp:
    def  __init__(self,empname,empid,empsalary,empdept):
        self.empname=empname
        self.empid=empid
        self.empsalary=empsalary
        self.empdept=empdept
s1=emp("swetha","118","50000","IT")
print(s1.empname)
print(s1.empid)
print(s1.empsalary)
print(s1.empdept)



#area of circle
class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return circle.pi*self.radius**2
    
s=circle(5)
print(s.area())


#triangle
class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
s=triangle(2,6)
print(s.area())



#class method
class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()


#static method
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(10, 20))


#Inheritance
class parent:
    def parent(self):
        print("this is a parent class")
class child(parent):
    def child(self):
        print("this is a child class")
obj=child()
obj.parent()
obj.child()

#multiple inheritance
class father:
    def show(self):
        print("this is a parent class")
class mother():
    def show1(self):
        print("this is a child class")
class child(father,mother):
    def show2(self):
        print("this is a multiple inheritance")
obj=child()
obj.show()
obj.show1()
obj.show2()

#multilevel
class father:
    def show(self):
        print("this is a parent class")
class mother(father):
    def show1(self):
        print("this is a child class")
class child(mother):
    def show2(self):
        print("this is a multiple inheritance")
obj=child()
obj.show()
obj.show1()
obj.show2()


#example
class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class product1(product):
    def __init__(self,name,price,warranty):
        super().__init__(name, price)
        self.warranty=warranty
s=product1("laptop","80000","2")
print(s.name)
print(s.price)
print(s.warranty)

#example
class emp:
    def __init__(self,empname,empid):
        self.empname=empname
        self.empid=empid
class emp1(emp):
    def __init__(self,empname,empid,programminglanguage):
        super(). __init__(empname,empid)
        self.programminglanguage=programminglanguage
class emp3(emp1):
    def __init__(self,empname,empid,programminglanguage,teamsize):
        super(). __init__(empname,empid,programminglanguage)
        self.teamsize =teamsize
s1=emp3("swetha","2","python","4")
print(s1.empname)
print(s1.empid)
print(s1.programminglanguage)
print(s1.teamsize)

#example
class phone:
    def __init__(self,iphone):
        self.iphone=iphone
class phone1(phone):
    def __init__(self,iphone,capturing):
        super(). __init__(iphone)
        self.capturing=capturing
class phone5(phone1):
    def __init__(self,iphone,capturing,calling):
        super(). __init__(iphone,capturing)
        self.calling=calling
s3=phone5("iphone","image","calling")
print(s3.iphone)
print(s3.capturing)
print(s3.calling)



#practice
class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,roll):
        self.roll=roll
s=student("rahul","101")
print(s.name)
print(s.roll)
