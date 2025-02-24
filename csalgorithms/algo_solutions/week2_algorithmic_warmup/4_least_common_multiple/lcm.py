def gcd(a, b):
    a, b = b, a%b
    if b == 0:
        return a
    else:
        return gcd(a,b)
    

def lcm(a, b):
    thisgcd = gcd(a, b)
    lcm = (a/thisgcd)* b
    return int(lcm)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

