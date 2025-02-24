n = int(input())
MOD = 1000000007
fib = [0] * 1000031
pow2 = [0] * 1000069
fib[0] = 1
fib[1] = 1
pow2[0] = 1
pow2[1] = 2
for i in range(2, 1000001):
    fib[i] = (fib[i - 1] + fib[i - 2]) % MOD
    pow2[i] = (pow2[i - 1] * 2) % MOD

for _ in range(n):
    m = int(input())
    ans = (pow2[m] - fib[m + 1] + 1) % MOD
    print(ans)