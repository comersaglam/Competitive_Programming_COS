from collections import deque
n = int(input())
weigths = list(map(int, input().split()))
direction = input().split()


balls = []
for i in range(n):
    balls.append([weigths[i], direction[i]])

ballstack = deque()
for i in range(n):
    if balls[i][1] == "R":
        ballstack.append(balls[i])

    if balls[i][1] == "L":
        isequal = False
        while len(ballstack) != 0 and ballstack[-1][0] <= balls[i][0] and ballstack[-1][1] == "R":
            if ballstack[-1][0] == balls[i][0]:
                ballstack.pop()
                isequal = True
                break
            ballstack.pop()

        if not isequal:
            if len(ballstack) == 0 or ballstack[-1][1] == "L":
                ballstack.append(balls[i])

print(len(ballstack))
