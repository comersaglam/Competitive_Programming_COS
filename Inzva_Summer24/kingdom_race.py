from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

queue = deque()
result = []
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

if len(queue) != 1:
    print("The duels should continue.")
    exit()

while queue:
    if len(queue) > 1:
        print("The duels should continue.")
        exit()
    node = queue.popleft()
    result.append(node)
    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

def res_to_ans(result):
    ans = [0 for _ in range(len(result))]
    for index, prince in enumerate(result):
        ans[prince-1] = index + 1
    return ans

result = res_to_ans(result)
if len(result) == n:
    print("The duels should stop.")
    print(*result)
else:
    print("The duels should continue.")

