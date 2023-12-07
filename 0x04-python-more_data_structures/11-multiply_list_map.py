#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mylist = my_list.copy()
    mylist = list(map(lambda x: x *2, mylist))
    return mylist
