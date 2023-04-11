import sys
N = int(input())
people = {}
for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    if b[0] == 'e':
        people[a] = 'e'
    else:
        del people[a]

people = list(people.keys())              
people.sort(reverse=True)
for i in range(len(people)):
    print(people[i])