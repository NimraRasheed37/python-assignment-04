import random

def is_win(player, computer):
    """Returns True if player wins against opponent."""
    return (player == 'r' and computer == 's') or \
           (player == 's' and computer == 'p') or \
           (player == 'p' and computer == 'r')

def play():
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    while True:
        user = input("Enter your choice ('r' for rock, 'p' for paper, 's' for scissors): ").lower()
        if user not in choices:
            print("Invalid input. Please choose 'r', 'p', or 's'.")
            continue

        computer = random.choice(['r', 'p', 's'])

        print(f"You chose {choices[user]}, and the computer chose {choices[computer]}.")

        if user == computer:
            print("It is a tie!")
        elif is_win(user, computer):
            print("You Won!")
        else:
            print("You lost!")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes' and again != 'y':
            print("Thanks for playing!")
            break

# Start the game
play()
