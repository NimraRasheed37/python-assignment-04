# Problem Statement:
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def divide_remainder():
    # Please enter an integer to be divided: 5
    divided = int(input("Please enter an integer to be divided: "))
    
    # Please enter an integer to divide by: 3
    divisor = int(input("Please enter an integer to divide by: "))
    
    # storing result of division in a variable
    result = divided // divisor
    
    # storing remainder of division in a variable
    remainder = divided % divisor
    
    # output
    print(f"The result of this division is {result} with a remainder of {remainder}")
    
divide_remainder()