#!/bin/python3

def add():
	print(x+y)

def sub():
	print(x-y)

def mult():
	print(x*y)

def div():
	print(x/y)

def wholediv():
	print(x//y)

def quitApp():
	print('Quit app')
	quit()

if __name__ == '__main__':

	while True:
		
		print("Enter two number and an operation. ")
		x = input("First number: ")
	
		if x.isdigit():
			x = int(x)
		else:
			print('Wrong input! Please enter the  number again')
			continue
		y = input('Second number: ')

		if y.isdigit():
			y = int(y)
		else:
			print('Wrong input! Please enter the  number again')
			continue
		z = input('Enter operation +, -, *, /, //, or q-quit: ')
	
		operation = {	'+':add, 
						'-':sub, 
						'*':mult, 
						'/':div, 
						'//':wholediv, 
						'q':quitApp}
		
		if z in operation:	
			print ('The result is: ')
			operation[z]()
		else:
			print('Invalid operation')
