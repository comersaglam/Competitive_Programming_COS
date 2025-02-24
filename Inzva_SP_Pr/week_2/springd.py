n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
occurences = {}
possibilities = 0

if m == 0:
    zeros = 0
    for ele in arr:
        if ele == 0:
            zeros += 1
    possibilities += zeros*(zeros-1)//2
    possibilities += zeros*(n-zeros)
    print(possibilities)
    quit()


for i in arr:
    if i != 0 and m % i == 0:
        possibilities += occurences.get(m // i, 0)
    occurences[i] = occurences.get(i, 0) + 1

print(possibilities)