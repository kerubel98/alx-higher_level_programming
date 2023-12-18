#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resualt = a/b
    except ZeroDivisionError:
        resualt = None
    finally:
        print('Inside result: {}'.format(resualt))
    return resualt
