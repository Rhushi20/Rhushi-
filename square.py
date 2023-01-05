class square:
    var=float(input("enter the side"))
    def area(self):
        print("the area of square is:",self.var*self.var)

    def peremeter(self):
        print("the peremeter of square is:",4*self.var)


c=square()
x=c.area()
y=c.peremeter()
