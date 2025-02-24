def binary_search(x, sortlist, n):
    low, high = 0, n
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if sortlist[mid][1] <= x:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer

n = int(input())
sortlist = [(0,0,0)]

for _ in range(n):
    s, e, k = map(int, input().split())
    sortlist.append((s, e, k))


sortlist.sort(key=lambda x: x[1])

dp = [ 0 for i in range(n+1)]

for i in range(1, n + 1):
    k = binary_search(sortlist[i][0],sortlist, n)
    dp[i] += max(dp[i-1], dp[k] + sortlist[i][2])

print(dp[-1])
