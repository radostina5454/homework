#!/bin/python3

if __name__ == '__main__':
	z = eval(input('Enter a number:'))
	a = [1, 4, 6, 10, 11, 15, 23, 34, 52, 63, 71]
	b = 0
	c = 0
	l = len(a)
	d = 0
	while b in range(len(a)):
		print(f'{a[b]}, {a[c]}') 
		if a[b] + a[c] == z:
			print(f'The numbers are {a[b]} and {a[c]}')
			quit()		
		elif a[b] + a[c] > z and a[b] == a[c] or c == l-1:
			print("Such combination doesn't exist in the given list of numbers")
			quit()
		elif a[b] + a[c] > z:
			l = d			
			b = c
			c += 1
		elif a[b] + a[c] < z and b == l-1:
			b = l-2
			c += 1
		b += 1
		d += 1
