n = int(input())
arr = list(map(int, input().split()))
dp = [[2]*n for i in range(n)]

for i in range(n):
    for j in range(i):
        for k in range(j):
            if (arr[k] > arr[i] > arr[j] ) or (arr[k] < arr[i] < arr[j]):
                dp[j][i] = max(dp[j][i], dp[k][j] + 1)

maxlist = []
for line in range(n):
    maxlist.append(max(dp[line]))
mx = max(maxlist)
if mx < 3:
    print(0)
else: print(mx)
