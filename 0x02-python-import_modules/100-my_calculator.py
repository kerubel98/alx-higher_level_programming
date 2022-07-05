#!/usr/bin/python3
from sys import argv
from calculator_1.py import sub, mul, add, div 
if __name__ == "__maine__":
    a = int(argv[0])
    b = int(argv[2])
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[1] == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif arg[1] == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif arg[1] == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif arg[1] == '/':
        print('{} - {} = {}'.format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
