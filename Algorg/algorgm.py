import math

X1, Y1, R1 = map(int, input().split())
X2, Y2, R2 = map(int, input().split())

def intersection_area(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if d >= r1 + r2: return 0
    elif d <= abs(r1 - r2) and r1 >= r2: return math.pi * (r2 ** 2)
    elif d <= abs(r1 - r2) and r2 >= r1: return math.pi * (r1 ** 2)
    else:
        theta1 = math.acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1))
        theta2 = math.acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2))

        area1, area2 = r1 ** 2 * theta1, r2 ** 2 * theta2

        chord_length = (1 / 2) * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
        intersection_area = area1 + area2 - chord_length

        return intersection_area

answer = math.pi * (R1 ** 2) + math.pi * (R2 ** 2) - intersection_area(X1, Y1, R1, X2, Y2, R2)

print("%.2f" % answer)
