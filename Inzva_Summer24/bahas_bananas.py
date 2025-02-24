import sys
input = sys.stdin.readline

def merge(node):
    x = 2*node
    seg[node] = seg[x] + seg[x+1]
    open_st[node] = open_st[x] + open_st[x + 1]

def build(node, start, end):
    if start == end:
        seg[node] = arr[start-1]
        open_st[node] = isopen[start-1]
        return
    mid = (start + end) // 2
    build(2*node, start, mid)
    build(2*node + 1, mid + 1, end)
    merge(node)

def update(node, start, end, pos, val):
    if start == end:
        isopen[start-1] = isopen[start-1] ^ 1
        if isopen[start-1] == 1:
            seg[node] = arr[start-1]
        else:
            seg[node] = 0
        open_st[node] = isopen[start-1]
        return
    mid = (start + end) // 2
    if pos <= mid:
        update(2*node, start, mid, pos, val)
    else:
        update(2*node + 1, mid + 1, end, pos, val)
    merge(node)

def query(node, start, end, ql, qr): #ql and qr are inclusive
    if start > qr or end < ql:
        return (0, 0)
    if start >= ql and end <= qr:
        return (open_st[node] ,seg[node])
    mid = (start + end) // 2
    l_opens, left_st = query(2*node, start, mid, ql, qr)
    r_opens, right_st = query(2*node + 1, mid + 1, end, ql, qr)
    return (l_opens + r_opens,left_st + right_st)

n = int(input())
arr = list(map(int, input().split()))
seg = [0] * (4 * n)
isopen = [1] * n
open_st = [0] * (4 * n)
build(1, 1, n)

q = int(input())

for _ in range(q):
    qry = list(map(int, input().split()))
    if len(qry) == 3:
        t, l, r = qry
        opencnt, sumquery = query(1, 1, n, l, r)
        if opencnt == 0:
            print(0)
        else:
            print(sumquery// opencnt)
    elif len(qry) == 2:
        t, pos = qry
        update(1, 1, n, pos, 0)
