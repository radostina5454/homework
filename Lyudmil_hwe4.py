#!/bin/python3

def factor(n):
	p = 1
	i = 1
	d = 0

	while (d < n):
		d += 1	
		i = d*p
		p = i
	
	return i

if __name__ == '__main__':
	n = eval(input("Input a needed factorial: "))
	f = factor(n)
	print(f'The value of the {n}! is: {f} ')
	
