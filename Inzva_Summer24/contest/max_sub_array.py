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
        seg[node] = val
        return
    mid = (start + end) // 2
    if pos <= mid:
        update(2*node, start, mid, pos, val)
    else:
        update(2*node + 1, mid + 1, end, pos, val)
    merge(node)

# her node 3 değer döndürecek. complete version, sağdan kesik versiyon, soldan kesik versiyon. bi de o nodun max ı
def query(node, start, end): #this is the building logic
    if start == end:
        return 0,0,seg[node], max(seg[node],0)
    else:
        mid = (start+end)//2
        lleft, lright, lcomplete,lm = query(2*node, start,mid)
        rleft, rright, rcomplete,rm = query(2*node+1, mid+1, end)
# 4 değer hesaplayacağız. sadece soldan kesik. sadece sağdan kesik, complete, solitary
    solk = max(lleft + rcomplete, rcomplete, rleft)
    sagk = max(lcomplete + rright, lcomplete, lright)
    tum = lcomplete + rcomplete
    solo = max(lleft + rright, lleft, rright)
    maxnode = max(solo, tum, sagk, solk, lm, rm)
    return (solk, sagk, tum, maxnode)

n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))
seg = [0] * (4 * n)
build(1, 1, n)

for i in range(q):
    i ,val = list(map(int, input().split()))
    update(1,1,n, i, val)
    x = query(1,1,n)
    print(max(x))
