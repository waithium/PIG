#PIG game (multiplayer)
'''
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

while max(player_scores) < max_score:
    for i in range(players):
        print(f'player {i+1}\'s turn:')
        current_score = 0

        while True:
            should_dice_roll = input('do you want to roll the dice? (y/n): ')
            
            if should_dice_roll.lower() != 'y':
                break

            value = dice_roll()
            if value == 1:
                print(f'you rolled a {value}, you lost this round :( your score will be reseted!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'you rolled a {value}')
        

            player_scores[i] += current_score
            print(f'your total score is {player_scores[i]}')

            # current_score += value
            # print(f'your total score = {player_scores[i]}!!')
'''

import random

# Function to roll the dice
def dice_roll():
    min_num = 1
    max_num = 6
    return random.randint(min_num, max_num)

# Inputting the number of players for the game
while True:
    players = input('Please enter the number of players for this game (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print(f'{players} is an invalid option!! Enter a value between 2 and 4')

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for i in range(players):
        print(f'Player {i+1}\'s turn:')
        current_score = 0

        while True:
            should_dice_roll = input('Do you want to roll the dice? (y/n): ')
            
            if should_dice_roll.lower() != 'y':
                break

            value = dice_roll()
            if value == 1:
                print(f'You rolled a {value}, you lost this round :( Your score will be reset!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a {value}')

            print(f'You scored {current_score} in this round')

            player_scores[i] += current_score
            print(f'Your total score is {player_scores[i]}')

            if player_scores[i] >= max_score:
                print(f'Player {i+1} wins with a score of {player_scores[i]}!')
                exit()
