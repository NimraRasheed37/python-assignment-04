# Problem Statement:
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def main():

    # What's your favorite animal? cow
    animal = input("What's your favorite animal? ")
    
    # My favorite animal is also cow!
    print(f"My favorite animal is also {animal}!")

main()