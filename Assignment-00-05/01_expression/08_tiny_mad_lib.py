# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def sentence():
    # prompt user for an adjective, noun and verb
    adjective = input("Please enter an adjective and press enter: ")
    noun = input("Please enter a noun and press enter: ")
    verb = input("Please enter a verb and press enter: ")
    
    # print the sentence
    print(f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!")

sentence()
