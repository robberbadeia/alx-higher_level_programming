#!/usr/bin/python3
def divisible_by_2(my_list=[]):    
    if my_list:
        numbers = []
        for i in my_list:
            if i % 2 is 0:
                numbers.append(True)
            else:
                numbers.append(False)
        return numbers
