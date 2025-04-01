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
        
