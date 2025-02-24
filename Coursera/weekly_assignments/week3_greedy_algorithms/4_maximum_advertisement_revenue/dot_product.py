    #*
from itertools import permutations


def max_dot_product(prices, clicks):
    max_product = 0
    prices.sort()
    clicks.sort()
    for i in range(n):
        max_product += prices[i] * clicks[i]

    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
