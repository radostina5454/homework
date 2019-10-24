#!/bin/python3

def measure(func):
    def wrapper(*args):
        c= func(*args)
        return c       
    return wrapper

@measure
def sum_two_numbers(a, b): 
    return a + b 
  
a, b = 1, 2
  

print("Sum =", sum_two_numbers(a, b)) 
