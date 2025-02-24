n,m = list(map(int, input().split()))
edges = {i: [] for i in range(1, n+1)}
visiteds = {i: "u" for i in range(0, n+1)}
for _ in range(m):
    x,y = list(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)

finallist= []
    


