tup = (1,True,2,6,8,1,"Nitesh")
#tuple are immutable if there is one object in tuple it should end in comma for python to recognize it has a tuple
print(type(tup), tup)

print(tup[2:-2])

if "Nitesh" in tup:
    print("Hello, Nitesh")
else:
    print("He is not here")

tup2 = ("Harry", "Yolo", False)

tup3 = tup+tup2

print(tup3)

c = list(tup)
c.append(4)
c.pop(5)
tup=tuple(c)

print(tup)

print(tup.count(1))
print(tup.index(2))
print(tup.index(1,0,5))
print(len(tup))

