def maximizeproduct(numlist):
    max1 = 0
    max2 = 0
    for j in numlist:
        if j >= max2:
            if j>= max1:
                max2 = max1
                max1 = j
            else:
                max2 = j
    return max1*max2 


def main():
    inputnum = int(input())
    numbers = list(map(int, input().split()))
    print(maximizeproduct(numbers))
    
if __name__=="__main__":
    main()