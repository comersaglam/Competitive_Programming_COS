import heapq
import sys
#input = sys.stdin.readline

n = int(input())
bacteria_info = []
for _ in range(n):
    bacteria = list(map(int, input().split()))
    bacteria_info.append(bacteria)

events = []

for info in bacteria_info:
    S, R, L = info
    heapq.heappush(events, (S - 1,      R))
    heapq.heappush(events, (S + L,   -2*R))
    heapq.heappush(events, (S + 2*L +1, R))

oldtime = 0
rate = 0
current_population = 0
max_population = 0

while events:
    time, rate_change = heapq.heappop(events)
    current_population += (time - oldtime) * rate
    oldtime = time
    rate += rate_change

    if max_population < current_population:
        max_population = current_population


print(max_population)