#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    sort = sorted(name for name in names if not name.startswith("__"))
    for name in sort:
        print(name)


if __name__ == "__main__":
    main()
