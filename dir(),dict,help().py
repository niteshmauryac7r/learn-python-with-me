x = [12,34]

print(dir(x))
#print(help(x))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = Person("Nitesh",27)
b = Person("Dharmesh",27)
print(b.__dict__)

print(help(Person))