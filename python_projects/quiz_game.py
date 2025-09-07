print("Welcome to the Quiz game you are at the correct place ")
playing = input("do you wanna play the game?  ")
if playing.strip().lower() != "yes":
    quit()
score = 0
answer = input("What does Cpu stands for ?  ")
if answer.strip().lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does RAM stands for ?  ")
if answer.strip().lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stands for ?  ")
if answer.strip().lower() == "graphics processing unit":
    print("correct")
    score += 1 
else:
    print("Incorrect")

answer = input("what does ROM stand for?  ")
if answer.strip().lower() == "read only memory":
    print("correct")
    score += 1 
else:
    print("Incorrect")
print("score is " + str(score))
print("your score is " +str((score /4 )* 100 )+ "%.")