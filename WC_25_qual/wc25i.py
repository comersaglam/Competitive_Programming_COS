from collections import deque
import sys

n,m = list(map(int, input().split()))
grid = []
for i in range(n):
    grid.append(input())

# . = pass through, # = wall
coordinates = []
for i in range(m):
    coordinates.append(list(map(int, input().split())))

query = int(input())

min_m_grid_id = [[float('inf') for j in range(n)] for i in range(n)] # (instrument_id, min_distance)
min_m_grid_dist = [[float('inf') for j in range(n)] for i in range(n)] # (instrument_id, min_distance)
max_m_grid_id = [[float('-inf') for j in range(n)] for i in range(n)] # (instrument_id, max_distance)
max_m_grid_dist = [[float('-inf') for j in range(n)] for i in range(n)] # (instrument_id, max_distance)

for index, (x, y) in enumerate(coordinates):
    visiteds = set()
    instrument_id = index + 1
    start = (x,y,0) # x, y, distance
    q = deque()
    q.append(start)
    visiteds.add((x,y))

    if min_m_grid_dist[x][y] > 0:
        min_m_grid_id[x][y] = instrument_id
        min_m_grid_dist[x][y] = 0
    if max_m_grid_dist[x][y] < 0:
        max_m_grid_id[x][y] = instrument_id
        max_m_grid_dist[x][y] = 0

    while q:
        x, y, d = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if  0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.' and (nx,ny) not in visiteds:
                if min_m_grid_dist[nx][ny] > d + 1:
                    min_m_grid_id[nx][ny] = instrument_id
                    min_m_grid_dist[nx][ny] = d + 1
                if max_m_grid_dist[nx][ny] < d + 1:
                    max_m_grid_id[nx][ny] = instrument_id
                    max_m_grid_dist[nx][ny] = d + 1
                q.append((nx, ny, d + 1))
                visiteds.add((nx,ny))


for i in range(query):
    x, y = list(map(int, input().split()))
    if min_m_grid_id[x][y] == float('inf'):
        print(-1,-1)
    else:
        print(min_m_grid_id[x][y], max_m_grid_id[x][y])


