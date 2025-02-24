def log2(x):
    return x.bit_length() - 1

n = int(input())
farray = list(map(int,input().split()))

maxnum = max(farray)
log2 = int(log2(maxnum))
keyturn = log2 // 3 + 1
print(keyturn)
