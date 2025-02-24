n = int(input())
streets = list(map(int, input().split()))
k = int(input())
guards = []

for i in range(k):
    s, e = map(int, input().split())
    guards.append((n - s + 1, -1))
    guards.append((n - e, 1))

guards.sort()

intensity = 0
passing_guards = 0
last_ind = 0
act_prev = 0

street_indexes = [0] * n

for i, ele in enumerate(guards):
    ind, act = ele
    if i < len(guards) - 1 and guards[i + 1][0] == ind:
        act_prev += act
        continue
    
    if act >= 1:
        passing_guards += (1 + act_prev)
    elif act <= -1:
        passing_guards += (-1 + act_prev)
    
    if act_prev % 2 == 1:
        last_ind = ind
        act_prev = 0
        continue

    if passing_guards % 2 == 0:
        for j in range(last_ind, ind):
            intensity += streets[j]
        last_ind = ind
        act_prev = 0
    else:
        last_ind = ind
        act_prev = 0

print(intensity)
