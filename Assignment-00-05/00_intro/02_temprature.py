# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def temprature():
    # prompt user for temprature in fahrenheit
    degrees_fahrenheit = float(input("Enter temprature in fahrenheit: "))
    
    # convert to celsius using this formula:
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    
    # output
    print(f"Temprature: {degrees_fahrenheit}F = {degrees_celsius}C")

temprature()