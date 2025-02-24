n = int(input())
arr = list(map(int, input().split()))

stack = [] # will hold pairs of (value, number of times value has been seen)

for i in range(n):
    ele = arr[i]
    if len(stack) == 0:
        stack.append((ele, 1))
    elif ele == stack[-1][0]:
        stack[-1] = (stack[-1][], stack[-1][1] + 1)
    else:
        stack.append((ele, 1))
    if stack[-1][1] == stack[-1][0]:
        stack.pop()

cnt = 0
for ele in stack:
    cnt += ele[1]
print(cnt)
