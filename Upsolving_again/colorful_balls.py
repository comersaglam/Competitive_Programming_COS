c, k = list(map(int, input().split()))
balls = list(map(int, input().split()))
balls.sort()

def is_possible(b,k):
    max_ball = b*k
    ball_cnt = 0
    for i , ball in enumerate(balls):
        ball_cnt += min(ball, b)
        if ball_cnt >= max_ball:
            return True
    return False
#cevaba binary search

#possible b's
low = 0

high = int(sum(balls) //k +5)

ans = 0
while low <= high:
    mid = (low + high) // 2
    if is_possible(mid, k):
        ans = mid
        low = mid +1
    else:
        high = mid - 1

print(ans)