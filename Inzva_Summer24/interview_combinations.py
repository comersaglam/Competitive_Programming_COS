n , target = map(int,input().split())
candidates = list(map(int,input().split()))
candidates.sort()
for c in candidates:
    if candidates.count(c)>1:
        exit()
result = list()
def solve(arr,target,path):
    if target<0:
        return
    if target==0:
        result.append(path)
        return
    for i in range(len(arr)):
        solve(arr[i:],target-arr[i],path+[arr[i]])
solve(candidates,target,[])
for r in result:
    print(*r)
if not result:
    print(-1)

#* 2
#* 2 2
#* 2 2 2 
#! 2 2 2 2 NO
#? 2 2 2 3 NO
#^ 2 2 2 5 NO

#* 2 2 AGAIN
#! 2 2 3 SOLUTİON
#? 2 2 5 NO

#* 2 3
#! 2 3 3 NO
#? 2 3 5 NO