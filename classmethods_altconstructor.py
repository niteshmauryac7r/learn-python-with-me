class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("_")[0],int(string.split("_")[1]))
string = "Nitesh_27"
a = Person(string.split("_")[0],int(string.split("_")[1]))

print(a.name,a.age)


b = Person.fromstr(string)
#print(b.name,b.age)
print(b.name, b.age)