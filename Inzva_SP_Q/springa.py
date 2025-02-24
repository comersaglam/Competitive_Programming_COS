n, k = list(map(int, input().split()))
yaxis = list(map(int,input().split()))
possibilites = 0
def bs (low, high, target, firstx):
    firsty = yaxis[firstx]
    ans = -1
    while high >= low:
        mid = (low + high) // 2
        if int((yaxis[mid] - firsty )/(mid - firstx)) > target:
            high = mid - 1
        else:
            ans = mid
            low = mid + 1
    return ans

for i, ele in enumerate(yaxis):
    x_index = bs(i + 1, n-1, k, i)
    if int((yaxis[x_index] - ele) / (x_index - i)) == k:
        possibilites += 1
print(possibilites)
