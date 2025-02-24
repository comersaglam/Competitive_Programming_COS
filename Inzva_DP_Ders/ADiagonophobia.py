 #* https://codeforces.com/blog/entry/66176
#* https://medium.com/@harshittheone007/counting-derangements-b97ae9ec4582
MOD = 10 ** 9 + 7

n = int(input())

dp = [0 for _ in range(10 ** 6 + 5)]

dp[0] = 1
dp[1] = 0
dp[2] = 0
dp[3] = 0

for i in range(4, 10 ** 6 + 5):
    if i % 2 == 0:
        dp[i] = (i - 1) * dp[i - 1] + 2 * (i - 2) * dp[i - 4]
        dp[i] %= MOD
    else:
        dp[i] = (i - 1) * dp[i - 1] + 2 * (i - 1) * dp[i - 2]
        dp[i] %= MOD

print(dp[n])