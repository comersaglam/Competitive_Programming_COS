from collections import deque
import heapq

N, S1, S2, H, T, C = list(map(int, input().split()))
matrix = [[] for _ in range(2*N+1)]
for i in range(S1):
    u,v,w = map(int, input().split())
    matrix[u].append((v, w))
    matrix[v].append((u, w))

def bfs(start, graph):
    distances = {}
    queue = deque([start])
    distances[start] = 0
    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        for neighbor, _ in graph[node]:
            if neighbor not in distances:
                distance = current_distance + 1
                distances[neighbor] = distance
                queue.append(neighbor)
                graph[neighbor].append((neighbor+N, distance*C))
                graph[neighbor+N].append((neighbor, distance*C))
    graph[start].append((start+N, 0))
    graph[start+N].append((start, 0))
bfs(H, matrix)

for i in range(S2):
    u,v,w = map(int, input().split())
    matrix[u].append((v+N, w+N))
    matrix[v].append((u+N, w+N))


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

distances = dijkstra(H, matrix, 2*N)
print(min(distances[T], distances[T+N]))

