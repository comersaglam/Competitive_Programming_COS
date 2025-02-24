n, k = list(map(int, input().split()))
target = k
modulo = 10**9 + 7
lst = list(map(int,input().split()))
dp = [ 0 for i in range(target+1)]
dp[0] = 1
for t in range(target +1):
        for coin in lst:
             if t-coin >= 0:
                  dp[t] = dp[t] + dp[t-coin]
print(dp[-1]%modulo)
