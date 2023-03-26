def func2(l, n):
    count = 0
    L = [0]*100
    for i in range(n):
        L[l[i]] = l[i]
        if L[100-l[i]] != 0:
            count += 1
    return print(count)

func2([1,23,53,77,90], 5)

