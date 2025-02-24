MOD = 10**9 + 7

N, K = map(int, input().split())

dp1 = [0 for _ in range(N + 1)] # almadığımız senaryo
dp0 = [0 for _ in range(N + 1)] # aldığımız senaryo
dpf = [0 for _ in range(N + 1)] # farkların prefix sum arrayi
dp0[1] = 1
dp1[1] = 1


for i in range(2, K+1):
    dp0[i] = 2*dp0[i-1] % MOD
    dp1[i] = 2*dp1[i-1] % MOD

for i in range(K+1, N + 1):
    dp0[i] = (dp0[i-1] + dp1[i-1]) % MOD
    dp1[i] = (dp0[i] - dp1[i-K] - dp1[i-K-1] + dpf[i-1] - dpf[i-K]) % MOD
    dpf[i] = (dp0[i] - dp1[i] + dpf[i-1]) % MOD

result = (dp0[N] + dp1[N]) % MOD
print(result)
