#!/usr/bin/python3
def best_score(a_dictionary):
    grt = 0
    if a_dictionary is not None:
        for key in a_dictionary.keys():
            if a_dictionary[key] > grt:
                grt = a_dictionary[key]
        for val in a_dictionary.keys():
            if a_dictionary[val] == grt:
                return val
