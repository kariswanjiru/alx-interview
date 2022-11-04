def pascal_triangle(n):
    x = []
    if n<=0:
        print(x)
    elif n==1:
        x += [1]
        print(x)
    else:
        x.append(n)
        print(x)
    

pascal_triangle(2)