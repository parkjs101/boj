s = input()
total = 0
li = []
li.append(s[0])
stack = []
floor = []

for i in range(1, len(s)):
    li.append(s[i])

    if li[-1] == ')' and s[i-1] == '(':
        if len(stack) == 0 or (len(li)-2 not in floor):
            stack.append(2)
            floor.append(len(li)-2)
        else:
            stack[-1] += 2
        li.pop()
        li.pop()

    elif li[-1] == ')' and (s[i-1] == ']' or s[i-1] == ')'):
        stack[-1] = stack[-1]*2
        if len(stack) > 1:
            stack[-2] += stack[-1]
            stack.pop()
        li.pop()
        li.pop()
        if len(floor) > 0:
            floor.pop()
    
    elif li[-1] == ']' and s[i-1] == '[':
        if len(stack) == 0 or (len(li)-2 not in floor):
            stack.append(3)
            floor.append(len(li)-2)
        else:
            stack[-1] += 3
        li.pop()
        li.pop()

    elif li[-1] == ']' and (s[i-1] == ']' or s[i-1] == ')'):
        stack[-1] = stack[-1]*3
        if len(stack) > 1:
            stack[-2] += stack[-1]
            stack.pop()
        li.pop()
        li.pop()
        if len(floor) > 0:
            floor.pop()
    
    elif (li[-1] == ']' and s[i-1] == '(')or (li[-1] == ')' and s[i-1] == '['):
        total = 0
        break

    else:
        pass

    if len(li) == 0:
        total += sum(stack)
        stack = []
        floor = []
    
print(total)
