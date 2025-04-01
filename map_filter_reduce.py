from functools import reduce

#MAP
def cube(num):
    return num*num*num

l = [1,2,3,4]
newl = list(map(cube,l))
print(newl)

# FILTER

def greater(num):
    return num > 2

newnewl = list(filter(greater, l))
print(newnewl)

#REDUCE

sum  = reduce(lambda x,y: x+y, l)
print(sum)
