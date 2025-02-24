def solve():
    import sys, math
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    mod = 10**9+7
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    
    max_small = 10**6
    spf = list(range(max_small+1))
    for i in range(2, int(max_small**0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i*i, max_small+1, i):
                if spf[j] == j:
                    spf[j] = i
    primes = [i for i in range(2, max_small+1) if spf[i] == i]
    
    def is_prime(n):
        if n < 2:
            return False
        smalls = (2, 3, 5, 7, 11)
        for p in smalls:
            if n == p:
                return True
            if n % p == 0:
                return False
        d = n - 1
        s = 0
        while d % 2 == 0:
            s += 1
            d //= 2
        for a in smalls:
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = (x * x) % n
                if x == n - 1:
                    break
            else:
                return False
        return True
    
    def factorize(n):
        fac = {}
        if n < 2:
            return fac
        if n <= max_small:
            while n != 1:
                p = spf[n]
                cnt = 0
                while n % p == 0:
                    n //= p
                    cnt += 1
                fac[p] = fac.get(p, 0) + cnt
            return fac
        
        if is_prime(n):
            fac[n] = 1
            return fac
        temp = n
        for p in primes:
            if p * p > temp:
                break
            if temp % p == 0:
                cnt = 0
                while temp % p == 0:
                    temp //= p
                    cnt += 1
                fac[p] = fac.get(p, 0) + cnt
            if temp == 1:
                break
        if temp != 1:
            fac[temp] = fac.get(temp, 0) + 1
        return fac
    
    cum_factors = {}
    out_lines = []
    for a in arr:
        facs = factorize(a)
        for p, cnt in facs.items():
            cum_factors[p] = cum_factors.get(p, 0) + cnt

        ans = pow(2, len(cum_factors), mod)
        out_lines.append(str(ans))
    
    divisors = 1
    for exp in cum_factors.values():
        divisors = (divisors * (exp + 1)) % mod
    divisors = (divisors * 2) % mod
    out_lines.append(str(divisors))
    
    sys.stdout.write("\n".join(out_lines))
