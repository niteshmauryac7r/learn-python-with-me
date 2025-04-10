class Animal:
    def __init__(self,name):
        self.name = name

    def showinfo(self):
        return f"Name : {self.name}"
    

class Dog(Animal):
    def __init__(self, name, species):
        Animal.__init__(self, name)
        self.species = species

    def showinfo(self):
        print(super().showinfo())
        return f"Species: {self.species}"
    
class Husky(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name,species="Husk")
        self.color = color

    def showinfo(self):
        print(super().showinfo())
        return f"Color : {self.color}"
    

a = Husky("Tommy", "Black")
print(a.showinfo())



# Create the following class structure:

# Class Vehicle (Base Class)
# Attributes: brand, model
# Method: show_info() → prints "Brand: <brand>, Model: <model>"
# Class Car (Inherits from Vehicle)
# Additional Attribute: seats
# Override show_info() to also include "Seats: <seats>"
# Class ElectricCar (Inherits from Car)
# Additional Attribute: battery_capacity (in kWh)
# Override show_info() to also include "Battery: <battery_capacity> kWh"

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def showinfo(self):
        return f"Brand: {self.brand}\nModel:{self.model}"
    
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats = seats

    def showinfo(self):
        
        return f"{super().showinfo()} \nSeats: {self.seats}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, seats,battery_capacity):
        super().__init__(brand, model, seats)
        self.battery_capacity = battery_capacity

    def showinfo(self):
        return f"{super().showinfo()} \nBattery Capacity: {self.battery_capacity}"
    
a = ElectricCar("Tesla","x5","4","120kwh")

print(a.showinfo())

    