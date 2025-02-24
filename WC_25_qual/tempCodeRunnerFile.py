MOD = 10**9 + 7
"""
def inverse(k):
    term = 1  # Corresponds to 1/1! mod MOD, since 1/1! = 1.
    series_sum = term  # Initialize sum with the first term.
    for n in range(2, k + 1):
        inv = pow(n, MOD - 2, MOD)
        term = (term * inv) % MOD
        series_sum = (series_sum + term) % MOD
    return series_sum
"""

def fexp(x, y):
    res = 1
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        y //= 2
    return res

k = int(input())
rooms = 93623148

series_sum = 0
numerator = 1 # factorials
denominator = 1 # inverse factorials
fact_cnt = 1
for i in range(k, rooms + 1):
    series_sum = (series_sum + (numerator * denominator) % MOD) % MOD

    numerator = (numerator * i) % MOD

    fact_cnt += 1
    inv = fexp(fact_cnt, MOD - 2)
    denominator = (denominator * inv) % MOD

print(series_sum)
