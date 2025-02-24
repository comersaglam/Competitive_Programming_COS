n, m = list(map(int, input().split()))
nodelist = []
for _ in range(n):
    a,b = list(map(int, input().split()))
    nodelist.append([a,b])

pair_count = 0
slidedict = dict()
for node in nodelist:
    slide_amount = node[1] - m*node[0]
    if slide_amount in slidedict:
        pair_count += slidedict[slide_amount]
    slidedict[slide_amount] = slidedict.get(slide_amount, 0) + 1

print(pair_count)
