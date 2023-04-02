N = int(input())

li = []
for i in range(N):
    li.append(list(map(int,input().split())))

li.sort(key=lambda x:(x[0], x[1]))

for i in li:
    print(li[0], li[1])
    

