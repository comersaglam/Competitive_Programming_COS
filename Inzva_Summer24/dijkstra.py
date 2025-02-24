 #!
import heapq
n = int(input())
edges =[[]]
succprob = []
start_node, end_node = map(int,input().split())


graph = [[] for _ in range()]
for i in range(len(edges)):
    u,v,w = edges[i][0], edges[i][1], succprob[i]
    graph[u].append((v,w))
    graph[v].append((u,w))

queue = [[0,start_node]]
visited = [False for _ in range(n)]
dist = [float('inf') for _ in range(n)]
dist[start_node] = 0

while queue:
    weight, node = heapq.heappop(queue)
    visited[node] = True
    for next_node, next_weight in graph[node]:
        if not visited[next_node]:
            heapq.heappush([weight+next_weight, next_node])
            dist[next_node] = min(dist[next_node], weight+next_weight)

print(dist[end_node])
