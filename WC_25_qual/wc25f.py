MOD = 10**9 + 7
N,K = list(map(int, input().split()))
v= list(map(int, input().split()))


ends = [-1] * (N)
r = 0
l = 0
sum_segment = 0
while l < N:
    while r < N and sum_segment < K:
        sum_segment += v[r]
        r += 1
    if sum_segment == K:
        ends[l] = r-1
    sum_segment -= v[l]
    l += 1


dp = [[0]*(N+1) for _ in range(4)]
# dp[i][j] --> i is the number of segments (0-4) and j is the number of elements (0-N)

for i in range(N+1):
    dp[0][i] = 1

for i in range(1,4):
    for j in range(i, N+1):
        if ends[j-1] != -1:
            dp[i][ends[j-1] + 1] = dp[i-1][j-1] % MOD
    # prefix sum the row
    for j in range(1, N+1):
        dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD

ans = dp[3][-1] % MOD
print(ans)