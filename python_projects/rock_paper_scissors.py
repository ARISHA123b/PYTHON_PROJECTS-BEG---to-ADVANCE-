import random


user_wins = 0 
computer_wins = 0

options = ["rock", "paper","scissors"]

while True:

    user_input = input("Type Rock/Paper/Scissors or Q to quit:").lower()
    if user_input == "q":
       break
    
    if user_input not in options:
        continue # what till will do is it keep asking to print something valid

    random_number = random.randint(0,2)
    #0 for rock , 1 for paper , 3 for scissors 
    computer_pick = options[random_number]
    print("Computer picks :" ,computer_pick +"." )
    if user_input == "rock" and computer_pick =="scissors":
        print("you won :) computer lose")
        user_wins += 1 
    elif user_input == "paper" and computer_pick == "rock":
        print("you win :) computer losse ")
        user_wins +=1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won :) computer wins")
        user_wins+=1
    else :
        print("you lost!")
        computer_wins +=1

print("you won", user_wins,"times.")
print("The computer won ", computer_wins , "times.")
print("Good bye")
