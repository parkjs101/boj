N = int(input())

time = [[0]*2 for _ in range(N)]

for i in range(N):
	start, end = map(int, input().split())
	time[i][0] = start
	time[i][1] = end

def schedule(N, time):
	time.sort()
	nt = [time[0]]

	for i in range(1, N):
		if time[i][0] == time[i-1][0]:
			if time[i][0] == time[i-1][1]:
				nt.append(time[i])
			else:
				continue
		else:
			if time[i][0] >= nt[-1][1]:
				nt.append(time[i])
			else:
				if time[i][1] <= nt[-1][1]:
					nt.pop()
					nt.append(time[i])
				else:
					continue
	return len(nt)

result = schedule(N, time)
print(result)
