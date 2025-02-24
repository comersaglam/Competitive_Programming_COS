from collections import deque

n, m = map(int, input().split())
farm = []
for _ in range(n):
    temp = list(input().strip())
    farm.append(temp)
    

def min_moves_to_escape(n, m, farm):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    tractor_distance = [[float('inf')] * m for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 'M':
                queue.append((i, j, 0))
                tractor_distance[i][j] = 0
    
    while queue:
        x, y, dist = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and farm[nx][ny] != '#' and dist + 1 < tractor_distance[nx][ny]:
                tractor_distance[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 'A':
                start = (i, j)
                break
    
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))
    
    while queue:
        x, y, moves = queue.popleft()
        
        if (x == 0 or x == n-1 or y == 0 or y == m-1) and (farm[x][y] == '.' or farm[x][y] == 'A'):
            return moves
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and farm[nx][ny] != '#':
                if moves + 1 < tractor_distance[nx][ny]:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
    
    return -1


print(min_moves_to_escape(n, m, farm))

