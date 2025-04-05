# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    # get input from user
    curr_value = input("Enter a number: ")
    curr_value = int(curr_value)  # convert input to integer
    
    # loop untill curr_value is less than 100        
    while curr_value < 100:
        curr_value = curr_value * 2    # this formula will double the value
        print(curr_value)
    
main()