# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

fruits = {
    "apple": 40,
    "banana": 30,
    "kiwi": 50,
    "mango": 50,
    "Melon": 100,
    "Grapes": 60,
    "Strawberry": 80,
}

def total_cost(fruits):
    total = 0
    for fruits, price in fruits.items():
        quantity = int(input(f"How many ({fruits}) do you want?: "))
        total += price * quantity
        print(f"{quantity} {fruits} cost: {price * quantity} pkr")
    # Print the total cost
    print(f"Your total is {total} pkr")
    
total_cost(fruits)

