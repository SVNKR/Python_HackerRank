#!/bin/python3

N = int(input())

if N % 2:
    print("Weird")
else:
    if 2 <= N <= 5:
        print("Not Weird")
    elif 6 <= N <= 20:
        print("Weird")
    else:
        print("Not Weird")



