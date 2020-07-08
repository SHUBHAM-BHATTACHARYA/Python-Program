class cat:
    def __init__(self,name):
        self.name=name
missy=cat('Missy')
lucky=cat('Lucky')
print(missy.name)
print(lucky.name)

class Person():
    pass
p=Person()
p.age=24
p.name="Peter"
print("{0} is {1} year old".format(p.name,p.age))
