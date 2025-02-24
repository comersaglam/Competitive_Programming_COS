from collections import Counter

n = int(input())
mystr = list(input())


counts = Counter(mystr)
filtered_str = [item for item in mystr if counts[item] > 1]

n = len(filtered_str)
s = "".join(filtered_str)

if len(s) == 0:
    print(0)
    quit()

dpset = set()
for i in range(n):
    first_name = s[:i]
    second_name = s[i:]
    dp =[ [0 for i in range(len(first_name)+1)] for j in range(len(second_name)+1)]
    for i in range(1,len(first_name)+1):
        for j in range(1,len(second_name)+1):
            if (first_name[i-1]==second_name[j-1]):
                dp[j][i]= dp[j-1][i-1] +1
            else:
                dp[j][i]= max(dp[j][i-1],dp[j-1][i])

    dpset.add(dp[-1][-1])
print(max(dpset)*2)
