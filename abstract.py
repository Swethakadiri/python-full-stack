from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
r=rectangle(10,5)
r.area()


#circle
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        
        self.radius=radius
    def area(self):
        print("Area of circle:",3.14*self.radius*self.radius)
c=circle(2)
c.area()

#without abstract method

class shape():
    @abstractmethod
    def area(self):
        print("area method")
class circle(shape):
    def __init__(self,radius):
        
        self.radius=radius
    def area(self):
        print("Area of circle:",3.14*self.radius*self.radius)
c=circle(2)
c.area()
