import sys
input = sys.stdin.readline
def fexp(base, exp, mod):
    return pow(base, exp, mod)

def sieve(limit):
    primes = [0] * (limit + 1)
    squares = [False] * (limit + 1)
    p = 2
    
    while p <= limit:
        if primes[p] == 0:
            for i in range(p, limit + 1, p):
                primes[i] += 1

            p_square = p * p
            if p_square <= limit:
                for i in range(p_square, limit + 1, p_square):
                    squares[i] = True
        p += 1
    return primes, squares



n = int(input())
p, a = map(int, input().split())
lee = int(input())

primes, squares = sieve(n)
usdict = {}
for i in range(2, len(primes)):
    if squares[i] != True:
        usdict[primes[i]] = usdict.get(primes[i], 0) + 1

zombies = 1
#print(usdict)
for us in usdict.keys():
    agg = fexp(a, us, p)
    if agg > p/2:
        agg = agg - p
    if us & 1:
        agg = -agg
    #print(agg)
    zombies += agg* usdict[us]

#print(zombies)
if zombies >= lee:
    print("Lee needs a better plan!")
else:
    print("Lee will kill them all!")
            
