#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary.keys())
    for i in sorted_key:
        print('{}: {}'.format(i, a_dictionary.get(i)))
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
