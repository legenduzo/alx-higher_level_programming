#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i and i != 8:
            print(f"{i}{j}", end=", ")
        elif i == 8 and j == 9:
            print(f"{i}{j}")
