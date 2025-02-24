n = int(input())
modulo = 10**9 + 7
 
maze = []
 
for _ in range(n):
    maze.append(list(input()))
 
dp = [[0] * n for _ in range(n)]
 
for i in range(n):
    if maze[0][i] == '.':
        dp[0][i] = 1
    else: break
for i in range(n):
    if maze[i][0] == '.':
        dp[i][0] = 1
    else: break
 
for i in range(1, n):
    for j in range(1, n):
        if maze[i][j] == '.':
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % modulo
 
print(dp[n-1][n-1] % modulo)