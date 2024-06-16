import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissor"]
# rock : 0, paper : 1, scissor : 2

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit : ").lower()

    if user_input == "q":
        break

    if user_input not in options :
        print("Invalid Input")
        continue;

    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print("computer picked ", computer_pick , "." )


    if user_input == "rock" and computer_pick == "scissor" :
        print("You won!!")
        user_score += 1

    elif user_input == "paper" and computer_pick == "rock" :
        print("You won!!")
        user_score += 1

    elif user_input == "scissor" and computer_pick == "paper" :
        print("You won!!")
        user_score += 1

    elif user_input == computer_pick :
        print("Try again!!")
        

    else:
        print("You lost!!")
        computer_score += 1
    
print("You won", user_score ,"times!!" )
print("Computer won" , computer_score  ,"times!!" )




    
