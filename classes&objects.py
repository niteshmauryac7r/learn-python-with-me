class Person:
    name = "Nitesh"
    occupation = "Python Developer"
    networth = "1000"
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Dharmesh"
a.occupation = "Software Developer"
print(a.name,a.occupation)
a.info()

b= Person()
b.name = "Nilesh"
b.occupation = "Frontend Developer"
print(b.name,b.occupation)
b.info()