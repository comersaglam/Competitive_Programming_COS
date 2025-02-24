n, m = map(int, input().split()) 
dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)] 

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    dist[u][v] = w

res = 0
for k in range(1, n+1):  # Intermediate nodes
    for i in range(1, n+1):  # Starting node
        for j in range(1, n+1):  # Ending node
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            if dist[i][j] != float('inf'):
                res += dist[i][j]

print(res)