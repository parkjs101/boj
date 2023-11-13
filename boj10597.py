s = str(input())

if len(s) < 10:
	N = len(s)
else:
	N = (len(s)-9)//2+9

is_used = [0]*(N+1)
arr = []

def func1(n, start):
	if n == N:
		for j in range(N):
			print(arr[j], end=' ')
		is_used[0] = 1
		return

	else:
		for i in range(2):
			if s[n] != 0 and is_used[0] == 0:
				v = int(s[start:start+i+1])
				if v <= N and is_used[v] == 0:
					is_used[v] = 1
					arr.append(v)
					func1(n+1, start+i+1)
					is_used[v] = 0
					arr.pop()

func1(0, 0)
