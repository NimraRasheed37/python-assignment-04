# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

def main():
    # Initialize an empty dictionary to store the counts
    counts = {}

    # Loop to get user input
    while True:
        try:
            # Prompt the user for a number
            num = int(input("Enter a number (or -1 to stop): "))
            if num == -1:
                break  # Exit the loop if the user enters -1

            # Update the count for the number in the dictionary
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        except ValueError:
            print("Please enter a valid integer.")

    # Print the counts of each number
    for num, count in counts.items():
        print(f"{num} appears {count} times.")

main()