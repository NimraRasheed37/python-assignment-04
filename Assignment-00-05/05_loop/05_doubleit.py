# Problem Statement
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# For example if the user enters the number 2 you would then print:

# output:  4 8 16 32 64 128 / We stop at 128 because that value is greater than 100.

# Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. Recall that you can double the value of curr_value using a line like:

# curr_value = curr_value * 2

# This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

# while curr_value < 100:

def main():
    # get input from user
    curr_value = input("Enter a number: ")
    curr_value = int(curr_value)  # convert input to integer
    
    # loop untill curr_value is less than 100        
    while curr_value < 100:
        curr_value = curr_value * 2    # this formula will double the value
        print(curr_value)
    
main()

# -> note-to-self: the last nnumber shown in output is greater than 100, that's because the last number that was multipliable with 2 was less than 100, so it shows product of that number