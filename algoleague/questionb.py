n = int(input())
p11 = list(map(int,input().split()))
p12 = list(map(int,input().split()))
p13 = list(map(int,input().split()))
p21 = list(map(int,input().split()))
p22 = list(map(int,input().split()))
p23 = list(map(int,input().split()))

tri1 = [p11, p12, p13]
tri2 = [p21, p22, p23]

def diff(p1, p2):
    return (p1[0] - p2[0]) + (p1[1] - p2[1])


def tri_power(p1, p2, p3):
    return diff(p2, p1) + diff(p3, p1)


def power_calc(n, tri1, tri2):
    power1 = tri_power(*tri1)
    power2 = tri_power(*tri2)

    if n == 1:
        return power1
    elif n == 2:
        return power1
    for i in range(3, n+1):
        p2 = (tri1[1][0] + power2, tri1[1][1] + power2)
        p3 = (tri1[2][0] + power1, tri1[2][1] + power1)

        power1, power2 = power2, (tri_power(tri1[0], p2, p3))
    
    return tri_power(tri1[0], p2, p3)


print(power_calc(n, tri1, tri2))


        