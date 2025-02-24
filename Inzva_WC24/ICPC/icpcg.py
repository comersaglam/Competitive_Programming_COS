import math

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

def calc_min(mydk, arr, n):
    dk = 0
    for i in range(0, n):
        dk += math.ceil(arr[i]/mydk)
    return dk
isfound = False
low, high = 0, n
ans = -1
while low <= high:
    mid = (low + high) // 2
    dk = calc_min(arr[mid], arr, n)
    if dk < m:
        high = mid - 1
    elif dk >= m:
        if dk == m:
            isfound = True
        ans = mid
        low = mid + 1

if ans == -1:
    low, high = 0, arr[0]
else:
    low, high = arr[ans], arr[ans+1]

ans2 = -1
while low <= high:
    mid  = (low + high) // 2
    dk = calc_min(mid, arr, n)
    if dk > m:
        high = mid - 1
        
    elif dk <= m:
        ans2 = mid
        low = mid + 1

print(ans2)
