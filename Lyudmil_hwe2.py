#!/bin/python3

if __name__ == '__main__':
	z = eval(input())
	a = [1, 4, 6, 8, 11, 15, 23, 34, 52]
	b = 0
	c = 0
	while b in range(len(a)):
		for c in range(len(a)):
			print(f'{a[b]},{a[c]}')
			if a[b] + a[c] == z:
				print(f'The numbers are {a[c]} and {a[b]}') 
				quit()
			c += 1
		b += 1
	print("Such combination doesn't exist")
