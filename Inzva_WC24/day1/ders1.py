 #* normal pc 2*10^8 unit operation per second olacak şekilde hesaplanır
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
    a = int(input("a"))
    b = int(input("b"))
    global modulo
    x = fct(a)
    y = fp(  (fct(b) * fct(a-b))%modulo  , modulo-2)
    z = x * y % modulo
    print(z)

main()

###########################

def gcd(a,b):
    if b== 0: return a
    return gcd(b, a%b)

############################

def sieve_of_eratosthenes(limit):
    sieve_bound = (limit - 1) // 2
    sieve = [True] * (sieve_bound + 1)
    crosslimit = int((math.sqrt(limit) - 1) / 2)
    for i in range(1, crosslimit + 1):
        if sieve[i]:
            for j in range(2*i*(i + 1), sieve_bound + 1, 2*i + 1):
                sieve[j] = False
    return [2] + [2*i + 1 for i in range(1, sieve_bound + 1) if sieve[i]]

def binary_search():
    pass
