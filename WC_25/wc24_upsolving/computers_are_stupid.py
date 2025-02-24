max_num = int(2e5 + 5)
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

def gcd(a,b):
    
k,l = list(map(int, input().split()))

if l <=2:
    print(0)
k = max(k,3)

ans = 0
cnt = 0
for prime in primes:
    if prime > l:
        break
    if prime >= k:
        cnt += 1
        ans += prime
    
print(str(cnt) + " " +str(ans))


    