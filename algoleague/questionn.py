import sys
import heapq

def dijkstra_modified(graph, N):
    distance_odd = [float('inf')] * (N + 1)
    distance_even = [float('inf')] * (N + 1)
    distance_odd[1] = 0

    to_process = [(0, 1, True)]
    heapq.heapify(to_process)

    while to_process:
        current_dist, current_node, is_odd = heapq.heappop(to_process)

        if current_node == N:
            return current_dist

        for next_node, edge_cost in graph[current_node]:
            if is_odd:
                new_cost = current_dist + edge_cost * 2
                if new_cost < distance_even[next_node]:
                    distance_even[next_node] = new_cost
                    heapq.heappush(to_process, (new_cost, next_node, False))
            else:
                new_cost = current_dist + edge_cost // 2
                if new_cost < distance_odd[next_node]:
                    distance_odd[next_node] = new_cost
                    heapq.heappush(to_process, (new_cost, next_node, True))

    return min(distance_odd[N], distance_even[N])

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    edge_inputs = [tuple(map(int, input().split())) for _ in range(M)]

    graph = [[] for _ in range(N + 1)]
    for u, v, w in edge_inputs:
        graph[u].append((v, w))
        graph[v].append((u, w))

    result = dijkstra_modified(graph, N)
    print(result)

if __name__ == "__main__":
    main()
