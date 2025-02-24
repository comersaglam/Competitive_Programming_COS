import heapq

def dijkstra(start, graph, n, is_omega, len_omega):
    distances = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    distances[start] = 0
    seen_omega = 0
    max_distance = -1
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        if visited[curr_node]:
            continue
        visited[curr_node] = True
        if is_omega[curr_node]:
            seen_omega += 1
            max_distance = max(max_distance, distances[curr_node])
            if seen_omega == len_omega:
                return max_distance
        for neighbor, weight in graph[curr_node]:
            if distances[curr_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[curr_node] + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))
    return max_distance
    

N, E = list(map(int, input().split()))  # N = number of nodes, E = number of edges
graph_total = [[] for _ in range(N + 1)]
for i in range(E):
    u, v, w = list(map(int, input().split()))
    graph_total[u].append((v, w))
    graph_total[v].append((u, w))

t = int(input())
theta = list(map(int, input().split()))
o = int(input())
omega = list(map(int, input().split()))
len_omega = len(omega)

is_theta = [False] * (N + 1)
is_omega = [False] * (N + 1)
for node in theta:
    is_theta[node] = True
for node in omega:
    is_omega[node] = True

graph = [[] for _ in range(N + 1)]
for u in range(1, N + 1):
    for v, w in graph_total[u]:
        if is_theta[u] and is_theta[v]:
            continue
        if is_omega[u] and is_omega[v]:
            continue
        graph[u].append((v, w))
for node in theta:
    graph[0].append((node, 0)) # add a virtual vertex 0 to all theta nodes with weight 0

distance = dijkstra(0, graph, N, is_omega, len_omega)
# we will go from theta to omega, because we want max of shortest path. 
# And because we can't use intramolecular edges, last edge seen from theta to omega will be max shortest path.
print(distance)