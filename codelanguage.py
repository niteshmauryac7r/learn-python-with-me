import random
import string

def Encoding(a):
    a = list(a)
    if len(a) >=3:
        a.append(a[0])
        a.remove(a[0])
        random_start = random.choices(string.ascii_letters, k=3)
        random_end = random.choices(string.ascii_letters, k=3) 
        a = random_start + a + random_end
        
    else:
        a.reverse()
    a = ''.join(a)  
    print(a)  
    return a
    
def Decoding(b):
    b = list(b)
    if len(b)<3:
        b.reverse()
    else:
        b = b[3:-3]
        c = b.pop()
        b.insert(0,c)
    b = ''.join(b)
    print(b)
        
        
user_input = input("Please enter the text: ")        
Encoding(user_input)
Decoding(Encoding(user_input))