arr = [0]*10001
arr[0] = 1

for i in range(1, 10001):
    idx = i
    while idx <= 10000:
        if idx >= 1000:
            idx += idx%10 +(idx%100)//10 + (idx%1000)//100 + idx//1000
        elif idx >= 100:
            idx += idx%10 + (idx%100)//10 + idx//100
        elif idx >= 10:
            idx += idx%10 + idx//10
        else:
            idx += idx

        if idx <= 10000:
            arr[idx] = 1

for i in range(len(arr)):
    if arr[i] == 0:
        print(i)