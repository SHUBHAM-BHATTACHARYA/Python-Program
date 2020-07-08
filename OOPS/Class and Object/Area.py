class Rectangle:
    def getData(self,x,y):
        self.length=x
        self.width=y
    def rectArea(self):
        self.area=self.length*self.width
        return self.area
rect1=Rectangle()
rect2=Rectangle()
rect1.length=15
rect1.width=10
area1=rect1.length*rect1.width
rect2.getData(20,12)
area2=rect2.rectArea()
print("Area1= ",area1)
print("Area2= ",area2)
