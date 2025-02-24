n, m, c = map(int, input().split())
values = list(map(int, input().split()))
constraints = [tuple(map(int, input().split())) for _ in range(c)]

#order values such that constraints are one after another. than normal bonds come.
c0dict = {}
c1dict = {}
for c0,c1 in constraints:
    c0dict[c0] = c1
    c1dict[c1] = c0

val_ordered = []
for i in range(n):
    if i in c0dict:
        val_ordered.append(values[i])
        val_ordered.append(values[c0dict[i]])
for i in range(n):
    if i not in c0dict and i not in c1dict:
        val_ordered.append(values[i])

dppre = [0 for _ in range(m+1)]
dppost = [0 for _ in range(m+1)]

#calculate constrainted bonds
for i in range(0, 2*c, 2):
    dppost[1] = max(dppre[0] + val_ordered[i+1], dppre[1])
    for j in range(2, m+1):
        dppost[j] = max(dppre[j], dppre[j-1]+val_ordered[i+1], dppre[j-2]+val_ordered[i+1]+val_ordered[i])
    dppre = dppost.copy()

dp = [[0 for _ in range(m+1)] for _ in range(n+1- (2*c))]
dp[0] = dppre.copy()

#knapsack for normal bonds
for i in range(1, n+1- (2*c)):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + val_ordered[i+2*c-1])

print(dp[n-2*c][m])