#!/bin/python3

def cmap(func):
    def wrapper(*args):
        c= func(*args)
        return c       
    return wrapper

@cmap
def sum_two_numbers(a, b): 
    return a + b 
  
a, b = 1, 2
  

print("Sum =", sum_two_numbers(a, b)) 
