n, l = map(int, input().split())
arr = []

while l<101 and l<=n+1:
    if n%l == 0 and l%2 != 0:
        for i in range(l):
            if n//l-int(l//2)+i < 0:
                break
            else:
                arr.append(str(n//l-int(l//2)+i))
        break

    elif n%l == int(l*0.5) and l%2 == 0:
        for i in range(l):
            if n//l-int(l//2)+i+1 < -1:
                break
            elif n//l-int(l//2)+i+1 < 0:
                arr.append('0')
            else:
                arr.append(str(n//l-int(l//2)+i+1))
        break
    else:
        l += 1

if len(arr) == 0:
    print(-1)
else:
    print(' '.join(arr))

#반례 n = 1 l = 2, n = 3 l = 3 
    


