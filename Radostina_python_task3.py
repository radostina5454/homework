#!/bin/python3

def sum1(lst):
    total = 0
    for element in lst:
        if type(element) is list:
            total = total + sum1(element)
        else:
            total = total + element
    return total


if __name__ == '__main__':

	t=[[1,2,10],4,3,5,[3,4]]
	result = sum1(t)

print(f'Sum of lists {t} is :{result}')
