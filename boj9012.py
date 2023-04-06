n = int(input())
result = []


for i in range(n):
    s = input()
    li = []
    for j in range(len(s)):
        li.append(s[j])
        if len(li)>1:
            if li[-2] == '(' and li[-1] ==')':
                li.pop()
                li.pop()
            else: 
                pass

    if len(li) == 0:
        result.append('YES')
    else:
        result.append('NO')

for i in range(n):
    print(result[i])
