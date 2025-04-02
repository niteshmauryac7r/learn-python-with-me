class MyClass:
    def __init__(self,value):
        self.value = value

    def show(self):
        print(f"{self.value} is a Number")

    @property      
    def Ten_X_value(self):
        return 10 * self.value
    
    @Ten_X_value.setter
    def Ten_X_value(self, new_value):
        self.value = new_value/10


    
a = MyClass(10)
a.show()
print(a.Ten_X_value)

a.Ten_X_value = 78
a.show()


# Bank Account
class BankAccount:
    def __init__(self,bank_balance):
        self._bank_balance = bank_balance
    
    @property
    def ShowBalance(self):
        return self._bank_balance
    
    @ShowBalance.setter
    def ShowBalance(self, New_Balance):
        if isinstance (New_Balance,int) and New_Balance>0:
            self._bank_balance = New_Balance
            return self._bank_balance
        else:
            raise ValueError("Value Must be Integer")
        
Nitesh = BankAccount("10")
print(Nitesh.ShowBalance)

Nitesh.ShowBalance = 55
print(Nitesh.ShowBalance)


#1️⃣ Temperature Converter
# Create a Temperature class that:

# Stores temperature in Celsius.
# Provides a getter method to retrieve the temperature in Fahrenheit.
# Provides a setter method that allows setting the temperature in Celsius, but prevents setting values below absolute zero (-273.15°C).
class Temperature:
    def __init__(self,celsius):
        self._celsius = celsius
        
        
    def info(self):
        print(f"Current temperature is {self._celsius} C ")
    
    @property  
    def temp(self):
        celsius = self._celsius
        return celsius
    
    @property
    def fahrenheit(self):
        result = (self._celsius * 1.8) + 32
        return result
        
    @temp.setter
    def temp(self, celsius_new):
        if celsius_new > 0:
            self._celsius = celsius_new
        else:
            raise ValueError("Should be greater than 0")
    
t = Temperature(33)

print(t.fahrenheit)

# 3️⃣ Car Speed Controller
# Create a Car class that:

# Stores the speed of the car.
# Allows setting the speed, but limits it to a maximum of 200 km/h.
# Provides a getter method to retrieve the current speed.

class Car:
    def __init__(self,speed):
        self._speed = speed
    
    def info(self):
        print(f"Speed of Car is {self._speed}")
        
    @property
    def CurrentSpeed(self):
        speed = self._speed
        return speed
        
    @CurrentSpeed.setter
    def CurrentSpeed(self, new_speed):
        if new_speed <=200:
            self._speed = new_speed
        else:
            raise ValueError("Maximum speed is 200km/hr")
        
            
        
bmw = Car(200)

bmw.info()

print(bmw.CurrentSpeed)

bmw.CurrentSpeed = -2

print(bmw.CurrentSpeed)



        
