n, k ,l = list(map(int, input().split()))
binalist = list(map(int,input().split()))

for i in range(n-l):

    s = min(binalist[i], binalist[i+l]) + k
    docrash = 0
    for j in range(i,i+l+i):
        if  binalist[j] > s:
            docrash = 1
            break

    if docrash: print("NO")
    else: print("YES")