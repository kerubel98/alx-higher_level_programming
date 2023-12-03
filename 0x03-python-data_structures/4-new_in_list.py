#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_ = my_list.copy()
    if idx > len(my_list) or idx < 0:
        return list_
    else:
        my_list[idx] = element
        return my_list
