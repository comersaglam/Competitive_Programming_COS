import sys
sys.setrecursionlimit(3000000)
import math
input = sys.stdin.readline

n, b = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v, l = map(int, input().split())
    adj[u].append((v, l))
    adj[v].append((u, l))

# Precompute arrays: parent, depth, dist (distance from root), sz (subtree sizes) and dp (sum of distances in subtree)
parent = [0]*(n+1)
depth = [0]*(n+1)
dist = [0]*(n+1)
sz = [0]*(n+1)
dp = [0]*(n+1)

def dfs(u, p):
    parent[u] = p
    sz[u] = 1
    for v, w in adj[u]:
        if v == p:
            continue
        depth[v] = depth[u] + 1
        dist[v] = dist[u] + w
        dfs(v, u)
        sz[u] += sz[v]
        dp[u] += dp[v] + sz[v] * w

dfs(1, 0)
# f[u] will be the sum of distances from u to all other nodes.
f = [0]*(n+1)
f[1] = dp[1]

def dfs2(u, p):
    for v, w in adj[u]:
        if v == p:
            continue
        # Re-rooting formula: when moving from u to v, the distances change by:
        # f[v] = f[u] + (n - 2*sz[v])*w
        f[v] = f[u] + (n - 2*sz[v]) * w
        dfs2(v, u)

dfs2(1, 0)

# Preprocess LCA using binary lifting.
LOG = math.ceil(math.log2(n)) + 1
up = [[0]*(n+1) for _ in range(LOG)]
# up[0][u] is the immediate parent of u.
for u in range(1, n+1):
    up[0][u] = parent[u]

for i in range(1, LOG):
    for u in range(1, n+1):
        up[i][u] = up[i-1][up[i-1][u]]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    # Lift u up so that depth[u] == depth[v]
    diff = depth[u] - depth[v]
    i = 0
    while diff:
        if diff & 1:
            u = up[i][u]
        diff //= 2
        i += 1
    if u == v:
        return u
    for i in range(LOG-1, -1, -1):
        if up[i][u] != up[i][v]:
            u = up[i][u]
            v = up[i][v]
    return parent[u]

def distance(u, v):
    w = lca(u, v)
    return dist[u] + dist[v] - 2*dist[w]

# Now answer each query.
# For each baying, we are given two orchards u and v;
# the baying path is the unique path between u and v.
# Then the answer is S(P) = (f(u) + f(v) - n*d(u,v)) // 2.
for _ in range(b):
    u, v = map(int, input().split())
    d_uv = distance(u, v)
    ans = (f[u] + f[v] - n * d_uv) // 2
    sys.stdout.write(str(ans) + "\n")


#* https://chatgpt.com/c/679df802-1920-8003-be05-769403b7a0c0?model=o3-mini-high