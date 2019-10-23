#!/bin/python3



def check(my_string): 
    brackets = ['()', '{}', '[]'] 
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string 
   





if __name__ == '__main__':


    string = input('Please enter brackets:')
    print(string, "-", "Correct" if check(string) else "Incorect")
