"""
for i in range(13):
    
    if i==7:    
        continue
    print("5 x",i,"=",5*i)
    

i = 0

while(i<4):
    print(i)
    if i==2:
        break
    i = i+1


    
i = 8

while True:
    print(i)
    i = i+1
    if i ==10:
        break


total = 0
while True:
    a = int(input("Enter a Number: "))
    
    if a == -1:
        break
    total =total + a

print(total)

"""
for num in range(2, 51):  # Iterate from 2 to 50
    is_prime = True  # Assume the number is prime
    for i in range(2, num):  
        if num % i == 0:  # If divisible, it's not prime
            is_prime = False
            break  # Exit inner loop early if a factor is found
    if is_prime:
        print(num, end=" ")


