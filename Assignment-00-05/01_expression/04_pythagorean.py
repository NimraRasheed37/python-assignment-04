# Problem Statement
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

def length_of_hypotenuse():
    
    # Enter the length of AB: 3
    len_ab = float(input("Enter teh length of AB: "))
    
    # Enter the length of AC: 4
    len_ac = float(input("Enter the length of AC: "))

    # BC ** 2 = AB ** 2 + AC ** 2
    len_bc = (len_ab ** 2 + len_ac ** 2) ** 0.5

    # output
    print(f"The length of BC (the hypotenuse) is: {len_bc}")

length_of_hypotenuse()