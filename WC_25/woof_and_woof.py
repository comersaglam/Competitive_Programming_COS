t = int(input())
#create a dp[18][32][2]

def solve(n):
    dp = [[[0 for i in range(2)] for j in range(16)] for k in range(len(n)+1)] 
    # len xor tight
    dp[0][0][0] = 1
    dp[0][0][1] = 1

    for ln in range(1,len(n)+1):
        for tight in range(2):
            for xor in range(16):
                if tight == 0:
                    for digit in range(10):
                        dp[ln][xor^digit][0] += dp[ln-1][xor][0]
                else:
                    num = int(n[-ln])
                    for digit in range(num):
                        dp[ln][xor^digit][1] += dp[ln-1][xor^digit][0]
                    dp[ln][xor^num][1] += dp[ln-1][xor^digit][1]

    ans = dp[len(n)][0][1]
    return ans

for i in range(t):
    l, r = list(map(int, input().split()))
    second = solve(str(r)) - solve(str(l-1))
    print(r - l + 1 - second)