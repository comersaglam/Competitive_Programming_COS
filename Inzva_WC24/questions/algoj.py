modulo = (10**9)+7

def fp(a,b):
    global modulo
    if b== 0: return 1
    if b%2 == 1: return a*fp(a,b-1)%modulo
    else:
        half = fp(a,b/2)
        return half*half %modulo
    
def fct(a):
    global modulo
    if a == 1: return 1
    else: return a* fct(a-1)%modulo

def main():
    a, b = list(map(int, input().split()))
    global modulo
    x = fct(a)
    y = fp(  (fct(b) * fct(a-b))%modulo  , modulo-2)
    z = x * y % modulo
    print(z)

main()