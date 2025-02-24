N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

low = arr[0]
high = arr[-1] - arr[0]

