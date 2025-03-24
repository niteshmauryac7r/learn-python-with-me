s = {2,3,41,2,1}
print(s)
t = set()
print(type(t))

for i in s:
    print(i)


s1 = {1,2,3,4}
s2 = {2,5,6,1}

print(s2.union(s1))
s1.update(s2)
print(s1)


print(s1.intersection(s2))
s.intersection_update(s1)
print(s)

print(s1.symmetric_difference(s2))

a = {1,2,3,4}
b = {1,6,5,7}

print(a.difference(b))

print(a.isdisjoint(b))
print(a.issuperset(b))
print(a.issubset(b))
a.add('Nitesh')
print(a)
a.remove("Nitesh")
print(a)
a.discard("Nitesh")
print(a)


item = a.pop()
print(a)
print(item)

#del a
#print(a)

s.clear()
print(s)

