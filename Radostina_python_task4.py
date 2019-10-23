#!/bin/python

def recur_factorial(n):

   if n == 1:
       return n
   else:
       return n * recur_factorial(n-1)


if __name__ == '__main__':
	num = int(input("Enter a number: "))
	if num < 0:
		print("Factorial does not exist for negative numbers")
	else:
		print("Factorial of",num,"is",recur_factorial(num))
