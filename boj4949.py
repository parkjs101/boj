def balance():
    while True:
        s = input()
        li = []
        if s =='.':
            return 0
        else:
            for i in range(len(s)):
                li.append(s[i])
                if li[-1] == '.':
                    if '(' in li or ')'in li or '[' in li or ']' in li:
                        print('no')
                        break
                    else:
                        print('yes')
                        break

                elif li[-1] == ')':
                    if '(' in li:
                        p = -1
                        while li[p] != '(':
                            p -= 1
                        li.pop(p)
                        li.pop()

                elif li[-1] == ']':
                    if '[' in li:
                        p = -1
                        while li[p] != '[':
                            p -= 1
                        li.pop(p)
                        li.pop()
                else:
                    continue
        
balance()
        
        