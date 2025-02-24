x1,y1 = list(map(int, input().split()))
x2,y2 = list(map(int, input().split()))
n = int(input())
wind = input()
yon = dict()
if y2>y1:
    yon["D"] = 0
    yon["U"] = 2
else:
    yon["D"] = 2
    yon["U"] = 0
if x2 > x1:
    yon["R"] = 2
    yon["L"] = 0
else:
    yon["R"] = 0
    yon["L"] = 2

dist = abs(x2-x1) + abs(y2-y1)
parr = []
yol = 0
mx = 0

for i, char in enumerate(wind):
    yol += yon[char]
    parr.append(yol)
    mx = max(mx, yol)
    if mx >= dist:
        print(i)
        exit()

if parr[-1] == 0:
    print(-1)
    exit()

loop = (dist//parr[-1]) * n
dist = dist % parr[-1]
if dist == 0:
    loop -= n
    dist += parr[-1]
l = 0
r = n-1
ans = -1
while l < r:
    mid = (l + r) // 2
    if parr[mid] < dist:
        l = mid + 1
        #sağa git
    else:
        ans = mid
        r = mid
        #sola git ve ans değiştir
if ans == -1:
    ans = n-1
print(ans + 1 + loop)