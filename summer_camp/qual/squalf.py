def min_time_to_complete_tasks(N, T, A):
    pass

n = int(input())
times = list(map(int, input().split()))
dependencies = []
for i in range(n):
    dependencies.append([int(x) - 1 for x in input().split() if x != '-1'])

print(min_time_to_complete_tasks(n, times, dependencies))