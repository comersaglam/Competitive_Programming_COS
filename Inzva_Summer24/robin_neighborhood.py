n = int(input())
graph = dict()
for i in range(n):
    u,v = map(int,input().split())
    if u not in graph: graph[u] = []
    graph[u].append(v)

dp0 = [-1] * (n+1) 
dp1 = [-1] * (n+1)
visited = [False] * (n+1)
values = list(map(int,input().split()))

def dfs(node):
    if visited[node]: return
    visited[node] = True
    rob = 0
    for i in graph[node]:
        rob 


#########!