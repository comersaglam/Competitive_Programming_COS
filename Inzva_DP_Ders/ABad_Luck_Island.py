import sys
import math

MOD = int(1e9+7)
INF = int(1e18)
MAX = 101
EPS = 1e-9

dp = [[[-1 for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAX)]

def rec(r, s, p):
    if r == 0:
        return 0
    if s == 0 and p == 0:
        return 1
    if dp[r][s][p] != -1:
        return dp[r][s][p]
    
    rr = r * p
    ss = s * r
    pp = p * s
    t = rr + ss + pp
    dp[r][s][p] = 0
    if p:
        dp[r][s][p] += (rr / t) * rec(r - 1, s, p)
    if s:
        dp[r][s][p] += (ss / t) * rec(r, s - 1, p)
    if s and p:
        dp[r][s][p] += (pp / t) * rec(r, s, p - 1)
    
    return dp[r][s][p]

def solve():
    r, s, p = map(int, input().split())
    for i in range(MAX):
        for j in range(MAX):
            for k in range(MAX):
                dp[i][j][k] = -1
    print(f"{rec(r, s, p):.12f}", end=' ')
    
    for i in range(MAX):
        for j in range(MAX):
            for k in range(MAX):
                dp[i][j][k] = -1
    print(f"{rec(s, p, r):.12f}", end=' ')
    
    for i in range(MAX):
        for j in range(MAX):
            for k in range(MAX):
                dp[i][j][k] = -1
    print(f"{rec(p, r, s):.12f}")

input = sys.stdin.read
t = 1
# t = int(input())
for _ in range(t):
    solve()
