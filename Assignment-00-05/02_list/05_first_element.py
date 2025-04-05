# Problem Statement
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty.

def get_first_element(lst):
    print("The first element is:", lst[0])

# Prompt the user to input the list elements
n = int(input("Enter the number of elements in the list: "))
user_list = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Call the function with the user-provided list
get_first_element(user_list)