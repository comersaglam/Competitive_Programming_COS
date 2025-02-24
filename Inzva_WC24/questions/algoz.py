n = int(input())
lst = list(map(int,input().split()))

dp = [0 for i in range(len(lst))]
for i in range(len(lst)):
    for j in range(i):
        if lst[i] >= lst[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp)+1)