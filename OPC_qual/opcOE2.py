S1 = input().strip()
S2 = input().strip()

def can_assign(M):
    positions = []

    min_nums_S1 = []
    prev_num = None
    for i in range(len(S1)):
        c = S1[i]
        if c == 'O':
            if prev_num is None:
                min_num = 1
            else:
                min_num = prev_num + 1
                if min_num % 2 == 0:
                    min_num += 1
            prev_num = min_num
        elif c == 'E':
            if prev_num is None:
                min_num = 2
            else:
                min_num = prev_num + 1
                if min_num % 2 != 0:
                    min_num += 1
            prev_num = min_num
        min_nums_S1.append((min_num, c))
        positions.append((min_num, c))

    min_nums_S2 = []
    prev_num = None
    for i in range(len(S2)):
        c = S2[i]
        if c == 'O':
            if prev_num is None:
                min_num = 1
            else:
                min_num = prev_num + 1
                if min_num % 2 == 0:
                    min_num += 1
            prev_num = min_num
        elif c == 'E':
            if prev_num is None:
                min_num = 2
            else:
                min_num = prev_num + 1
                if min_num % 2 != 0:
                    min_num += 1
            prev_num = min_num
        min_nums_S2.append((min_num, c))
        positions.append((min_num, c))

    positions.sort()

    used_numbers = set()
    current_odd = 1
    current_even = 2

    for min_num_p, c in positions:
        if c == 'O':
            current = max(current_odd, min_num_p)
            if current % 2 == 0:
                current += 1
            while current in used_numbers and current <= M:
                current += 2
            if current > M:
                return False
            used_numbers.add(current)
            current_odd = current + 2
        elif c == 'E':
            current = max(current_even, min_num_p)
            if current % 2 != 0:
                current += 1
            while current in used_numbers and current <= M:
                current += 2
            if current > M:
                return False
            used_numbers.add(current)
            current_even = current + 2
    return True

left = 1
right = 2 * (len(S1) + len(S2)) + 10

while left < right:
    mid = (left + right) // 2
    if can_assign(mid):
        right = mid
    else:
        left = mid + 1

print(left)
