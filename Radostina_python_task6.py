#!/bin/python3


def glavna(func,*args):
	c= func(*args)
	return c



s = glavna(sum, [6,3,2,5,4])
print(f'{s}')
