n = int(input())
high = []
for i in range(n):
    high.append(int(input()))

high.sort()

score = 0
high2 = []
for i in range((n + 1) // 2):
    high2.append(high[i])
    if i != n - 1 - i:
        high2.append(high[n - 1 - i])

for i in range(1,n):
    score += abs(high2[i] - high2[i-1])

print(score)

3 1 4 1 5 9
4 1 9 1 5 3 

1 2 5 7 9

a b c d  

  5 1 9 2 7