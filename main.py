#PIG game (multiplayer)
import random

# function to roll the dice
def dice_roll():
    min_num = 1
    max_num = 6
    return random.randint(min_num,max_num)

# inputing the number of players for the game
while True:
    players = input('please eneter the number of players for this game(2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4 :
            break
        else:
            print(f'{players} is an invalid option!! enter a value between 2 and 4')
            # continue

max_score = 50
player_scores = [0 for i in range(players)]

while player_scores < max_score:
    for i in range(players)
        should_dice_roll = input('do you want to roll the dice? (y/n)')
        if should_dice_roll.lower() != 'y':
            break

        while True:
            