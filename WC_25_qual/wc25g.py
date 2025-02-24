import heapq
#t = int(input())

n,x,y = list(map(int,input().split())) # n = monster num, x = knight health, y = knight attack
health = list(map(int,input().split()))
boss_attack = list(map(int,input().split()))
scaling = list(map(int,input().split()))

geo = 0
heap = []
for i in range(n):
    if health[i] > y:
        heapq.heappush(heap,(boss_attack[i],health[i],scaling[i]))
    else:
        geo += 1


while x > 0 and heap:
    boss = heapq.heappop(heap)
    boss[1] -= y
    geo += 1
    