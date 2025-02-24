import math
import sys

def sieve_of_eratosthenes(limit):
    sieve_bound = (limit - 1) // 2
    sieve = [True] * (sieve_bound + 1)
    crosslimit = int((math.sqrt(limit) - 1) / 2)
    for i in range(1, crosslimit + 1):
        if sieve[i]:
            for j in range(2*i*(i + 1), sieve_bound + 1, 2*i + 1):
                sieve[j] = False
    return [2] + [2*i + 1 for i in range(1, sieve_bound + 1) if sieve[i]]

def prime_factors_of_gcd(x, y, primes):
    gcd_value = math.gcd(x, y)
    if gcd_value == 1:
        return [-1]

    factors = []
    for prime in primes:
        if prime * prime > gcd_value:
            break
        if gcd_value % prime == 0:
            factors.append(prime)
            while gcd_value % prime == 0:
                gcd_value //= prime
    if gcd_value > 1:
        factors.append(gcd_value)
    return factors

def process_codes():
    Q = int(sys.stdin.readline())
    input_pairs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]

    primes = sieve_of_eratosthenes(10**4)
    for x, y in input_pairs:
        factors = prime_factors_of_gcd(x, y, primes)
        print(' '.join(map(str, factors)))

process_codes()
