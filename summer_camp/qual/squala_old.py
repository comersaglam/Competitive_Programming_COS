n, m, c = map(int, input().split())
values = list(map(int, input().split()))
constraints = [tuple(map(int, input().split())) for _ in range(c)]

c0dict = {}
c1dict = {}
for c0,c1 in constraints:
    c0dict[c0] = c1
    c1dict[c1] = c0

dp = [[[0] * 2 for _ in range(m+1)] for _ in range(n+1)]

val_ordered = []
for i in range(n):
    if i in c0dict:
        val_ordered.append(values[i])
        val_ordered.append(values[c0dict[i]])
    elif i in c1dict:
        pass
    else:
        val_ordered.append(values[i])


# 1 is used, 0 is unused

for i in range(1,2*c+1):
    if i % 2 == 1: #c0
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1])
        for j in range(2,m+1):
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])
            dp[i][j][1] = max(dp[i-1][j-2][0] + val_ordered[i-1] + val_ordered[i], dp[i-1][j-2][1] + val_ordered[i-1] + val_ordered[i])
    else: #c1
        for j in range(1,m+1):
            dp[i][j][0] = dp[i-1][j][0]
            dp[i][j][1] = max(dp[i-1][j-1][0] +val_ordered[i-1], dp[i-1][j][1])

for j in range(1, m+1):
    i = 2*c + 1
    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] , dp[i-1][j-1][1] + val_ordered[i-1], dp[i-1][j-1][0] + val_ordered[i-1])

for i in range(2*c + 2, n+1):
    for j in range(1,m+1):
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][0] + val_ordered[i-1])

print(dp[n][m][0])