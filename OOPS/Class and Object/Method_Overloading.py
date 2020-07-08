class overloading:
    def area(self,side):
        self.side=side
        self.area=self.side*self.side
        print("Area of Square= ",self.area)
    def area(self,length,breadth):
        self.length=length
        self.bradth=breadth
        self.area=self.length*self.breadth
        print("Area of Rectangle= ",self.area)
    def area(self,a,b,c):
        self.s=(a+b+c)/2
        self.area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Area of Triangle= ",self.area)
obj=overloading()
obj.area(5)
obj.area(6,5)
obj.area(2.5)
obj.area(2.0,3.0,4.0)
