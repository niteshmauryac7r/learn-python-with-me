import random

computer_option = ["snake", "gun","water"]

user_score = 0
computer_score = 0


while True:
    user_option = input("Enter the string ")
    computer_input = random.choice(computer_option)
    print(f"Computer pick is {computer_input}")
    if user_option == "snake":
        if user_option == computer_input:
            print("Draw")
        elif computer_input == "gun":
            print("Gun Kills Snake,Computer wins")
            computer_score = computer_score + 1
        else:
            print("snake drinks water,User win")
            user_score = user_score + 1
    elif user_option == "gun":
        if user_option == computer_input:
            print("Draw")
        elif computer_input == "snake":
            print("Gun Kills Snake, User win")
            user_score = user_score + 1
        else:
            print("Water spoils gun,computer win ")
            computer_score = computer_score + 1

    elif user_option == "water":
        if user_option == computer_input:
            print("Draw")
        elif computer_input == "snake":
            print("snake drinks water, Computer win")
            computer_score = computer_score + 1
        else:
            print("Water spoils gun,User win ")
            user_score = user_score + 1
    
    else:
        break
    

print(f"Player Score is {user_score}")
print(f"Computer Score is {computer_score}")


    
    