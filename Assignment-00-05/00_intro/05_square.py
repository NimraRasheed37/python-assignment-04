# Problem Statement
# Ask the user for a number and print its square (the product of the number times itself).

def square():
    # user input
    num = float(input(f"Enter a number: "))
    
    # formula
    number_square = num * num
    
    # output
    print(f"Square of {num} is", number_square)

square()