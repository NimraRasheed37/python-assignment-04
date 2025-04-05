# Problem Statement
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def main():
    
    # initialize an empty list
    user_list = []
    
    # while loop to ask user for input until they press enter without typing anything.
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)
    print("Here's the list:", user_list)
    
main()
