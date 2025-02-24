import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v, w, f = map(int, input().split())
    graph[u].append((v, w, f))
    graph[v].append((u, w, f))
# u,v,w,f = node1, node2, weight, frequency

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
        for neighbor, weight, freq in graph[curr_node]:
            if distances[curr_node] % freq != 0:
                weight += freq - distances[curr_node] % freq
                if distances[curr_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[curr_node] + weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))

            if distances[curr_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[curr_node] + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))

    if distances[n] == float('inf'):
        print(-1)
    else:
        print(distances[n])

dijkstra(1, graph, n)