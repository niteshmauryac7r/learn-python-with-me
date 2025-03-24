'''
a = "Nitesh"
b = "Maurya"

print(a+b)
print("Hello", a , b) 
print(f"{a} {b}")
print(a + " " + b)
print("Hello", f"{a} {b}")


print(a[0])
print(b[2])
print(a[3])

for i in a:
    print(i)

#string slicing

print(len(a))
a = "Nitesh"
print(a[0:4])
print(a[-4:-3])
print(a[0:len(a)-1])
'''
b="1234"
a = "my name is nitesh maurya !!!!!!"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.rstrip("!"))
print(a.center(50))
print(a.replace("nitesh", "Dharmesh"))
print(a.split(" "))
print(a.endswith("!"))
print(a.endswith("is" , 1 , 6))
print(a.find("nitesh"))
print(b.isalnum())
print(b.isalpha())
print(b.isnumeric())
print(a.islower())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.swapcase())
print(a.startswith("my"))

for i in b:
    print(i)


d = int(input("Enter a number: "))

if(d>0):
    if(d>5 and d<10):
        print("Number is between 5 an 10")
    elif(d>=10 and d<=15):
        print("Number is between 10 and 15")
    else:
        print("Number is higher than 15")
else:
    print("Number is negative")


import time

timestamp = int(time.strftime("%H"))
print(timestamp)

if (timestamp > 6 and timestamp<12):
    print("good morning")
elif(timestamp >=12 and timestamp<=18):
    print("good evening")
else:
    print("Good night")
