def gcd(a, b):
    a, b = b, a%b
    if b == 0:
        return a
    else:
        return gcd(a,b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
