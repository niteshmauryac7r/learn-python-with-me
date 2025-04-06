class Employee:
    companyname = "Apple"
    def showinfo(self):
        print(f"The name of employee is {self.name} and company name is {self.companyname}")

    @classmethod
    def changeCompany(cls,newName):
        cls.companyname = newName


e1 = Employee()
e1.name = "Nitesh"

e1.showinfo()

e1.changeCompany("Tesla")
e1.showinfo()
print(Employee.companyname)