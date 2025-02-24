import heapq
n,m,k = map(int, input().split())
start, end = map(int, input().split())
intermediates = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start, graph, n):
    distances = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    distances[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        if visited[curr_node]:
            continue
        visited[curr_node] = True
        for neighbor, weight in graph[curr_node]:
            if distances[curr_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[curr_node] + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))
    return distances

from_start = dijkstra(start, graph, n)
from_end = dijkstra(end, graph, n)

sp = float('inf')
for inter in intermediates:
    if from_start[inter] != float('inf') and from_end[inter] != float('inf'):
        path = from_start[inter] + from_end[inter]
        sp = min(sp, path)

if sp == float('inf'):
    print(-1)
else:
    print(sp)