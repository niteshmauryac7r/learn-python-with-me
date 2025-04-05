x = 10

def abc():
    global y 
    y = 5
    print(y)
    print(x)

abc()
print(x)
print(y)