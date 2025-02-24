def find_min_jumps(routes, start, finish):
    if start >= finish:
        return 0

    routes.sort(key=lambda x: x[0])
    jumps = 0
    current_reach = start

    while current_reach < finish:
        max_reach = -1
        while routes and routes[0][0] <= current_reach:
            start_point, end_point = routes.pop(0)
            if end_point > max_reach:
                max_reach = end_point

        if max_reach <= current_reach:
            return -1 

        current_reach = max_reach
        jumps += 1

    return jumps

def main():
    N, K = map(int, input().split())
    routes = [list(map(int, input().split())) for _ in range(K)]

    result = find_min_jumps(routes, 1, N)
    print(result)

if __name__ == "__main__":
    main()
