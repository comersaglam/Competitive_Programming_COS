r, c = list(map(int, input().split()))
r1 = list(map(int, input().split()))
c1 = list(map(int, input().split()))

cipher = [] # r x c matrix
for i in range(r):
    cipher.append(list(map(int, input().split())))

rows = []
cols = []

temp = 0
for i in r1:
    temp = temp ^ i
rows.append(temp)

temp = 0
for i in c1:
    temp = temp ^ i
cols.append(temp)

for i in range(1,c):
    temp = cipher[0][i] ^ rows[0] ^ r1[i]
    cols.append(temp)

for i in range(1,r):
    temp = cipher[i][0] ^ cols[0] ^ c1[i]
    rows.append(temp)

for i in range(r):
    row = []
    for j in range(c):
        temp = cipher[i][j] ^ rows[i] ^ cols[j]
        row.append(temp)
    print(*row)