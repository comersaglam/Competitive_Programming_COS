from collections import deque

n,m = map(int,input().split())
dag = [[] for _ in range(n)]
indegree = [0 for i in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    dag[u].append(v)
    indegree[v]+=1

queue = deque()
result = []
for i in range(n):
    if indegree[i]==0:
        queue.append(i)
        
while queue:
    node = queue.popleft()
    result.append(node)
    for next_node in dag[node]:
        indegree[next_node]-=1
        if indegree[next_node]==0:
            queue.append(next_node)

print(result)