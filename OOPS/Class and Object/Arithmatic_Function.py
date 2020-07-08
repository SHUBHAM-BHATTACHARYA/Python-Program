class Arithmatic:
    def input(self):
        self.x=int(input("Enter the x: "))
        self.y=int(input("Enter the y: "))
    def add(self,x,y):
        self.x=x
        self.y=y
        result=self.x+self.y
        print("Sum= ",result)
    def sub(self,x,y):
        self.x=x
        self.y=y
        result=self.x-self.y
        print("Sub= ",result)
    def mul(self,x,y):
        self.x=x
        self.y=y
        result=self.x*self.y
        print("Mul= ",result)
    def div(self,x,y):
        self.x=x
        self.y=y
        result=self.x/self.y
        print("Div= ",result)
obj=Arithmatic()
obj.input()
obj.add(obj.x,obj.y)
obj.sub(obj.x,obj.y)
obj.mul(obj.x,obj.y)
obj.div(obj.x,obj.y)
