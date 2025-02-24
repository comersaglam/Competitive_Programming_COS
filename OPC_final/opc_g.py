n,m = list(map(int, input().split()))
arr = [[-1 for i in range(n)] for j in range(m)]
#dp = [[0 for i in range(target+1)] for j in range(len(weights)+1)]
def copy_array(arr):
    newarr = [[-1 for i in range(n)] for j in range(m)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            newarr[i][j] = arr[i][j]
    return newarr

def check_possible(arr, i,j,val):
    x = True
    if val == 1: #kare
        x = x and arr[i][j-1] == -1
        x = x and arr[i][j] == -1
        x = x and arr[i][j+1] == -1
        x = x and arr[i-1][j-1] == -1
        x = x and arr[i-1][j] == -1
        x = x and arr[i-1][j+1] == -1
        x = x and arr[i+1][j-1] == -1
        x = x and arr[i+1][j] == -1
        x = x and arr[i+1][j+1] == -1
    elif val == 0: #karo
        x = x and arr[i][j] == -1
        x = x and arr[i][j+1] == -1
        x = x and arr[i][j-1] == -1
        x = x and arr[i+1][j] == -1
        x = x and arr[i-1][j] == -1
    return x
        
def fill1(arr,i,j):
    arr[i][j-1] = 1
    arr[i][j] = 1
    arr[i][j+1] = 1
    arr[i-1][j-1] = 1
    arr[i-1][j] = 1
    arr[i-1][j+1] = 1
    arr[i+1][j-1] = 1
    arr[i+1][j] = 1
    arr[i+1][j+1] = 1

def fill0(arr,i,j):
    arr[i][j] = 0
    arr[i][j+1] = 0
    arr[i][j-1] = 0
    arr[i+1][j] = 0
    arr[i-1][j] = 0

    
def rec(arr):
    ans = 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[i])-1):
            if check_possible(arr,i,j,1):
                newarr = copy_array(arr)
                fill1(newarr,i,j)
                ans += rec(newarr)
                ans += 1
            if check_possible(arr,i,j,0):
                newarr = copy_array(arr)
                fill0(newarr,i,j)
                ans += rec (newarr)
            else:
    if ans == 0:
        return 1
    return ans

if n<3 or m<3:
    print(1)
    exit()

num = rec(arr)
print(num+1)