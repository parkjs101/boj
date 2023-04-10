x = int(input())

n = 1
while x > sum(i for i in range(n+1)):
    n += 1

if n%2 == 0:
    print((x - sum(i for i in range(n))), end='')
    print('/',end='')
    print(n+1 - (x - sum(i for i in range(n))))

else:
    print(n+1 - (x - sum(i for i in range(n))), end='')
    print('/',end='')
    print(x - sum(i for i in range(n)))

