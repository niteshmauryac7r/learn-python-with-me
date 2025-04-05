class Person:
    def __init__(self,name,age):
        self._age = age
        self.__name = name #name mangling

a = Person("Nitesh",27)
#print(a.__name)  cannot be accessed directly 
print(a._Person__name) #can be accessed indirectly

print(a._age)