def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers

modulo = 10**9 + 7
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a,b):
    return a * b // gcd(a,b)

limit = 10**6 + 1
phi_arr = [0] * limit
def phi(n, phi_arr):
    for i in range(len(phi_arr)):
        phi_arr[i] = i
    for i in range(2,len(phi_arr)+1):
        if phi[i] == i:
            for j in range(i, len(phi_arr), i):
                phi_arr[j] -= phi_arr[j] // i


