# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def inches():
    # user input
    feet = float(input("Enter the number of feet/foot: "))
    
    # formula to convert feet/foot to inches, 1 foot is equal to 12 inches
    feet_to_inches = feet * 12
    
    # check if input is singular or plural, feet or foot
    if feet == 1:
        print(f"{feet} foot is equal to {feet_to_inches}" + " inches.")
    else:
        print(f"{feet} feet is equal to {feet_to_inches}" + " inches")
    
inches()