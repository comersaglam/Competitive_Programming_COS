l, n, k =map(int,input().split())
dist = list(map(int,input().split()))
inter = []
for i in range(len(dist) -1):
    inter.append(dist[i+1] - dist[i])

inter.sort()

nums = [0] * k

curr_dist = 0
#finds index that x is smaller than that. 1 2 3 4 5 LİST and ind
def find_ind(inter, x, start): #binary search e değiştir
    for i in range(start, len(inter)):
        if inter[i] > x:
            return x

res_sum = 0
ind = -1
while res_sum < k:
    ind += 1
    find_ind(inter, i, start)
    nums[i] += 




