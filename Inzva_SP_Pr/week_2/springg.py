import heapq

n, k = list(map(int, input().split()))
seat = list(map(int, input().split()))
seat.sort()
gap = []
for i in range(k + 1):
    if i == 0:
        gap.append((seat[i] - 1,0))
    elif i == k:
        gap.append((n - seat[i-1], seat[i-1]))
    else:
        gap.append((seat[i] - seat[i-1] - 1,seat[i-1]))

gapheap = []
for item in gap:
    heapq.heappush(gapheap, (-item[0], item[1]))

guestlist = []

for _ in range(n - k):
    gap_size, start = heapq.heappop(gapheap)
    gap_size = -gap_size
    guestlist.append(start + 1)
    heapq.heappush(gapheap, (-(gap_size - 1), start + 1))

print(*guestlist)