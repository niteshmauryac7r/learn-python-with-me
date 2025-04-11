a = 2
print(a:=3)  # :=walrus operator

numbers = [1,2,3,4,5]

while (n:=len(numbers))>0:
    numbers.pop()
    print(numbers)

fruit = []
while (food :=input("What fruit do u like")) != "quit":
    fruit.append(food)
    
print(fruit)    