from collections import deque
#append and popleft
n = int(input())
bfs = deque([[n,0]])
num = bfs.popleft()
numset = set()

while num[0] != 0:
    turn = num[1]
    for digit in str(num[0]):
        digit = int(digit)
        if (num[0] - digit) not in numset:
            numset.add(num[0] - digit)
            bfs.append([num[0] - digit,turn + 1])
    num = bfs.popleft()

print(num[1])