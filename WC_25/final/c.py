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

r = (x2-x1) > 0
u = (y2-y1) > 0

dist = abs(x2-x1) + abs(y2-y1)
parr = []
yol = 0
mx = 0
ud = 0
lr = 0
arr_lr = []
arr_ud = []

for i, char in enumerate(wind):
   
    yol += yon[char]
    parr.append(yol)
    mx = max(mx, yol)
    if char == "U" or char == "D":
        ud += yon[char]
        arr_ud.append(ud)
    else:
        lr += yon[char]
        arr_lr.append(lr)



if mx >= dist:
    print(i+1) # index + 1
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
while l <= r:
    mid = (l + r) // 2
    if parr[mid] < dist:
        l = mid + 1
        #sağa git
    else:
        ans = mid
        r = mid - 1
        #sola git ve ans değiştir

print(ans + 1 + loop) # index + 1