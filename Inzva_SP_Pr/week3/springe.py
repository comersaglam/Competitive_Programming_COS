from collections import deque

def bfs(start, table):
    count = 0
    queue = deque([(start, 0)])

    while queue:
        (x, y), depth = queue.popleft()

        if depth == 3:
            if table[x][y] == 2:
                count += 1
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if depth == 0 and table[nx][ny] == 2:
                queue.append(((nx, ny), depth + 1))
            elif depth == 1 and table[nx][ny] == 0:
                queue.append(((nx, ny), depth + 1))
            elif depth == 2 and table[nx][ny] == 2:
                queue.append(((nx, ny), depth + 1))

    return count

n, m = list(map(int, input().split()))
table = []
table.append([-1] * (m + 2))
for _ in range(n):
    temp = list(map(int, input().split()))
    table.append([-1] + temp + [-1])
table.append([-1] * (m + 2))

count = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if table[i][j] == 2:
            count += bfs((i, j), table)

print(count)