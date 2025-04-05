# Problem Statement
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.


def tall_enough():
    height = int(input("How tall are you? "))
    if height >= 50:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
    

tall_enough()

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)

def tall_enough_extension():
    while True:
        height = input("How tall are you? ")
        if height == "":
            break
        height = int(height)
        if height >= 50:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")
            
tall_enough_extension()