n, m = list(map(int, input().split()))
edgecount = [0] * (n+1)
for _ in range(m):
    u, v = list(map(int, input().split()))
    edgecount[u] += 1
    edgecount[v] += 1

print(*edgecount[1:])