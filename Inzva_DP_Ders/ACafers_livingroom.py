MOD = 1000000007

N = int(input().strip())

dp = [0] * (N + 1)

dp[0] = 1
if N >= 1:
    dp[1] = 0
if N >= 2:
    dp[2] = 3
if N >= 3:
    dp[3] = 0

for i in range(4, N + 1):
    dp[i] = (4 * dp[i-2] - dp[i-4]) % MOD

print(dp[N])

n = int(input())
mod = 1000000007

f = [0] * (n+1)
g = [0] * (n+1)
f[0] = 1
f[1] = 0
g[0] = 0
g[1] = 1

for i in range(2,n+1):
    f[i] = ( f[i-2] + 2 * g[i-1] ) % mod
    g[i] = ( f[i-1] + g[i-2] ) % mod
        
print( f[n] )