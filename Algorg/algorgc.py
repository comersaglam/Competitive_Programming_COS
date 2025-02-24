
def solve(x):
    m = {}
    cnt = 0
    val = []
    for it in x:
        m[it[0]] = m.get(it[0], 0) + 1
        m[it[1] + 1] = m.get(it[1] + 1, 0) - 1
    last = 0
    for key in sorted(m.keys()):
        last += m[key]
        if last > cnt:
            cnt = last
            val = [key]
        elif last == cnt:
            val.append(key)
    return val

def binary_search(left, low, high):
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if rights[mid] >= left:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return rights[res]

n = int(input())
v = []
rights = []
maxcnt = 0

for _ in range(n):
    x = list(map(int, input().split()))
    v.append(x)
    rights.append(x[1])

leftmax = solve(v)
rights.sort()

for left in leftmax:
    right = binary_search(left, 0, n-1)
    if right != -1:
        maxcnt += right - left + 1

print(maxcnt)
    