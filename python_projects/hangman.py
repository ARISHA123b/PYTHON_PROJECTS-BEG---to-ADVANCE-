import random 
import hangman_stages
word_list = ["apple", "strawberry", "mango", "peach", "kiwi"]
lives = 6 
choosen_word = random.choice(word_list)

print(choosen_word)

display = []

for letter in range(len(choosen_word)):
    display+="_"
print(display)
game_over = False
while not game_over:

   guessed_letter = input("enter a letter ").lower()

   for position in range(len(choosen_word)):#apple
        letter = choosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
   print(display)        
   if guessed_letter not in choosen_word:
       lives-=1
       if lives == 0 :
            game_over = True
            print("you lose ")

   if '_' not in display:
    game_over = True
    print("You win")
  
   print(hangman_stages.stages[lives])                                                                   