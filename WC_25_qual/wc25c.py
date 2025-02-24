#* we will calculate C(n+1,k+1) due to sum of series. n is the first modulo, k is the input
n = 93623149
k = int(input())
k += 1
mod = 1000000007

def fexp (a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return fexp(a * a % mod, b // 2)
    return a * fexp(a, b - 1) % mod

def inv (a):
    return fexp(a, mod - 2)

nom = 1
denom = 1
r = min(k, n - k)

for i in range(r):
    nom = nom * (n - i) % mod
    denom = denom * (i + 1) % mod

res = nom * inv(denom) % mod
if k == 2:
    res += 2
elif k == 3:
    res += 1
print(res % mod)
