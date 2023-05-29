s = str(input())+' '
li = []
count = 0
stick = 0
laser = 0
li.append(s[0])
for i in range(1, len(s)):
    li.append(s[i])
    if li[-1] == ')' and s[i-1] =='(':
        li.pop()
        li.pop()
        count += len(li)
    elif li[-1] == ')' and s[i-1] != '(':
        li.pop()
        li.pop()
        stick += 1

print(count+stick)