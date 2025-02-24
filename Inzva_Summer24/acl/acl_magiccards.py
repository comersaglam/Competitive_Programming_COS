n = int(input())
log = 1
while 2**log < n:
    log += 1

binlist = [[] for _ in range(log)]
for num in range(1, n+1):
    numyedek = num
    for j in range(log):
        if num % 2 == 1:
            binlist[j].append(numyedek)
        num //= 2
print(log)
for i in range(log):
    print(*binlist[i])