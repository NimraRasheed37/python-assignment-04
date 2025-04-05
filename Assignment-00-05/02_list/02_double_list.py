# Problem Statement
# Write a program that doubles each element in a list of numbers.


def double():
    
    numbers = [3, 4, 5, 6]
    
    for i in range(len(numbers)):
        
        numbers[i] = numbers[i] *2
        
        print(numbers[i])
double()