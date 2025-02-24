from collections import deque

N = int(input().strip())
parents = list(map(int, input().strip().split()))
Q = int(input().strip())

adj = [[] for _ in range(N+1)]
for i, parent in enumerate(parents, start=2):
    adj[parent].append(i)

depths = [0] * (N+1)
queue = deque([1])
while queue:
    node = queue.popleft()
    for child in adj[node]:
        depths[child] = depths[node] + 1
        queue.append(child)

print(depths[Q])

