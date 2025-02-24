from collections import deque

def bfs_min_cost_to_exit(n, m):
    queue = deque([(n, 0)])
    min_cost = {n: 0}

    while queue:
        current_section, current_cost = queue.popleft()

        next_sections = []
        if current_section % 2 == 0:
            next_sections.append((current_section // 2, current_cost))

        next_sections.extend([(current_section - 1, current_cost + 1), (current_section * 3, current_cost + 1), (current_section + 4, current_cost + 1)])
        
        for next_section, next_cost in next_sections:
            if 0 <= next_section <= 2 * 10**5:
                if next_section not in min_cost or next_cost < min_cost[next_section]:
                    min_cost[next_section] = next_cost
                    queue.append((next_section, next_cost))

    return min_cost.get(m, -1)

n, m = map(int, input().split())
print(bfs_min_cost_to_exit(n, m))