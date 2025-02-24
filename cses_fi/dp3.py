import sys
n, x = list(map(int, sys.stdin.readline().split()))
coins = list(map(int, sys.stdin.readline().split()))
dp = [0] * (x + 1)
dp[0] = 1
modulo = 10**9 + 7


for i in range(1, x + 1):
    for c in coins:
        if i >= c:
            dp[i] = dp[i] + dp[i-c] % modulo

print(dp[x] % modulo)