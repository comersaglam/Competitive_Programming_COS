MOD = 10**9+7
emin = list(map(int,list(input())))
melih = list(map(int,list(input())))

def fexp(a,b):#a^b
    if b == 0: return 1
    if b == 1: return a
    if b % 2 == 0: return fexp(a,b//2)**2 % MOD
    else: return fexp(a,b//2)**2 * a % MOD

def toasts(num):
    count = 0
    n = len(num)
    for i in range(n):
        temp = (num[i]-1) * fexp(3,len(num)-i-1) % MOD
        count = (count + temp) % MOD
        temp = 4 * fexp(3,len(num)-i-1) % MOD
        count = (count + temp) % MOD
    return count

print(toasts(melih)-toasts(emin))