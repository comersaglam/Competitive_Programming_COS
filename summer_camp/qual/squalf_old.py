from collections import deque

n = int(input())
times = list(map(int, input().split()))
dependencies = []
for i in range(n):
    dependencies.append(list(map(int, input().split())))

from collections import deque

def min_time_to_complete_tasks(N, T, A):
    adj_list = [[] for _ in range(N)]
    in_degree = [0] * N
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                adj_list[j].append(i)
                in_degree[i] += 1

    queue = deque([i for i in range(N) if in_degree[i] == 0])

    min_time = T[:]

    while queue:
        tasks = [queue.popleft() for _ in range(min(2, len(queue)))]  # Take up to 2 tasks
        max_time = max(T[task] for task in tasks)
        for task in tasks:
            for dependent_task in adj_list[task]:
                in_degree[dependent_task] -= 1
                if in_degree[dependent_task] == 0:
                    queue.append(dependent_task)
                min_time[dependent_task] = max(min_time[dependent_task], min_time[task] + T[dependent_task])

    if any(in_degree[i] > 0 for i in range(N)):
        print(-1)
    else:
        print(max(min_time))

min_time_to_complete_tasks(n, times, dependencies)