# Problem Statement: 
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll():
    for i in range(3):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Roll {i +1}: {dice1} and {dice2} = {dice1 + dice2}")
        
roll()
