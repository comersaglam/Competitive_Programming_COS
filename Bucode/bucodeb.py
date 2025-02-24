n, m ,k = list(map(int,input().split()))
x, y = list(map(int,input().split()))
sakuras= []
for i in range(k):
    a,b = list(map(int,input().split()))
    sakuras.append([a,b])

flowercount = 0
for coordinate in sakuras:
    a, b = coordinate[0], coordinate[1]
    absa = abs(x - a)
    absb = abs(y - b)
    if absa % 2 == 1:
        if absb % 2 == 1:
            flowercount += 1
        else:
            if absa > absb:
                flowercount += 1
    elif absb % 2 == 1:
        if absb > absa:
            flowercount += 1
        

print(flowercount)