#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    leng = len(my_list)
    for i in range(leng, 0, -1):
        print('{}'.format(my_list[i - 1]))
