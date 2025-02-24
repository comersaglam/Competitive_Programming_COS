n = int(input())
lst = list(map(int,input().split()))
target = sum(lst)
if target % 2 == 1:
    print("false")
else:
    target = target // 2
    dp = [ 0 for i in range(target+1)]
    dp[0] = 1

    for i in lst:
        for j in range(target, i-1, -1):
            dp[j] = dp[j] or dp[j-i] 
    if dp[-1]: print("true")
    else: print("false")