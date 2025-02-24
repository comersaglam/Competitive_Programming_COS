q = int(input())
beatenset = set()
for _ in range(q):
    query = list(map(int,input().split()))
    isbeaten = True
    if query[0] == 1:
        beatenset.add(query[1])
    elif query[0] == 2:
        a, b = query[1], query[2]
        for ele in [a, a+b, a-b]:
            if ele not in beatenset:
                isbeaten = False
        if isbeaten: print("GG EZ")
        else: print("GLHF")