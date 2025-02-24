import math

n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd_of_lcms(arr):
    n = len(arr)
    lcm_first_last = lcm(arr[0], arr[-1])
    gcd_of_lcms = lcm_first_last

    for i in range(n):
        for j in range(i + 1, n):
            gcd_pair = gcd(arr[i], arr[j])
            gcd_of_lcms = gcd(gcd_of_lcms, gcd_pair)

    return gcd_of_lcms



result = gcd_of_lcms(n, arr)
print(result)




