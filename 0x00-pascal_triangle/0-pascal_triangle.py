#!/usr/bin/python3

def pascal_triangle(n):
    x = []
    if n<=0:
        print(x)
    else:
        for i in range(n-1,0,-1):
            for j in range(i+1):
                print('*',end='')
        print()


