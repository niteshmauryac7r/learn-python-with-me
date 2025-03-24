def CalculateGmean(num1,num2):
    gmean = (num1+num2)/(num1*num2)
    return gmean
    
def IsGreater(num1, num2):
    if num1>num2:
        print("First Number is greater than second Number")
    elif num1==num2:
        print("First Number is equal to the second Number")
    else:
        print("Second number is greater than first number")

def Islesser(num1,num2):
    pass

if __name__ == "__main__":
    print(CalculateGmean(1,4))