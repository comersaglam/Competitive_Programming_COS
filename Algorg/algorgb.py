months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

def calc_deadline(n):

    weekday = 6
    week = n % 7
    weekday += week % 7

    today = [10, 3, 2024]
    year = n // 1461
    remain = n % 1461
    while remain > 0:
        if today[1] == 2 and today[2] % 4 == 0:
            if remain >= 29:
                remain -= 29
                today[1] += 1
            else:
                break
        else:
            if remain >= months[today[1]]:
                remain -= months[today[1]]
                today[1] += 1
            else:
                break
        if today[1] > 12:
            today[1] = 1
            today[2] += 1
    today[2] += year * 4
    today[0] += remain
    if today[1] == 2 and today[2] % 4 == 0:
        if today[0] > 29:
            today[0] -= 29
            today[1] += 1
    else:
        if today[0] > months[today[1]]:
            today[0] -= months[today[1]]
            today[1] += 1
    if today[1] > 12:
        today[1] = 1
        today[2] += 1
    today.append(weekday % 7)
    return today

def print_date(today):
    print(f"{today[0]:02d}.{today[1]:02d}.{today[2]} {days[today[3]]}")

t = int(input())

for _ in range(t):
    n = int(input())
    result = calc_deadline(n)
    print_date(result)