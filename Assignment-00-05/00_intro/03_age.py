# Problem Statement
# Write a program to solve this age-related riddle!

def age():
    
    # Anton is 21 years old.
    anton_age = 21
    # Beth is 6 years older than Anton.
    beth_age = anton_age + 6
    # Chen is 20 years older than Beth.
    chen_age = beth_age + 20
    # Drew is as old as Chen's age plus Anton's age.
    drew_age = chen_age + anton_age
    # Ethan is the same age as Chen.
    ethan_age = chen_age
    
    # Anton is 3
    print("Anton is", anton_age)
    
    # Beth is 4
    print("Beth is", beth_age)

    # Chen is 5
    print("Chen is", chen_age)
    
    # Drew is 6
    print("Drew is", drew_age)

    # Ethan is 7
    print("Ethan is", ethan_age)

age()