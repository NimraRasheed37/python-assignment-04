# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# The phonebook is a dictionary where the keys are names and the values are phone numbers.
phonebook ={
    "Nimra": "92-334-2478912",
    "Sara": "92-323-12092828",
    "Ahmed": "92-315-28387202",
}

# The program allows the user to add, remove, or look up phone numbers by name.

def main():
    # displaying menu
    print("welcome to the phonebook")
    print("1. Add a new contact")
    print("2. Remove a contact")
    print("3. Find a number")
    print("4. Exit")
    
    # Loop untill the user chooses to exit
    while True:
        # Prompt the user for an option
        choice = int(input("Enter your choice (1-4): "))
        
        # Perform the corresponding action based on the user's choice
        if choice == 1:
            name = input("Enter the name of the contact: ")
            number = input("Enter the phone number: ")
            phonebook[name] = number
            print(f"Contact {name} added with number {number}.")
        elif choice == 2:
            name = input("Enter the name of the contact to remove: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} removed.")
            else:
                print(f"Contact {name} not found.")
        elif choice == 3:
            name = input("Enter the name to find the number: ")
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}.")
            else:
                print(f"Contact {name} not found.")
        elif choice == 4:
            print("Exiting phonebook.")
            break
        else:
            print("Invalid choice. Please try again.")
        
main()
