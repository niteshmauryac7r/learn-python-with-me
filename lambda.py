double  = lambda x : x*2
cube  = lambda x: x*x*x
print(double(2))
print(cube(4))

def apply(f,value1,value2,value3):
    return 6 + f(value1,value2,value3)

print(apply(lambda x,y,z: (x+y+z)/3 ,1,2,3 ))