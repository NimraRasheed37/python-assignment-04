# Problem Statement
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

def mass():
    
    # user input for mass (M
    mass = float(input("Enter kilos of mass: "))
    
    # speed of light in m/s
    speed_of_light = 299792458
    
    # E = m * c**2
    energy = mass * speed_of_light ** 2
    
    # output
    print(f"{energy} joules of energy!")

mass()
