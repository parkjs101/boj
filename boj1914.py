n = int(input())

def func1(n, s, e):
    if n == 1:
        print(s, end=' ')
        print(e)
        return 1
    else:
        return func1(n-1, s, 6-s-e) + func1(1, s, e) + func1(n-1, 6-s-e, e)

print(2**n-1)
if n <= 20:
    func1(n, 1, 3)