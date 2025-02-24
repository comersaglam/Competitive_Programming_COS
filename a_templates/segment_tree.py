# Description: Segment Tree implementation in Python
# index 1 based to work with the formulas 2* and 2* + 1

import sys
input = sys.stdin.readline

def merge(node):
    seg[node] = seg[2*node] + seg[2*node + 1]

def build(node, start, end):
    if start == end:
        seg[node] = arr[start-1]
        return
    mid = (start + end) // 2
    build(2*node, start, mid)
    build(2*node + 1, mid + 1, end)
    merge(node)

def update(node, start, end, pos, val):
    if start == end:
        seg[node] += val
        return
    mid = (start + end) // 2
    if pos <= mid:
        update(2*node, start, mid, pos, val)
    else:
        update(2*node + 1, mid + 1, end, pos, val)
    merge(node)

def range_update(node, start, end, ql, qr, val): # ql and qr are inclusive
    if start > qr or end < ql:
        return
    if start == end:
        seg[node] += val
        return
    mid = (start + end) // 2
    range_update(2*node, start, mid, ql, qr, val)
    range_update(2*node + 1, mid + 1, end, ql, qr, val)
    merge(node)

def propagate(node, start, end):
    seg[node] += (end - start + 1) * lazy[node]
    if start != end:  
        lazy[2*node] += lazy[node]
        lazy[2*node + 1] += lazy[node]
    lazy[node] = 0

def range_update_lazy(node, start, end, ql, qr, val):  # ql and qr are inclusive
    if lazy[node] != 0:
        propagate(node, start, end)
    if start > qr or end < ql:
        return
    if start >= ql and end <= qr:
        seg[node] += (end - start + 1) * val
        if start != end:
            lazy[2*node] += val
            lazy[2*node + 1] += val
        return
    mid = (start + end) // 2
    range_update_lazy(2*node, start, mid, ql, qr, val)
    range_update_lazy(2*node + 1, mid + 1, end, ql, qr, val)
    merge(node)

def query(node, start, end, ql, qr): #ql and qr are inclusive
    if start > qr or end < ql:
        return 0
    if start >= ql and end <= qr:
        return seg[node]
    mid = (start + end) // 2
    left_st = query(2*node, start, mid, ql, qr)
    right_st = query(2*node + 1, mid + 1, end, ql, qr)
    return left_st + right_st

n, q = map(int, input().split())
arr = list(map(int, input().split()))
lazy = [0] * (4 * n)
seg = [0] * (4 * n)
build(1, 1, n)

for _ in range(q):
    k, l, r = map(int, input().split())
    if k == 1:
        update(1, 1, n, l, r)
    elif k == 2:
        print(query(1, 1, n, l, r))