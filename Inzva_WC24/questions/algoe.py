def fp(a,b, modulo):
    if b== 0: return 1
    if b%2 == 1: return a*fp(a,b-1, modulo)%modulo
    else:
        half = fp(a,b/2, modulo)
        return half*half %modulo

a, b, m = list(map(int, input().split()))
print(fp(a, b, m))