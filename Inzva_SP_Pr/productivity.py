modulo = 10**9 + 7
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a,b):
    return a * b // gcd(a,b)

n = int(input())
arr = list(map(int, input().split()))