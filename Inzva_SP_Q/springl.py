k, a, b = list(map(int, input().split()))

def fp(a,b):
    modulo = 10**9 + 7
    if b== 0: return 1
    if b%2 == 1: return a*fp(a,b-1)%modulo
    else:
        half = fp(a,b/2)
        return half*half %modulo

distab = b - a

if k % 2 == 0:
    if fp(2, int(k//2)) > distab:
        print(-1)
        quit()
else:
    if fp(2, int((k+1)//2)) > distab:
        print(-1)
        quit()

k = int(k // 2)
dist = fp(2, k) - 1
print(b + dist)