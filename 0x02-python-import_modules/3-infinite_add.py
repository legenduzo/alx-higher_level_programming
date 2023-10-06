#!/usr/bin/python3
from sys import argv


def main():
    n = len(argv)
    if n == 1:
        print(0)
    elif n == 2:
        print(int(argv[1]))
    elif n > 2:
        sum = 0
        for i in range(1, n):
            sum += int(argv[i])
        print(sum)


if __name__ == "__main__":
    main()
