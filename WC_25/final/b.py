n1,n2, k_swap = list(map(int, input().split()))
s1 = input()
s2 = input()

dpx = [[0]*(n2+1) for _ in range(n1+1)]
dp = []
for i in range(k_swap+1):
    dpx = []
    dpx = [[0]*(n2+1) for _ in range(n1+1)]
    dp.append(dpx)
#dp[k][n1+1][n2+1] with k swap, LCS btw s1[i] s2[j] ending in dp[k][i][j]

#find lcs
x= 0
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if s1[i-1] == s2[j-1]:
            dp[0][i][j] = dp[0][i-1][j-1]+1
        else:
            # dp[k][i][j] = max(dp[0][i][j-1] , dp[0][i-1][j])
            pass

x= 0
for k in range(1, k_swap+1):
    for i in range(1, n1+1):
        for j in range(1,n2+1):
            if s1[i-1] == s2[j-1]:
                noswap = dp[k][i-1][j-1] + 1
                if dp[k-1][i][j] < min(i,j):
                    swap = max(dp[k-1][i][j] + 1 , dp[k-1][i-1][j-1] + 1)
                else:
                    swap = dp[k-1][i-1][j-1] + 1
            else:
                noswap = 0
                swap = dp[k-1][i-1][j-1] + 1

            dp[k][i][j] = max(swap, noswap)

ans = 0
for i in range(1,n1+1):
    for j in range(1,n2+1):
        ans = max(ans, dp[k_swap][i][j])

print(ans)