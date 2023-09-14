# GitHub: SFhectorj
# Skills Used: Importing modules, creating and using lists, if statements, conditionals, randomization
# Description: This is a Paper, Scissors, Rock game where the user inputs a number to select their choice.
#              The game will randomly generate a rebuttal choice and depending on will result in win, lose, or draw.

import random
import sys

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Since the images will be used by multiple variables, it's easier to compile it into a list
# that can be accessed by said variables.
game_images = [paper, scissors, rock]

user_move = int(input("Which do you choose? Type 0 for Paper, 1 for Scissors, 2 for Rock:\n"))
if user_move >= 3 or user_move < 0:
    # Using the exit function prevents from incorrect user inputs.
    # The function is imported from the sys module
    sys.exit("Input not recognized, please restart program and try again.")
else:
    print(game_images[user_move])

# In order to generate a random number for the COM to use we import from the random module
# and use the random and randint functions.
com_player = random.randint(0, 2)
print("Computer chooses:")
# The random number generated is then used to select the proper image
print(game_images[com_player])

# This block is where the logic for the game is implemented using if statements
if user_move == com_player:
    print("DRAW")
if user_move == 0 and com_player == 1\
        or user_move == 1 and com_player == 2\
        or user_move == 2 and com_player == 0:
    print("COMPUTER WINS!")
elif user_move == 0 and com_player == 2\
        or user_move == 1 and com_player == 0\
        or user_move == 2 and com_player == 1:
    print("YOU WIN!")
