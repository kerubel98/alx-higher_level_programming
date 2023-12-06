#!/usr/bin/python3
def uniq_add(my_list=[]):
    mylist = []
    sum = 0
    for x in my_list:
        if x not in mylist:
            sum += x
        mylist.append(x)
    return sum
