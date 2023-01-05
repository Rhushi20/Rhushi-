import math
class ellipse:
    a=float(input("enter a number"))
    b=float(input("enter a number"))
    def area(self):
        print("area of ellipse is",3.14*self.a*self.b)
    def peremeter(self):
        print("peremeter of ellipse is",2*3.14*math.sqrt((self.a*self.a+self.b*self.b)/2))

c=ellipse()
x=c.area()
y=c.peremeter()
    
            
