class Employee:
    def __init__(self,name,id):
        self._name = name
        self._id = id

    def showinfo(self):
        print(f"The name of employee {self._id} is {self._name}")

    
class Programmer(Employee):
    def showLanguage(self):
        print(f"The coding language is python which is used by {self._name}")

e1 = Employee("Nitesh",1)
e2 = Programmer("Dharmesh",2)
e1.showinfo()
e2.showLanguage()
e2.showinfo()




