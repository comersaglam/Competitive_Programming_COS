n, p = list(map(int, input().split()))

notelist = [[0],[0],[0],
            [0],[0],[0]]

move = 0
for i in range(n):
    s, f = list(map(int, input().split()))
    s -= 1
    if notelist[s][-1] > f:
        move += 1
        notelist[s].pop(-1)
        while notelist[s][-1] > f:
            move += 1
            notelist[s].pop(-1)
        if notelist[s][-1] == f: continue
        else:
            notelist[s].append(f)
            move += 1

    elif notelist[s][-1] < f:
        move += 1
        notelist[s].append(f)
    else: continue

print(move)