# Problem Statement
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

def seconds_in_year():
    # Constants for the calculation
    days = 365
    hours = 24
    minutes = 60
    seconds = 60
    
    # calculating the result in seconds
    result = days * hours * minutes * seconds
    
    # output the result
    print(f"There are {result} seconds in a year!")

seconds_in_year()