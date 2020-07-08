class Rectangle():
    def __init__(self,x,y):
        self.length=x
        self.width=y
    def rectArea(self):
         return (self.length*self.width)
rect=Rectangle(15,10)
area=rect.rectArea()
print("Area= ",area)
