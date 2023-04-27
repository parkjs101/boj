s = str(input())
li = []
result = []
for i in range(len(s)):
    if len(result) > i:
        continue

    if s[i] == '<':
        j = i
        while s[j] != '>':
            result.append(s[j])
            j += 1
        result.append(s[j])

    elif s[i] == ' ':
        result.append(s[i])

    else:
        j = i
        while s[j] != '<' and s[j] != ' ':
            li.append(s[j])
            if j < len(s)-1:
                j += 1
            else:
                break

        for i in range(len(li)):
            result.append(li.pop())

print(''.join(str(i) for i in result))

