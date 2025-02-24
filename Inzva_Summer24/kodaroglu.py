MAX_INT = 10**9
Q = int(input())
for i in range(Q):
    n, m = map(int,input().split())
    salaries = list(map(int,input().split()))
    moneys = list(map(int,input().split()))
    dp = [MAX_INT] * (1<<n)
    dp[0] = 0
    #############!
