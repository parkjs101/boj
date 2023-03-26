n = str(input())
n_list = []
for i in range(len(n)):
    n_list.append(n[i])
print(''.join(sorted(n_list, reverse=True)))

