class Math:
    def __init__(self,num):
        self._num = num

    def addtonum(self, num2):
        self._num = self._num + num2
        return self._num

    @staticmethod
    def add(a,b):
        return a+b
    

a = Math(12)
print(a.addtonum(2))

print(a.add(1,2))
print(Math.add(2,4))