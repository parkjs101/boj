N = int(input())
shorcut = []
li = []
for i in range(N):
    w = list(input().split())
    flag = False
    for j in range(len(w)):
        if w[j][0].upper() not in shorcut:
            shorcut.append(w[j][0].upper())
            w[j] = '['+w[j][0]+']'+w[j][1:]
            li.append(' '.join( _ for _ in w))
            flag = True
            break
        else:
            pass
    if flag == True:
        continue
           
    for j in range(len(w)):
        for k in range(len(w[j])):
            if w[j][k].upper() not in shorcut:
                shorcut.append(w[j][k].upper())
                w[j] = w[j][:k]+'['+w[j][k]+']'+w[j][k+1:]
                li.append(' '.join( _ for _ in w))
                flag = True
                break
        if flag == True:
            break
    if flag == False:
        li.append(' '.join( _ for _ in w))

for i in range(len(li)):
    print(li[i])