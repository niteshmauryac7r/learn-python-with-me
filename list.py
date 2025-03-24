marks = [24,23,21,2,5,6,7,8,0]
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])



print(marks[-2])

if 24 in marks:
    print("Number is present")
else:
    print("Number is not present")
#same thing applies for string as well
print(len(marks))
print(marks[0:-3:2])

a = [i for i in range(1,10) if i%2==0]
print(a)