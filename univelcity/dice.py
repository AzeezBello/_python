import random

player_score = 0
ai_score = 0
turns = 0

print('Hit enter to play')
start = input()

while turns < 3:

    player_die1 = random.randint(1,6)
    player_die2 = random.randint(1,6)
    player_score = player_score + player_die1 + player_die2


    ai_die1 = random.randint(1,6)
    ai_die2 = random.randint(1,6)
    ai_score = ai_score + ai_die1 + ai_die2

    print(f"Player rolled {player_die1}  and {player_die2}")
    print(f"Computer rolled {ai_die1}  and {ai_die2}")
    
    turns += 1
    roll_again = input('Hit Enter to roll dice again')


print(f"Player scored {player_score}  Computer scored {ai_score}")

if player_score > ai_score :
    print("You win") 

elif player_score == ai_score:
    print("No winner")

else:
    print("You lose")