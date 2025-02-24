def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(n, edges):
    parent = [i for i in range(n)]
    rank = [0] * n
    mst_weight = 0
    ct_t_connections = 0
    edge_count = 0

    for edge in edges:
        u, v, weight, is_ct_t = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += weight
            edge_count += 1
            if is_ct_t:
                ct_t_connections += 1
            if edge_count == n - 1:
                break

    if edge_count != n - 1:
        return -1

    return ct_t_connections

n, m = map(int, input().split())
area_types = input().split()
edges = []

for _ in range(m):
    s, d, x = map(int, input().split())
    is_ct_t = 1 if (area_types[s-1] == 'CT' and area_types[d-1] == 'T') or (area_types[s-1] == 'T' and area_types[d-1] == 'CT') else 0
    edges.append((s-1, d-1, x, is_ct_t))

edges.sort(key=lambda edge: (edge[2], edge[3]))

result = kruskal(n, edges)
print(result)
