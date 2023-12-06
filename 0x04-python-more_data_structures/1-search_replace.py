#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = my_list.copy()
    for i, x in enumerate(my_list):
        if x is search:
            mylist[i] = replace
    return mylist
