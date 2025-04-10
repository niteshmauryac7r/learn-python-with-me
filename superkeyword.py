class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def info(self):
        print(f"The name of employee is {self.name} and his id is {self.id}")

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__( name,id)
        self.lang = lang

    def info(self):
        super().info()
        



a = Employee("Nitesh",1)
b = Programmer("Dharmesh",2,"Python")

print(b.name,b.id,b.lang)

b.info()