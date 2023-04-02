import sys
N = int(input())

li = list(map(int,sys.stdin.readline().split()))
s_li = sorted(list(set(li)))
print(s_li)
