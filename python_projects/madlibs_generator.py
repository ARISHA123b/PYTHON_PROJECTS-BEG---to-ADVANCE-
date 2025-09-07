with open("story.txt" , "r") as f:
    story = f.read()

words = set()
start_of_the_word = -1 # means their is no word right now 
target_starts_with = "<"
targets_ends_with = ">"

for i, char in enumerate(story):
    if char == target_starts_with:
        start_of_the_word = i 
    if char == targets_ends_with and start_of_the_word != -1:
        word = story[start_of_the_word:i+1]
        words.add(word)
        start_of_the_word = -1

answers = {}
for word in words:
   answer = input("Enter the word: "+word+ ":")
   answers[word] = answer

for word in words:
    story = story.replace(word,answer[words])