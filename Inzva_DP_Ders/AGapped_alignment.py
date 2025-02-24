 #* Global Alignment
first_name = 'inzva'
second_name = 'winterva'

gap = 5
mismatch = 3
match = 5
dp =[ [0 for i in range(len(first_name)+1)] for j in range(len(second_name)+1)]

for i in range(1,len(first_name)+1):
    for j in range(1,len(second_name)+1):
        if (first_name[i-1]==second_name[j-1]): 
            dp[j][i]= dp[j-1][i-1] + match
        else:
            dp[j][i]= max(dp[j][i-1] - gap, dp[j-1][i] - gap, dp[j-1][i-1] - mismatch)

print(dp) 