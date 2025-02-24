n = int(input().strip())
arr = list(map(int, input().strip().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = arr[i]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = max(arr[i] - dp[i + 1][j], arr[j] - dp[i][j - 1])

print((sum(arr) + dp[0][n - 1]) // 2)