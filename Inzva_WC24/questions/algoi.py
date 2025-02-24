n, q = list(map(int,input().split()))
ranges = []
for i in range(n):
    x,y = list(map(int,input().split()))
    ranges.append((x,y))
ranges.sort(key=lambda x: x[0])
numbers = []
for i in range(q):
    numbers.append(int(input()))

for number in numbers:
    low, high = 0, n - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if ranges[mid][0] <= number <= ranges[mid][1]:
            found = True
            break
        elif number < ranges[mid][0]:
            high = mid - 1
        else:
            low = mid + 1
    print("Yes" if found else "No")