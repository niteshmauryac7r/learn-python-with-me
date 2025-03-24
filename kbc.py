questions = ["Who is the father of our nation?","Total Number of Continents ?",
        "Capital of USA?","National Bird of India?"]

options = [["MK Gandhi", "Sardar Patel", "Nehru", "Bhagat Singh"],
           [1,5,3,7],
           ["Washington DC", "New Delhi", "Moscow", "London"],
           ["Tiger","Crow","Peacock","Pigeon"]]

answer = ["MK Gandhi", 7, "Washington DC", "Peacock"]

price = 0

try:
    for i in range(len(questions)):
        print(questions[i])
        
        for j, option in enumerate(options[i],1):
            print(f"{j}. {option}")
            
        a = int(input("Enter the option "))
        
        a = a - 1
        
        if options[i][a] == answer[i]:
            print("Correct answer")
            price = price + 5000
        else:
            print("Wrong answer")
            break   

except Exception as e:
    print(e)
    
finally:
        print(price)