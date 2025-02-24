sum_, n , x = list(map(int,input().split()))
sum_ = sum_ - n
short, long = sorted((x, n-x-1))
k = 1
#k = dogukan's score
turn = 1
istop = 0
point = 0

while turn <= short:
    if turn**2 <= sum_:
        turn +=1
    else:
        istop = 1
        break
if istop:
    k+= turn - 1
    print(int(k))
else:
    sum_ -= turn ** 2
    while turn <= long:
        point += turn + short
        if point <= sum_:
            turn += 1
        else:
            istop = 1
            break
    if istop:
        k += turn -1
        print(int(k))
    else:
        while point <= sum_:
            point += n
            turn += 1
        k += turn -1
        print(int(k))
        #kmax =(x+1)*(2*k-x)/2 + (n-x-1)*(2*k-n+x)/2