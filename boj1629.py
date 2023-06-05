a, b, c = map(int, input().split())
v = 1

def func1(n):
    if n == 1:
        v = a%c
        return v
    if n == 0:
        return 1
    if n%2 == 0:
        v = func1(n//2)
        return v*v%c
    elif n%2 == 1:
        v = func1(n//2)
        return v*v*a%c

print(func1(b))

