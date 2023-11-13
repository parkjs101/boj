V, E = map(int, input().split())
K = int(input())

INF = float('inf')
dp = [INF] * (V + 1)
visited = [False] * (V + 1)
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
		dp[start] = 0 

		def get_min_node():
				min_dis = float('inf')
				node = 0
				for i in range(1, V+1):
						if dp[i] <= min_dis and not visited[i]:
								min_dis = dp[i]
								node = i
				return node
		
		for _ in range(1, V+1):
				minnode = get_min_node()
				visited[minnode] = True
				for i in range(len(graph[minnode])):
						if graph[minnode][i][0] + dp[minnode] < dp[graph[minnode][i][1]] and visited[graph[minnode][i][1]] == False:
								dp[graph[minnode][i][1]] = graph[minnode][i][0] + dp[minnode]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
	
Dijkstra(K)

for i in range(1, V + 1):
    print("INF" if dp[i] == INF else dp[i])