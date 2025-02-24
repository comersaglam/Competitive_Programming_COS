from collections import deque

n, k = list(map(int, input().split()))

queue = deque()

cnt = 0
for i in range(n):
    person = input()

    if cnt == k:
        queue.append(person)
        cnt = 0
    else:
        print(person)
        cnt += 1

while queue:
    person = queue.popleft()
    if cnt == k:
        queue.append(person)
        cnt = 0
    else:
        cnt += 1
        print(person)