    #*
def optimal_summands(n):
    summands = []
    for i in range(int((n**(1/2))*1.2), int(((n**(1/2))*1.7))+1):
        trinum = int(i*(i+1)/2)
        if trinum >= n:
            if trinum == n:
                for j in range(1,i+1):
                    summands.append(j)
            else:
                for j in range(1, i-1):
                    summands.append(j)
                summands.append(i-1 + (i + n-trinum))

            break
        
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
