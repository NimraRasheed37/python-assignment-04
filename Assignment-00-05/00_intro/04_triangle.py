# Problem Statement
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

def triangle_perimeter():
    
    # What is the length of side 1? 3
    side1 = float(input(f"Enter the length of side 1 of traingle: "))
    # What is the length of side 2? 4
    side2 = float(input(f"Enter the length of side 2 of traingle: "))
    # What is the length of side 3? 5.5
    side3 = float(input(f"Enter the length of side 3 of traingle: "))
    
    # The perimeter of the triangle is 12.5
    perimeter = side1 + side2 + side3
    
    # output
    print(f"The perimeter of the tranlge is", perimeter)

triangle_perimeter()