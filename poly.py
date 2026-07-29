#method overiding
class animal:
    def sound(self):
        print("animal sound")
class Dog(animal):
    def sound(self):
        print("Bark")
class Cat(animal):
    def sound(self):
        print("Meow")
d=Dog()
c=Cat()
d.sound()
c.sound()


#Duck typing example
class animal:
    def sound(self):
        print("animal sound")
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
def make_sound(animal):
        animal.sound()
make_sound(Dog())
make_sound(Cat())

#method overloading
class cal:
    def add(self, a, b,c=0,d=0):
        return a+b+c+d
    def add(self,a,b,c,d=0):
        return a+b+c+d
obj=cal()

print(obj.add(10,20,0,0))
        


