#!/usr/bin/python3
def common_elements(set_1, set_2):
    return list(map(lambda x, y: x == y, (set_1, set_2)))
