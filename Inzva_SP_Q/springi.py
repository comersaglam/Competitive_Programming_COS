import sys

modulo = 10**9 + 7

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def modInverse(a, p):
    return power(a, p - 2, p)

def precomputeFactorials(n, p):
    fact = [1] * (n + 1)
    invFact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % p
    invFact[n] = modInverse(fact[n], p)
    for i in range(n, 0, -1):
        invFact[i - 1] = (invFact[i] * i) % p
    return fact, invFact

def comb(n, k, p, fact, invFact):
    if k < 0 or k > n:
        return 0
    return fact[n] * invFact[k] * invFact[n - k] % p

n = int(input())
mlist = [int(sys.stdin.readline()) for _ in range(n)]
max_m = max(mlist)

fact, invFact = precomputeFactorials(max_m, modulo)

for m_ in mlist:
    chances = 1
    for m in range(1, ((m_ + 1) // 2) + 1):
        for r in range(m, m_ - m + 1):
            chances = (chances + comb(m_ - m, r, modulo, fact, invFact)) % modulo
    sys.stdout.write(str(chances) + "\n")
