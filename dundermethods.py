class Employee:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i = 0
        for item in self.name:
            i = i+1
         
        return i
    
    def __str__(self):
        return f"The name of Employee is {self.name}"
    
    def __repr__(self):
        return f"Employee('{self.name}')"
    
    def __call__(self, *args, **kwds):
        return self.name


a = Employee("Nitesh")

print(len(a))
print(str(a))
print(repr(a))
print(a.__call__())