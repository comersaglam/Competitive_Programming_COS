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
            