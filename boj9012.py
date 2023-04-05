n = int(input())

result = [0]*n

for i in range(n):

    s = input()

    li = [0]*len(s)

    for j in range(len(s)):
        li[i] = s[i]

    while len(li)>0:
        if len(li) == 0:
            result[i] = 'YES'
            break

        elif 0 in li:
            li.remove(0)

        else:
            result[i] = 'NO'
            break

        for k in range(len(li)-1):
            if li[k] == '(' and li[k+1] == ')':
                li[k] = 0
                li[k+1] = 0
                
    if len(li) == 0:
        result[i] = 'YES'
        

for i in range(n):
    print(result[i])
