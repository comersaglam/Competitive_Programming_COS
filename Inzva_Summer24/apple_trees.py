import sys
input = sys.stdin.readline

def merge(node):
    seg[node] = max(seg[2*node], seg[2*node + 1])

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
        seg[node] -= val
        return
    mid = (start + end) // 2
    if pos <= mid:
        update(2*node, start, mid, pos, val)
    else:
        update(2*node + 1, mid + 1, end, pos, val)
    merge(node)

def search(node, start, end, val):
    if start == end:
        return start if seg[node] >= val else None
    mid = (start + end) // 2
    if seg[2*node] >= val:
        return search(2*node, start, mid, val)
    else:
        return search(2*node + 1, mid + 1, end, val)

n, c = map(int, input().split())
arr = list(map(int, input().split()))
seg = [0] * (4 * n)
build(1, 1, n)

childs = list(map(int, input().split()))

for c in childs:
    tree = search(1, 1, n, c)
    if tree is None:
        print(0, end=' ')
    else:
        print(tree, end=' ')
        update(1, 1, n, tree, c)