n = int(input())
count = 0
list = [[0]*100 for _ in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            if list[x+j][y+k] == 1:
                pass
            else:
                list[x+j][y+k] = 1
                count += 1

print(count)