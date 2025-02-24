n, p = list(map(int,input().split()))
soulmatelist = list(map(int,input().split()))
soulmateset = set()
zeros = 0
halves = 0
for ele in soulmatelist:
    mod = ele % p
    if mod == 0:
        zeros += 1
    elif p % 2 == 0 and mod == p // 2:
        halves += 1
    else:
        soulmateset.add(ele % p)

if zeros >= 2 or halves >= 2:
    print("Yes")
else:
    for ele in soulmateset:
        if (p - ele) % p in soulmateset:
            print("Yes")
            break
    else:
        print("No")