# Always good to prepare solutions with various languages (namely C++ & Python)!
# Helps adjusting constraints properly. For instance, if they are too large for Python, lower them.
import sys
from collections import deque
import heapq

# Read inputs from the file
#input_file_path = sys.argv[1]
#with open(input_file_path, 'r') as file:
#    lines = file.readlines()
with open('./input/input_24.txt', 'r') as file:
    lines = file.readlines()
N, S1, S2, H, T, C = list(map(int, lines[0].split()))
matrix = [[] for _ in range(2*N+3)]
for i in range(1, S1+1):
    u, v, w = map(int, lines[i].split())
    matrix[u].append((v, w))
    matrix[v].append((u, w))

"""
N, S1, S2, H, T, C = list(map(int, input().split()))
matrix = [[] for _ in range(2*N+1)]
for i in range(S1):
    u,v,w = map(int, input().split())
    matrix[u].append((v, w))
    matrix[v].append((u, w))"""

def bfs(start, graph):
    distances = {}
    queue = deque([start])
    distances[start] = 0
    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        for neighbor, _ in graph[node]:
            if neighbor not in distances:
                distance = current_distance + 1
                distances[neighbor] = distance
                queue.append(neighbor)
    for node, distance in distances.items():
        graph[node].append((node+N, C * distance))
        graph[node+N].append((node, C * distance))
bfs(H, matrix)
# Parse the next S2 lines of inputs
for i in range(S1+1, S1+S2+1):
    u, v, w = map(int, lines[i].split())
    matrix[u+N].append((v+N, w))
    matrix[v+N].append((u+N, w))
   
"""for i in range(S2):
    u,v,w = map(int, input().split())
    matrix[u+N].append((v+N, w))
    matrix[v+N].append((u+N, w))"""


def dijkstra(start, graph, n):
    distances = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    distances[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        if visited[curr_node]:
            continue
        visited[curr_node] = True
        for neighbor, weight in graph[curr_node]:
            if distances[curr_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[curr_node] + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))
    return distances

distances = dijkstra(H, matrix, 2*N)
output = min(distances[T], distances[T+N])
if output == float('inf'):
    output = -1
print(output)


