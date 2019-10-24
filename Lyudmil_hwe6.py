#!/bin/python3

def cmap(func, *args, **kwargs):
	return_value = []
	
	return_value.append(func(*args, **kwargs))
	
	print(f'{return_value}\n'+'-'*40)
	return return_value

#################Example######################

if __name__ == '__main__':
	a = ['a', 'c', 'b', 's', 'd', 'g']
	b = [1, 2, 5, 6, 8, 10, 16, 7, 8, 11]
	
	cmap(sorted, a)
	cmap(sorted, b)
	cmap(sum, b)
