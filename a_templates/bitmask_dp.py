import sys

MAX_INT = sys.maxsize
n=4

dp = [MAX_INT] * (1<<n)

dp[0] = 0
cost = [[0,3,2,2],[3,0,2,3],[2,2,0,1],[2,3,1,0]]

for mask in range(1<<n):
    x = bin(mask).count('1')

    for i in range(n):
        if mask & (1<<i) == 0:
            new_mask = mask | (1<<i)
            dp[new_mask] = min(dp[new_mask],dp[mask]+cost[x][i])

print(dp)






n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

dp = [[0]* (1<<n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for mask in range(1<<n):
            if mask.bit_count() != i: continue
            if (mask & (1<<j)): continue
            dp[i][mask | (1<<j)] = max(dp[i][mask | (1<<j)], dp[i-1][mask] + grid[i][j])
        
print(dp[-1][-1])
            