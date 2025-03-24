

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(3))


def fibonacci_series(length):
    if length == 0:
        return 0
    elif length == 1:
        return 1
    else:
        return fibonacci_series(length - 1) + fibonacci_series(length - 2)
    
print(fibonacci_series(0))


a = "1234"

for i in a:
    print(i)