a = float(input("Enter the First Number: "))
b = float(input("Enter the Second Number: "))
ans1 = a+b
print("Addition of",a ,"and",b ,"is" ,ans1)
ans2 = a-b
print("Subtraction of",a,"and",b,"is",ans2)
ans3 = a*b
print("Multiplication of",a,"and",b,"is",ans3)
ans4 = a/b
print("Divison of",a,"and",b,"is",ans4)
ans5 = a//b
print("Floor of",a,"and",b,"is",ans5)
ans6 = a%b
print("Modulus of",a,"and",b,"is",ans6)
ans7 = a**b
print("Expotential of",a,"and",b,"is",ans7)



a = ("Nitesh","Prithish","Nuilesh")
for letters in a:
    print(letters)
    for q in letters:
        print(q)
        match q:
            case "t":
                print("Hii")
            case "P":
                print("Bye")
            case _ if q=="h":
                print("hello")
            