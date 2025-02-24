nums = [2,7,9,3,1]
n = len(nums)
dp = [[0,0] for i in range(n+1)]
dp[1][0] = 0
dp[1][1] = nums[0]
for i in range(2,n+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    dp[i][1] = dp[i-1][0]+ nums[i-1]
print(max(dp[n][0], dp[n][1]))
