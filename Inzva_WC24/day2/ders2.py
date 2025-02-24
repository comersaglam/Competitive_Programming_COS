 #! Hold query/cache for optimization

cache = {}
def fib(n):
    if n in cache:
        return cache[n]
    
    if n == 0: return 0
    if n == 1: return 1

    cache[n] = fib(n-1)+ fib(n-2)

guery = [2,10,30,5]
n = 10
a, b = 1

for i in range(n):
    cache[i] = cache[i-1] + cache[i-2]
