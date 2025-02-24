import heapq

# Input handling
n, m = map(int, input().split())  # n = number of vertices, m = number of edges
graph = [[] for _ in range(n+1)]  # Graph represented as an adjacency list

for _ in range(m):
    u, v, w = map(int, input().split())  # Read each edge and its weight
    graph[u].append((w, v))  # Add edge to the graph
    graph[v].append((w, u))  # Since the graph is undirected

# Prim's algorithm
def prims(start=1):
    visited = [False] * (n+1)  # Track visited vertices
    min_heap = [(0, start)]  # Min heap initialized with an arbitrary starting vertex
    total_weight = 0  # Total weight of the MST
    mst_edges = []  # Edges in the MST

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        if u != start:  # Avoid adding the initial 0-weight edge
            mst_edges.append((u, weight))
        for edge_weight, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_weight, v))

    return total_weight, mst_edges

total_weight, mst_edges = prims()
print("Total weight of MST:", total_weight)
for vertex, weight in mst_edges:
    print(f"Edge to {vertex} with weight {weight}")