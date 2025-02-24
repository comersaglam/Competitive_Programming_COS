n, m = list(map(int, input().split()))
edges = set()
bidirectionals = set()
for _ in range(m):
    a, b = list(map(int, input().split()))
    if (b, a) in edges:
        bidirectionals.add((min(a,b), max(a,b)))
    edges.add((a, b))

bidirectionals = list(bidirectionals)
bidirectionals.sort()

print(len(bidirectionals))
for edge in bidirectionals:
    print(edge[0], edge[1])