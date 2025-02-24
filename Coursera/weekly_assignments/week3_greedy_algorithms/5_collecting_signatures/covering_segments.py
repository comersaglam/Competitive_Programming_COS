from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    segmentsleft = sorted(segments, key=lambda x: x[0])
    segmentsright = sorted(segments, key=lambda x: x[1])
    points += segmentsleft[0][1]
    for ind, seg in enumerate(segmentsright):
        if segmentsleft[0][1] >= seg[1]:
            segments.pop(segments.index(seg))
    if len(segments) <= 0:
        pass 
    else:
        points += optimal_points(segments)
        return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    print (segments)
    print(segments[0])
    print(type(segments[0]))#!different class
    points = optimal_points(segments)
    print(len(points))
    print(*points)
  