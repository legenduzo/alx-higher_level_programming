#!/usr/bin/python3
from sys import argv
from sys import exit
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    count = len(argv)
    operators = ('+', '-', '*', '/')
    if count < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, o, b = argv[1:]

    if o == '+':
        print(f"{a} {o} {b} = {add(int(a), int(b))}")
    elif o == '-':
        print(f"{a} {o} {b} = {sub(int(a), int(b))}")
    elif o == '*':
        print(f"{a} {o} {b} = {mul(int(a), int(b))}")
    elif o == '/':
        print(f"{a} {o} {b} = {div(int(a), int(b))}")
