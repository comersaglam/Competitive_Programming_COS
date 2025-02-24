MAX = 10**6 + 7
n, x = list(map(int, input().split()))
coins = list(map(int, input().split()))

dp = [MAX] * (x+1)
dp[0] = 0
for c in coins:
    for i in range(c, x+1):
        dp[i] = min(dp[i], dp[i-c] + 1)
print(dp[x] if dp[x] != MAX else -1)
