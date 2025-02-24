n = int(input())
house = list(map(int,input().split()))
a,b,c,d = map(int, input().split())
def hash1(x, a=a, b=b, n=n):
    return (a*x + b) % n
def hash2(x, c=c, d=d, n=n):
    return (c*x + d) % n

filled = set()

definites = []
mights = []
nots = []

num_fill = 0
for i in house:
    if i ==1:
        num_fill += 1


#check for impossible cases:
if ((a == n) and house[b] == 0) or  ((c == n) and house[d] == 0):
    print("-1")
    exit()

i = -1
while len(filled) < num_fill and i<1e7:
    i += 1
    x1 = hash1(i)
    x2 = hash2(i)
    if  not (house[x1] and house[x2]):
        nots.append(i)
    else:
        if not ((x1 in filled) and (x2 in filled)):
            definites.append(i)
            filled.add(x1)
            filled.add(x2)
        else:
            mights.append(i)

if i == 1e7:
    print("-1")
else:
    if len(nots) == 0: print("-1")
    else: print(*nots)
    if len(definites) == 0: print("-1")
    else: print(*definites)
    if len(mights) == 0: print("-1")
    else: print(*mights)
    

