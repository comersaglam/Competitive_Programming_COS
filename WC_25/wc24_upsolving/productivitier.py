n = int(input())
arr = list(map(int, input().split()))

max_num = int(1e6 + 5)
sieve = [True] * max_num
primes = []

def find_primes():
    global sieve, primes
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if not sieve[i]:
            continue
        primes.append(i)
        for k in range(i * i, max_num, i):
            sieve[k] = False


find_primes()

factors = {}

for prime in primes:
    factor = []
    for i in range(len(arr)):
        if arr[i] % prime == 0:
            cnt = 0
            while arr[i] % prime == 0:
                arr[i] //= prime
                cnt += 1
            factor.append(cnt)
        else:
            factor.append(0)
    factors[prime] = factor

ans = 1
if len(arr) == 2:
    ans = arr[0] * arr[1]
elif len(arr) == 1:
    ans = arr[0]
else:
    arr.sort()
    ans *= arr[1]

for prime, factor in factors.items():
    factor.sort()
    ans *= prime ** factor[1]


print(ans)