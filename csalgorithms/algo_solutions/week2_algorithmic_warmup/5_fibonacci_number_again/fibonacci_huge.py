def fibonacci_number(n):
    x1 = 1
    x2 = 1
    for i in range(n-2):
        x1, x2 = x2, x1 + x2
    return x2

def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    if n <= 100000:
        return(fibonacci_number(n))% m
    
    elif n > 100000:
        fibo_n = ((1 + 5**(1/2))+ (1 - 5**(1/2)))/5**(1/2)
        return int(fibo_n) % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))