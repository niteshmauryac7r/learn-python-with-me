class Animal:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def makesound(self):
        return f"The animal makes a sound"
    

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name,breed)

    def makesound(self):
        return f"Dog barks"
    
a = Animal("Cat","Feline")

b = Dog("Sheru","Husky")

print(a.makesound())
print(b.makesound())

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name,breed)

    def info(self):
        return f"The name of the cat is {self.name} and breed is {self.breed}"
    
c = Cat("Payal","Paltu")
print(c.info())