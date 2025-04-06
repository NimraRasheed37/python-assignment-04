import random


def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (h), too low (l), or correct (c)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print(f'yay! I guessed your number, {guess}, correctly!')
            
comp_guess(32)