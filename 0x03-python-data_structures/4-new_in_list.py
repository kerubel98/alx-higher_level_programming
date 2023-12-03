#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_ = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        list_[idx] = element
        return list_
