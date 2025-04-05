# Problem Statement:
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

def main():
    
    # Prompt the user to enter the first number.
    num1 = input("Enter first number: ")
    
    # Read the input and convert it to an integer.
    num1 = int(num1)
    
    # Prompt the user to enter the second number.
    num2 = input("Enter second number: ")
    
    # Read the input and convert it to an integer.
    num2 = int(num2)
    
    # Calculate the sum of the two numbers.
    total_sum = num1 + num2
    
    # Print the total sum with an appropriate message.
    print("The sum of the two numbers is: ", total_sum)
    
main()