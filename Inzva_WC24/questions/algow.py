n = int(input())
target = int(input())
lst = list(map(int,input().split()))

dp = [ 0 for i in range(target+1)]
dp[0] = 1

for i in lst:
    for t in range(i, target+1):
        dp[t] = dp[t] + dp[t-i]

for i in range(target, -1, -1):
    if dp[i] != 0:
        print(i)
        break