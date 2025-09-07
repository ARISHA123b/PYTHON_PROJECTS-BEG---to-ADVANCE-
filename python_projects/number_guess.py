import random 
top_of_range = input ("Enter the number :")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("plz type a number that is greater than 0")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0,top_of_range)
guesses_score = 0
while True:
    guesses_score += 1
    user_guess = input("Make a guess:")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number :")
        continue # rather than breaking it will bring us back to the top

    if user_guess == random_number:
        print("you got it right: ")
        break
    else:
        if user_guess > random_number:
            print("Let me help you , you were above the number ")
        else:
            print("your guess is lower than number")
print("you got it in ",guesses_score,"guesses.")