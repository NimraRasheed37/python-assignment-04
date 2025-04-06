import random

def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < random_number:
            print('Too low!')
        elif guess > random_number:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number.')

guess_number(30)