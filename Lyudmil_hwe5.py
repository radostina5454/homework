#!/bin/python3

if __name__ == '__main__':
	n = input()
	p = 0
	countercirc = 0
	countersq = 0
	countercur = 0

	for p in range(len(n)):
		if n[p] == '(':
			countercirc += 1
		elif n[p] == ')':
			countercirc -= 1
		elif n[p] == '[':
			countersq += 1
		elif n[p] == ']':
			countersq -= 1
		elif n[p] == '{':
			countercur += 1
		elif n[p] == '}':
			countercur -= 1
	
	if countercirc == 0 and countersq == 0 and countercur == 0:
		print("There are no missing brackets")
	else:
		if countercirc > 0:
			print(f"There is a missing number of missing '(' : {countercirc}")
		elif countercirc < 0:
			print(f"There is a missing number of missing ')' : {countercirc}")
		if countersq > 0:
			print(f"There is a missing number of missing '[' : {countersq}")
		elif countersq < 0:
			print(f"There is a missing number of missing ']' : {countersq}")
		if countercur > 0:
			print("There is a missing number of missing '{' : " f"{countercur}")
		elif countercur < 0:
			print("There is a missing number of missing '}' : " f"{countercur}")
