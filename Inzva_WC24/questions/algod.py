n = int(input())
mylist = list(map(int, input().split()))
def combs(a):
    if len(a) == 0:
        return [0]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+a[0]]
    return cs
res = list(map(abs, combs(mylist)))
res = sorted(res)
res.pop(0)
print(res[0])