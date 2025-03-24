y = int(input("Please enter a number: "))

match y:
    case 0:
        print("the number is zero")
    case _ if y>0:
        print("The number is positive")
    case _ :
        print("the number is negative")


b = ("red","yellow","green")
for i in b:
    print(i)
    for c in i:
        print(c)
        match c:
            case "r":
                print("nothing good")
            case "e":
                print("awesome")
            case _:
                print("qwerty")




