import math

def sieve_of_eratosthenes(limit):
    sieve_bound = (limit - 1) // 2
    sieve = [True] * (sieve_bound + 1)
    crosslimit = int((math.sqrt(limit) - 1) / 2)

    for i in range(1, crosslimit + 1):
        if sieve[i]:
            for j in range(2 * i * (i + 1), sieve_bound + 1, 2 * i + 1):
                sieve[j] = False

    return {2} | {2 * i + 1 for i in range(1, sieve_bound + 1) if sieve[i]}

limit = 10**4
primes_set = sieve_of_eratosthenes(limit)

n = int(input())
mylist = list(map(int, input().split()))

for i in mylist:
    if i <= limit:
        if i in primes_set:
            print("Yes")
        else:
            print("No")
    else:
        isprime = True
        for prime in primes_set:
            if i % prime == 0:
                isprime = False
                break
        if isprime:
            print("Yes")
        else:
            print("No")
