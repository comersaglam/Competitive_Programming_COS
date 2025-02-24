n = int(input())
dishes = [list(map(int, input().split())) for _ in range(n)]

dishes.sort(key=lambda x: (x[0], x[1]))

sourness = [dish[1] for dish in dishes]

def lis(sequence):
    if not sequence:
        return 0
    
    dp = [sequence[0]]
    for s in sequence[1:]:
        if s >= dp[-1]:
            dp.append(s)
        else:
            left, right = 0, len(dp) - 1
            while left < right:
                mid = (left + right) // 2
                if dp[mid] <= s:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = s
    
    return len(dp)

print(lis(sourness))
