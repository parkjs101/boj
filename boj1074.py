k, n, m = map(int, input().split())

def func1(k, n, m):
    if k == 0:
        return 0
    else:
        h = 2**(k-1)
        if n >= h and m >= h:
            return h*h*3 + func1(k-1, n-h, m-h)
        elif n >= h and m < h:
            return h*h*2 + func1(k-1, n-h, m)
        elif n < h and m >= h:
            return h*h + func1(k-1, n, m-h)
        elif n < h and m < h:
            return func1(k-1, n, m)

print(func1(k, n, m))