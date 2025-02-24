MOD = 10**9 + 7

import math

def fp(a,b, modulo=MOD):
    if b== 0: return 1
    if b%2 == 1: return a*fp(a,b-1)%modulo
    else:
        half = fp(a,b/2)
        return half*half %modulo

def fib(n, modulo=MOD):
    A = (1 + math.sqrt(5)) / 2
    B = (1 - math.sqrt(5)) / 2
    fib = (fp(A, n, modulo) - fp(B, n, modulo)) / math.sqrt(5)
    return round(fib) % modulo

def count_combinations(n):
    return fib(n) % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_combinations(n+2)-1)