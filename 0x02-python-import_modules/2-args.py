#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    a = argc - 1
    str = 'argument' if a == 1 else 'arguments'
    pls = ':' if a != 0 else '.'
    str = str + pls
    print('{} {}'.format(a, str), end='\n')
    for i in range(1, argc):
        print('{}: {}'.format(i, sys.argv[i]), end='\n')
