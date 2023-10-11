#!/usr/bin/python3
def uniq_add(my_list=[]):
    set1 = set(my_list)
    result = list(set1)
    sum = 0
    for i in result:
        sum += i
    return(sum)
# We Can find a uniq vales
# unique_values = list(reduce(lambda x, y: x + [y]
#                               if y not in x else x, lists, []))
