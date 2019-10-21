#!/bin/python3

def sum(n):
	i = 0
	s = 0

	for i in range(len(n)):
		if str(type(n[i])) == "<class 'int'>":
			s += n[i]
		elif str(type(n[i])) == "<class 'list'>":
			x = sum(n[i])
			s += x
	return s


if __name__ == '__main__':
	n = eval(input('Enter a list:'))
	s = sum(n)
	
	print(f'The sum of all the numbers in the list is: {s}')

