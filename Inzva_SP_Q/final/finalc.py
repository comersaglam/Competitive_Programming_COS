num, x, cap = list(map(int, input().split()))
w = list(map(int, input().split()))
v = list(map(int, input().split()))
pairs = []
for pair in range(x):
    a,b = list(map(int, input().split()))
    pairs.append([a,b])

dp = []
for c in range(cap +1):
    temp2list = []
    for n in range(num+1):
        templist = []
        for i in range(2):
            templist.append(0)
        temp2list.append(templist)
    dp.append(temp2list)
    


"dp = [[[0] * 2] * (num + 1)] * (cap + 1)"
#dp[c][n][usage]
usedindexes = set()
weights = []
values = []
for pair in pairs:
    usedindexes.add(pair[0]-1)
    usedindexes.add(pair[1]-1)
    weights.append(w[pair[0]-1])
    weights.append(w[pair[1]-1])
    values.append(v[pair[0]-1])
    values.append(v[pair[1]-1])
for i in range(num):
    if i not in usedindexes:
        weights.append(w[i])
        values.append(v[i])

for n in range(1, 2*x + 1):
    for c in range(weights[n-1], cap + 1):  #!
        isused = 0
        sol = dp[c-weights[n-1]][n][:]
        solust = dp[c-weights[n-1]][n-1][:]
        ust = dp[c][n-1][:]
        valuem = values[n-1]
        if n%2 != 0:
            if sol[1] == 0:
                usedval = max(sol[0] + valuem, solust[0] + valuem)
            else: usedval = max(solust[0] + valuem, sol[0])
            if usedval > ust[0]: dp[c][n][1] = 1
            dp[c][n][0] = max(usedval, ust[0])

        else:
            solikiust = dp[c-weights[n-1]][n-2][:]
            ikiust = dp[c][n-2][:]

            if sol[1] == 0:
                if solust[1] == 0:
                    usedval = max(sol[0] + valuem, solust[0] + valuem, solikiust[0] + valuem)
                else: usedval = max(sol[0] + valuem, solikiust[0] + valuem)
            elif solust[1] == 0:
                usedval = max(sol[0], solust[0] + valuem, solikiust[0] + valuem)
            else: usedval = max(sol[0], solikiust[0] + valuem)

            nousedval = max(ust[0], ikiust[0])
            
            if usedval > nousedval: dp[c][n][1] = 1
            dp[c][n][0] = max(usedval, nousedval)

for n in range(2*x +1, num + 1):
    for c in range(weights[n-1], cap + 1):  #!
        sol = dp[c-weights[n-1]][n][:]
        solust = dp[c-weights[n-1]][n-1][:]
        ust = dp[c][n-1][:]
        valuem = values[n-1]

        if sol[1] == 0:
            usedval = max(sol[0] + valuem, solust[0] + valuem)
        else: usedval = max(sol[0], solust[0] + valuem)

        if usedval >ust[0]:
            if usedval > ust[0]: dp[c][n][1] = 1
        dp[c][n][0] = max(usedval, ust[0])
    
print(dp[c][n][0])

