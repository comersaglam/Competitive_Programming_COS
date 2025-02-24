n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Step 1: DFS to fill euler, first, and height
euler = []
first = [-1] * (n + 1)
height = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(node, h=0):
    visited[node] = True
    height[node] = h
    first[node] = len(euler)
    euler.append(node)
    for to in graph[node]:
        if not visited[to]:
            dfs(to, h + 1)
            euler.append(node)
dfs(1)

# Step 2: Build Segment Tree
m = 4 * len(euler)
segtree = [0] * m

def build(node, b, e):
    if b == e:
        segtree[node] = euler[b]
    else:
        mid = (b + e) // 2
        build(node * 2, b, mid)
        build(node * 2 + 1, mid + 1, e)
        l, r = segtree[node * 2], segtree[node * 2 + 1]
        segtree[node] = l if height[l] < height[r] else r

build(1, 0, len(euler) - 1)

# Step 3: Query Segment Tree
def query(node, b, e, L, R):
    if b > R or e < L:
        return -1
    if L <= b and e <= R:
        return segtree[node]
    mid = (b + e) // 2
    left = query(node * 2, b, mid, L, R)
    right = query(node * 2 + 1, mid + 1, e, L, R)
    if left == -1: return right
    if right == -1: return left
    return left if height[left] < height[right] else right

def lca(u, v):
    left, right = first[u], first[v]
    if left > right: left, right = right, left
    return query(1, 0, len(euler) - 1, left, right)

u, v = map(int, input().split())
ancestor = lca(u, v)
print(ancestor, height[u] + height[v] - 2 * height[ancestor])
