    #*
def binary_search(keys, query):
    n = len(keys)
    if n ==0:
        return -1
    leftside = keys[0:(n//2)]
    midside = keys[n//2]
    rightside = keys[(n//2)+1:]
    if query ==midside:
        return n//2
    elif query < midside:
        return binary_search(leftside,query)
    else:
        r = binary_search(rightside,query)
        if r == -1:
            return -1
        else:
            return n//2 + r



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
