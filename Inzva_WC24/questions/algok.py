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

def count_prime_factors(number, primes):
    unique_factors = set()  

    for prime in primes:
        while number % prime == 0:
            unique_factors.add(prime)  
            number //= prime
            if number == 1:
                break
        if number == 1:
            break

    return len(unique_factors)  


primes = sieve_of_eratosthenes(10**6)

n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    factors = prime_factors_of_gcd(a, b, primes)
    if factors[0] == -1:
        result = count_prime_factors(a, primes) + count_prime_factors(b, primes)
        print(result)
    else:
        for factor in factors:
            while a % factor == 0:
                a //= factor 
            while b % factor == 0:
                b //= factor
        result = len(factors) + count_prime_factors(a, primes) + count_prime_factors(b, primes)
        print(result)
