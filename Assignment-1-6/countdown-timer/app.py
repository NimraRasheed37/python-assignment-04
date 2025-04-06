import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!            ")

# Ask user for input and handle errors
try:
    user_input = int(input("Enter the time in seconds: "))
    if user_input > 0:
        countdown_timer(user_input)
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Invalid input. Please enter a number.")
