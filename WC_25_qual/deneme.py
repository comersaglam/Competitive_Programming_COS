MOD = 10**9 + 7
N,K = list(map(int, input().split()))
v= list(map(int, input().split()))
# Assume array v[1...N] (1-indexed) and given integer K.

# Precompute 'next' array using a two-pointer approach.
next_pos = [-1] * (N + 1)    # next_pos[i] will store the endpoint r if sum(v[i..r]) == K, else -1

l = 1
current_sum = 0
for r in range(1, N+1):
    current_sum += v[r]
    # Adjust left pointer until current_sum <= K
    while l <= r and current_sum > K:
        current_sum -= v[l]
        l += 1
    # Now if current_sum equals K, then record the segment starting at l
    # Note: Because the array is positive, if current_sum equals K then it is unique for that l.
    if current_sum == K:
        next_pos[l] = r  # valid segment from index l to r

# Initialize DP table: dp[i][j] is the number of ways to have chosen j segments from first i elements.
dp = [[0]*4 for _ in range(N+2)]
dp[0][0] = 1

for i in range(0, N):
    # Always propagate the current ways to next index if we skip i+1.
    for j in range(4):
        dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD

    # Check if position (i+1) can start a valid segment.
    start = i+1
    r = next_pos[start]
    if r != -1 and r <= N:
        for j in range(3):  # we can only add segments if we have chosen less than 3 so far
            dp[r][j+1] = (dp[r][j+1] + dp[i][j]) % MOD

# The answer is the number of ways to form exactly 3 segments using the whole array.
# Depending on implementation, you could sum dp[i][3] for all i from 0 to N.
ans = dp[N][3] % MOD
print(ans)
