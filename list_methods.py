l = [145,22,32,41,5,6,5]
print(l)

l.append(7)
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(5))

print(l.count(5))

m = l.copy()

print(m)

l.insert(2,"Hart")
print(l)

o = [100,6,3]

l.extend(o)
print(l)

l.remove("Hart")
print(l)