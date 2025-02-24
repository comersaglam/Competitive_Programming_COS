n = int(input())
def newram(r,a,b,c):
    new = (a*r+ b)%c
    maxnew = max(new,r)
    for i in range(5*10**3):
        r = new
        new = (a*r+ b)%c
        maxnew = max(maxnew, new)
    return maxnew
maxram = 0

for i in range(n):
    r,a,b,c = list(map(int, input().split()))
    new = newram(r,a,b,c)
    maxram += new

print(maxram)