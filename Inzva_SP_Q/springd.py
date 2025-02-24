 #! 1*2 + 2*3 ... = n-1 * n * n+1 / 6. dont forget additional /2

n = int(input())
enjoy = list(map(int, input().split()))
enjoy.sort()

modulo = 10**9 + 7
ans = 0

for i in range(0, n-3):
    k = n - i
    ns = int((k-3)*(k-2)*(k-1)/6)  % modulo
    ans += enjoy[i] * ns % modulo
    ans += enjoy[n-1 - i] * ns  % modulo

print((ans%modulo))