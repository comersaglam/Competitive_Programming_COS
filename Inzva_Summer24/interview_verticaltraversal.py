import heapq
from collections import deque
n = int(input())
graph = [[None,None] for i in range(n + 1)] # [left, right]
positions =[[0,0,i+1] for i in range(n)] # [col, row]
pq_sort = []

for i in range(n-1):
    p, d, c = map(int, input().split())
    graph[p][d] = c

bfs = deque([1])
while bfs:
    p = bfs.popleft()
    left, right = graph[p]
    if left:
        positions[left-1][0] = positions[p-1][0] - 1
        positions[left-1][1] = positions[p-1][1] + 1
        bfs.append(left)
    if right:
        positions[right-1][0] = positions[p-1][0] + 1
        positions[right-1][1] = positions[p-1][1] + 1
        bfs.append(right)

positions.sort()
for position in positions:
    print(position[2], end = ' ')