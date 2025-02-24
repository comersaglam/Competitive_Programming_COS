n = int(input())
xf,yf = list(map(int, input().split()))
arr = []
for i in range(n):
    x,y = list(map(int, input().split()))
    arr.append((x,y))

a = arr[:n//2]
b = arr[n//2:]

map1 = {} # (x,y,k : cnt) 
map2 = {} # (x,y : k)
map2[(xf,yf)] = 0

for mask in range(1<<len(a)):
    xt, yt = 0,0
    for i in range(len(a)):
        if mask & (1<<i):
            x,y = a[i]
            xt += x
            yt += y

    k = mask.bit_count()
    xt = xf - xt
    yt = yf - yt
    if map2.get((xt,yt),0) == k:
        map1[(xt,yt,k)] = map1.get((xt,yt,k), 0) + 1
    else:
        map1[(xt,yt,k)] = 1
        map2[(xt,yt)] = k

k_arr = [0] * (n + 1)

for mask in range(1<<len(b)):
    xt, yt = 0,0
    for i in range(len(b)):
        if mask & (1<<i):
            x,y = b[i]
            xt += x
            yt += y
    k = mask.bit_count()

    if (xt,yt) in map2:
        k_old = map2[(xt,yt)]
        a = k_old + k
        k_arr[a] += map1[xt,yt,k_old]

for i in range(1,len(k_arr)):
    print(k_arr[i], end = "\n")
