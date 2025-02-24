n,k = list(map(int(), input().split()))

MOD = 10**9 + 7

def sieve(limit=3*(10**6)):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes
primes = sieve()

numbers_of_factors = []
factors = []
def find_prime_factors(k, primes):
    for p in primes:
        if p * p > k:
            break
        if k % p == 0:
            num = 0
            while k % p == 0:
                num += 1
                k //= p
            factors.append(p)
            numbers_of_factors.append(num)
    if k > 1:
        factors.append(k)
        numbers_of_factors.append(1)

find_prime_factors(k, primes)


