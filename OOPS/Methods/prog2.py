class Methods():
    def __init__(self):
        self.name='SHUBHAM'
    def getName(self):
        return self.name
m=Methods()
print(m.getName())
print(Methods.getName(m))
