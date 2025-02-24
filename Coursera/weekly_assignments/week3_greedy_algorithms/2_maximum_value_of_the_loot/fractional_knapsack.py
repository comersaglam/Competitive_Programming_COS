    #*
from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    elementdict = {}
    for element in range(len(weights)):
        elementdict[(values[element]/weights[element])] = [weights[element], values[element]]
    elementdict = dict(sorted(elementdict.items(), reverse=True))
    for perkg in elementdict:
        if capacity >= elementdict[perkg][0]:
            capacity -= elementdict[perkg][0]
            value += elementdict[perkg][1]
        else:
            if capacity > 0:
                value += perkg*capacity
                capacity = 0
            else:
                break

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
