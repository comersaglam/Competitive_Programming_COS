    #*
from sys import stdin


def min_refills(distance, tank, stops, refstop = 0):
    totalstop = 0
    for index, stopnum in enumerate(stops):
        if not stopnum - refstop <= tank:
            totalstop += 1
            if totalstop != 0:
                totalstop = totalstop + min_refills(distance , tank, stops[index:], stops[index-1])
                return totalstop
            else:
                return -1000
    return 0


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    stops.append(d)
    x = min_refills(d, m, stops)
    if x < 0:
        print(-1)
    else:
        print(x)
