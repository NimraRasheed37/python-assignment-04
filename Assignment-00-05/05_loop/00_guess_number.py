# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

def guess_my_number():
    number_to_guess = random.randint(0, 99)
    guess = None
    
    while guess != number_to_guess:
        guess = int(input("Enter a guess: "))
        
        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess >number_to_guess:
            print("Your guess is too high")
        else:
            print(f"Congratulations! You got it. The number was: {number_to_guess}")


guess_my_number()