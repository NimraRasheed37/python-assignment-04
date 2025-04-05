# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long.
# If lst is already shorter than MAX_LENGTH you should leave it unchanged.

def shorten(lst):
    MAX_LENGTH = 3
    while len(lst) > MAX_LENGTH:
        print("Removing:", lst.pop())

def shorten():
    # Prompt the user to input the list elements
    n = int(input("Enter the number of elements in the list: "))
    user_list = []

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    print("Original list:", user_list)
    shorten(user_list)
    print("Shortened list:", user_list)

shorten()