import random

def roll():
    min_value = 1
    max_value = 6  # Fix max_value to be 6 for the dice roll
    roll = random.randint(min_value, max_value)  # Roll a dice between 1 and 6
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input. Please enter a number.")

max_score = 50
player_scores = [0 for _ in range(players)]  # Initialize player scores to 0
print(player_scores)

# Main game loop: Runs until a player reaches the max_score
while max(player_scores) < max_score:
    for players_idx in range(players):
        print("\nPlayer number", players_idx + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[players_idx], "\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()  # Call the roll function to get the dice value

            if value == 1:
                current_score = 0
                print("You rolled a 1! Turn done.")
                break  # End the turn if the roll is 1
            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your score is:", current_score)
        
        player_scores[players_idx] += current_score
        print("Your total score is:", player_scores[players_idx])
                                                

        # Check if player has reached the max score, then break out of the loop
        if player_scores[players_idx] >= max_score:
            print(f"Player {players_idx + 1} has won with a score of {player_scores[players_idx]}!")
            break  # Break out of the loop if a player reaches the max score

# Determine the winner after the game loop ends
max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number", winning_index + 1, "is the winner with a score of:", max_score)
