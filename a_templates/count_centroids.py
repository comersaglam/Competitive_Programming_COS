n = int(input())
graph = {i: [] for i in range(1, n + 1)}
children_count = {i: 1 for i in range(1, n + 1)}

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs_size(node, parent):
    for child in graph[node]:
        if child != parent:
            children_count[node] += dfs_size(child, node)
    return children_count[node]

def find_centroids(node, parent, n):
    is_centroid = True
    max_subtree_size = 0

    for child in graph[node]:
        if child != parent:
            if children_count[child] > n // 2:
                is_centroid = False
            max_subtree_size = max(max_subtree_size, children_count[child])

    if n - children_count[node] > n // 2:
        is_centroid = False
    else:
        max_subtree_size = max(max_subtree_size, n - children_count[node])

    if is_centroid:
        centroids.append(node)
    
    for child in graph[node]:
        if child != parent:
            find_centroids(child, node, n)

centroids = []
dfs_size(1, -1)
find_centroids(1, -1, n)

print(len(centroids))