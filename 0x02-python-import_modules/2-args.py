#!/usr/bin/python3
from sys import argv


def main():
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    elif n > 2:
        print(f"{n - 1} arguments:")
        for i in range(1, n):
            print(f"{i}: {argv[i]}")


if __name__ == "__main__":
    main()
