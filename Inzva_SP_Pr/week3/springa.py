from collections import deque

n, m = list(map(int, input().split()))
start, end = list(map(int, input().split()))
adj_list = {}
visitedlist = [0] * (n+1)
for _ in range(n):
    x = list(map(int, input().split()))
    adj_list[x[0]] = x[2:]
# x = 1 2 3 4 means room 1 has 2 doors to room 3 and 4

def bfs(start, end, adj_list):
    queue = deque([start])
    distance = {start: 0}

    while queue:
        current_room = queue.popleft()
        if current_room == end:
            return distance[current_room]
        for neighbor in adj_list[current_room]:
            if neighbor not in distance:
                queue.append(neighbor)
                distance[neighbor] = distance[current_room] + 1

    return -1

min_distance = bfs(start, end, adj_list)
print(min_distance)