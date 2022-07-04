#!/usr/bin/python3
from sys import argv
import calculator_1.py 
if __name__ == "__maine__":
    a = int(argv[1])
    b = int(argv[3])
    if len(argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif argv[2] == "+":
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif arg[2] == "-":
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif arg[2] == "*":
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif arg[2] == "/":
        print('{} - {} = {}'.format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
