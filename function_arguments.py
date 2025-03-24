def AverageofTwonum(num1=1,num2=8):
    avg = (num1+num2)/2
    return avg

a = AverageofTwonum(num2=10)
print(a)


def AverageofMultipleNumber(*num):
    sum =0
    for i in num:
        sum = sum+i
    return sum/2

b = AverageofMultipleNumber(1,2,3,4,5)
print(b)


def Fullname(**name):
    print(type(name))
    
    print("Hello,", name["fname"], name["mname"], name["lname"])



Fullname(fname = "Nitesh", mname= "Chandrakant", lname= "Maurya")


