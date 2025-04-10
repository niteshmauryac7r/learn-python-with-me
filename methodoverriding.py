class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area()
    
Rect = Shape(2,3)

print(Rect.area())

Circ = Circle(4)
print(Circ.radius)
print(Circ.area())


# 📝 Requirements:
# Create a base class Creature with a method speak() that returns:
# "The creature makes a sound."
# Create subclasses:
# Wolf → speak() returns "The wolf howls!"
# Bird → speak() returns "The bird chirps!"
# Snake → speak() returns "The snake hisses!"
# Write a function forest_conversation(creatures) that takes a list of Creature objects and calls speak() on each one.

class Creature:
    Total_Creature = 0
    def __init__(self,name):
        self.name = name
        Creature.Total_Creature +=1
        
    def speak(self):
        return f"The {self.name} make a sound"
        
    @classmethod
    def CreatureCount(cls):
        return Creature.Total_Creature
        
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"
        
class Wolf(Creature):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        return f"The wolf {self.name} howls!"
        
    def __str__(self):
        return super().__str__()
        
class Bird(Creature):
    def __init__(self,name):
        super().__init__(name)
        
    def speak(self):
        return f"The bird {self.name} chirps!"
        
    
    def __str__(self):
        return super().__str__()        
    
        
class Snake(Creature):
    def __init__(self,name):
        super().__init__(name)
        
    def speak(self):
        return f"The snake {self.name} hisses!"
        
    def __str__(self):
        return super().__str__()
        
def forest_conversation(creatures):
    for creature in creatures:
        print(creature.speak())
        print(str(creature))
        
creatures = [Wolf("nitesh"), Bird("qwe"), Snake("ssdf"), Creature("ghjv")]
forest_conversation(creatures)

print(Creature.Total_Creature)


        
        