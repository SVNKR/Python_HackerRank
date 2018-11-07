#!/bin/python3

year = int(input())
leap = False

if not year % 4:
        if not year % 100 and not year % 400:
            leap = True
        else:
            leap = True

print(leap)


def is_leap(year):
    leap = False

    # Write your logic here
    if not year % 4:
        if not year % 100:
            if not year % 400:
                leap = True
        else:
            leap = True
    return leap

