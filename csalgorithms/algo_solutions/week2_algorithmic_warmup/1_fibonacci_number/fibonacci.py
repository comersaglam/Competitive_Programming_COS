def fibonacci_number(n):
    x1 = 1
    x2 = 1
    for i in range(n-2):
        x1, x2 = x2, x1 + x2
    return x2


if __name__ == '__main__':
    input_n = int(input())
    if input_n == 0:
        result = 0
    elif input_n == 1 or input_n == 2:
        result = 1
    else:
        result = fibonacci_number(input_n)
    print(result)
