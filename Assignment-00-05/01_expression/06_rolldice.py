# Problem Statement:
# Simulate rolling two dice, and prints results of each roll as well as the total.

import random
def dice_roll():
    # generate random number between 1 to 6 for dice 1 and dice 2
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    # print result of dice 1 , dice 2 and total of both dice
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total: {dice1 + dice2}")
    
dice_roll()