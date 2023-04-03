def func1(n):
    sum = 0
    a = int(n/3)
    b = int(n/5)
    c = int(n/15)

    for i in range(a+1):
        sum += i*3
    
    for i in range(b+1):
        sum += i*5

    for i in range(c+1):
        sum -= i*15
    
    return sum

print(func1(27639))

# n까지 3과5의 배수의 합 구하기