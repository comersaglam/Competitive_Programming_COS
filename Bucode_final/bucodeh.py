def calc_move(max, n):
    move = 0
    indx = 0
    for i in range(max - n + 1, max +1):
        move += abs(arr[indx] - i)
        indx += 1
    return move

q = int(input())


for _ in range(q):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    high = arr[-1] + m + 1
    low = 0
    ans = 1000000000007
    while low <= high:
        mid = (low + high) // 2
        a = calc_move(mid, n)
        b = calc_move(mid-1, n)
        ans = min(a, b, ans)
        if a < b:
            low = mid + 1
        elif a > b:
            high = mid - 1
        else:
            i = 0
            while a == b:
                i += 1
                b = calc_move(mid -1- i, n)
            if a < b:
                low = mid + 1
            elif a > b:
                high = mid - 1 - i

    print(ans)