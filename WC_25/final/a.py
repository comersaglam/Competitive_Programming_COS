max_num = int(1e6 + 5)
sieve = [True] * (max_num +1)
primes = []

def find_primes():
    global sieve, primes
    sieve[0] = sieve[1] = False

    for i in range(2, max_num + 1):
        if not sieve[i]:
            continue
        primes.append(i)
        for k in range(i * i, max_num, i):
            sieve[k] = False

find_primes()

k,l = list(map(int, input().split()))


ans = 0
cnt = 0
for prime in primes:
    if prime > l:
        break
    if prime >= k:
        cnt += 1
        ans += prime
    
print(str(cnt) + " " +str(ans))


    