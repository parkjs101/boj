x = int(input())


arr = [0]*(1000001)
arr[1] = 0

if x > 1:
    for i in range(2,x+1):
        cur = []
        if i%3 == 0:
            cur.append(arr[i//3]+1)
        if i%2 == 0:
            cur.append(arr[i//2]+1)
        cur.append(arr[i-1]+1)

        arr[i] = min(cur)

print(arr[x])