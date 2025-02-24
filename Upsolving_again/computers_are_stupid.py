max_num = int(1e7 + 5)
sieve = [True] * max_num
factors = [0] * max_num
primes = []

def find_primes():
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if not sieve[i]:
            continue
        primes.append(i)
        factors[i] = 1
        for k in range(i * i, max_num, i):
            factors[k] = i
            sieve[k] = False

find_primes()

def find_factors (factorset, num):
    while not sieve[num]:
        factorset.add(factors[num])
        num = num // factors[num]
    factorset.add(num)

t = int(input())

for i in range(t):
    a,b = list(map(int,input().split()))
    factorset = set()
    find_factors(factorset, a)
    find_factors(factorset, b)
    print(len(factorset))