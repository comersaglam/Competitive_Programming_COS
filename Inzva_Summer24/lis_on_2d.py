 #* we need to find the longest increasing subsequence in a 2D matrix
from collections import deque

matrix = [[],[]] # input will be given here
n, m = len(matrix), len(matrix[0])
dag = [[] for _ in range(n*m)]
coordinates = [[0,1],[1,0],[0,-1],[-1,0]]
indegree = [0 for _ in range(n*m)]
for i in range(n):
    for j in range(m):
        for x, y in coordinates:
            if 0 <= i+x < n and 0 <= j+y < m and matrix[i][j] < matrix[i+x][j+y]:
                dag[i*m+j].append((i+x)*m+j+y)
                indegree[(i+x)*m+j+y] += 1 

queue = deque()
result = 0
for i in range(n*m):
    if indegree[i] == 0:
        queue.append(i)
        result = 1

while queue:
    node = queue.popleft()
    for neighbor in dag[node]:
        indegree[neighbor] -= 1
        result = max(result, indegree[neighbor]+1)
        if indegree[neighbor] == 0:
            queue.append(neighbor)  
print(result)