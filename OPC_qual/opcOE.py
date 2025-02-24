S1 = input()
S2 = input()

dp = [[0 for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
dp[0][0] = 0

for i in range(1, len(S1)+1):
    if S1[i-1] == "O":
        dp[i][0] = dp[i-1][0] - (dp[i-1][0]+1)%2 + 2
    else:
        dp[i][0] = dp[i-1][0] - dp[i-1][0]%2 + 2

for j in range(1, len(S2)+1):
    if S2[j-1] == "O":
        dp[0][j] = dp[0][j-1] - (dp[0][j-1]+1)%2 + 2
    else:
        dp[0][j] = dp[0][j-1] - dp[0][j-1]%2 + 2


for i in range(1, len(S1)+1):
    for j in range(1, len(S2)+1):
        if S1[i-1] == "O" and S2[j-1] == "E":
            dp[i][j] = min(dp[i-1][j] - (dp[i-1][j]+1)%2 + 2, dp[i][j-1] - dp[i][j-1]%2 + 2) 
        elif S1[i-1] == "O" and S2[j-1] == "O":
            dp[i][j] = min(dp[i-1][j] - (dp[i-1][j]+1)%2 + 2, dp[i][j-1] - (dp[i][j-1]+1)%2 + 2)
        elif S1[i-1] == "E" and S2[j-1] == "E":
            dp[i][j] = min(dp[i-1][j] - dp[i-1][j]%2 + 2, dp[i][j-1] - dp[i][j-1]%2 + 2)
        elif S1[i-1] == "E" and S2[j-1] == "O":
            dp[i][j] = min(dp[i-1][j] - dp[i-1][j]%2 + 2, dp[i][j-1] - (dp[i][j-1]+1)%2 + 2)

print(dp[-1][-1])