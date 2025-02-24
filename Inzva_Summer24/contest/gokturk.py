import heapq

n, m, start, target = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(m):
    u,v,w = list(map(int,input().split()))
    graph[u].append((v,w))
    graph[v].append((u,w))


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
            x = max(distances[curr_node], weight)
            if  x < distances[neighbor]:
                distances[neighbor] = x
                heapq.heappush(pq, (distances[neighbor], neighbor))
    return distances

dist = dijkstra(start, graph, n)
print(dist[target])