l, n, k =map(int,input().split())
d=set(map(int,input().split()))
vis=set(d)
ans=[]
c=0
while (len(ans)<k):
    new=set()
    for i in d:
        ans.append(c)
        if 0<=i+1<=l and (i+1 not in vis):
            vis.add(i+1)
            new.add(i+1)
        if 0<=i-1<=l and (i-1 not in vis):
            vis.add(i-1)
            new.add(i-1)
    d=new
    c+=1
for i in range(k):
    print(ans[i])