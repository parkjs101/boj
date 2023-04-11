s = input()+' '
#ababc' '
#012345
li = []

for i in range(len(s)-1):
    for j in range(0, len(s)-1-i):
        li.append(s[j:j+i+1])

li = set(li)

print(len(li))
