import random
from words import words

def hangman():
    # choose random word from words module
    word = random.choice(words).upper()
    word_letters = set(word) 
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()
    
    lives = 7
    print("\n ========== Welcome to Hangman!==========")
    print("      You have 7 lives to guess the word.")
    print("          The word has", len(word), "letters.")
    print("           You can use letters A-Z.")
    print("     ========= Let's start! =========\n")
    
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left.")
        print("Used letters:", ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))
        
        guess = input("Guess a letter: ").upper()
        
        if guess in used_letters:
            print("You already guessed that letter. Try again.")
        elif guess not in alphabet:
            print("Invalid input. Please enter a letter A-Z.")
        else:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Good guess!")
            else:
                lives -= 1
                print("Wrong guess!")
                
       # End of game messages
    if lives == 0:
        print("You ran out of lives! The word was:", word)
    else:
        print("Congratulations! You guessed the word:", word)
hangman()