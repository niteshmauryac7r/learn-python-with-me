def func1():
    try:
        a = int(input("Please enter the Number: "))
        b = [1,2,3]
        try:
            print(b[a])
        except IndexError:
            print("Index Error")
        for i in range(1,11):
            print(f"{a} x {i} = {int(a*i)}")
    except ValueError:
        print("Not an integer")
    finally:
        print("This will always be executed")
    return True

print(func1())