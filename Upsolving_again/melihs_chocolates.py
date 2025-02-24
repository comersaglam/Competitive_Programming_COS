def is_possible(x,y,a,b,pack):
    if pack*b > y:
        return False
    diff = a - b
    #calculate what x can be at maximum, at extreme all packs contains a number of x
    if diff == 0:
        a_cnt = pack
    else:
        a_cnt = (x - (b*pack)) // diff
        a_cnt = min(a_cnt ,pack)
    b_cnt = pack - a_cnt
    if y < (b_cnt * a + a_cnt * b):
        return False
    else:
        return True
    pass
def solve():
    x,y,a,b = list(map(int,input().split()))
    if a < b: a,b = b,a # a is bigger than b
    if x < y: x,y = y,x # x is bigger than y
    low = 0
    high = x // b + 1

    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if is_possible(x,y,a,b,mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

t = int(input())
for i in range(t):
    print(solve())