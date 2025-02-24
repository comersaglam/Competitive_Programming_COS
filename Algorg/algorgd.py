modulo = 998244353

n = int(input())
metus = input()

mcount = 0
ecount = 0
tcount = 0
ucount = 0

for c in metus:
    if c == "M":
        mcount += 1
    if c == "E":
        ecount = ecount + mcount % modulo
    if c == "T":
        tcount = tcount + ecount % modulo
    if c == "U":
        ucount = ucount + tcount % modulo

print(ucount % modulo)