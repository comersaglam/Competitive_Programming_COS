import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
x = int(data[1])

coins = list(map(int, data[2:n+2]))

dp = [0] * (x + 1)
dp[0] = 1
modulo = int(1e9 + 7)

for i in range(1, x + 1):
    for c in coins:
        if i >= c:
            dp[i] = (dp[i] + dp[i - c]) % modulo

print(dp[x] % modulo)
   
