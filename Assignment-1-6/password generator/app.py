import random
import string

def generate_password(length):
    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one of each type for strong password
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest with random choices
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle and join to make final password
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            user_length = int(input("Enter desired password length (between 8 and 12): "))
            if 8 <= user_length <= 12:
                password = generate_password(user_length)
                print("Generated password:", password)
                break
            else:
                print("Please enter a number between 8 and 12.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()
