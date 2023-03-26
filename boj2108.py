import sys
from collections import Counter

N = int(sys.stdin.readline())

sum = 0
median = 0
scope = 0

list = []
n = []
mode_list = []

for i in range(N):
    list.append(int(sys.stdin.readline()))
    sum += list[i]
    n.append(list[i])

mean = sum/N
if mean < 0 and -1 < mean:
    print(0)
else:
    print("%.0f"%mean)

list.sort()
median = list[int(N/2)]
print(median)

counter = Counter(n).most_common()

for i in range(len(counter)):
    if i == 0:
        mode_list.append(counter[i][0])
    else:
        if counter[i-1][1] < counter[i][1]:
            mode_list.append(counter[i][0])
            break
        elif counter[i-1][1] == counter[i][1]:
            mode_list.append(counter[i][0])
        else:
            break

mode_list.sort(reverse=True)

if len(mode_list) > 1:
    print(mode_list[-2])
else:
    print(mode_list[0])

scope = list[-1]-list[0]
print(scope)


# Counter 클래스 사용법
# most_common() 함수
#  sort(reverse=True) 
# list 안에 tuple [(a,b),(c,d)] 접근
# // 연산자 = 몫
