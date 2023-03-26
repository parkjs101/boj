n = int(input())
cnt = 0
for i in range(n):
    w = input()
    wc = 0

    for j in range(len(w)):
        if j == 0:
            pass
        else:
            if w[j] != w[j-1]:
                wc += 1
            else:
                pass
    if wc+1 == len(set(w)):
        cnt += 1

print(cnt)

"""
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)

"""
