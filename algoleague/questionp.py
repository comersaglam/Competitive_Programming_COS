from collections import defaultdict

MOD = 10**9 + 7

def add_edge(graph, u, v):
    graph[u].add(v)  # Using a set for edges

def iterative_dfs(graph, start, end):
    stack = [(start, 1, set([start]))]  # (node, path_length, visited_set)
    total_path_length = 0

    while stack:
        node, path_length, visited = stack.pop()

        if node == end:
            total_path_length += path_length
            total_path_length %= MOD
            continue

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_visited = visited.copy()
                new_visited.add(neighbor)
                stack.append((neighbor, path_length + 1, new_visited))

    return total_path_length

def find_all_paths_and_lengths(edges, start, end):
    graph = defaultdict(set)  # Changed to defaultdict of sets
    for u, v in edges:
        add_edge(graph, u, v)

    total_path_length = iterative_dfs(graph, start, end)
    return total_path_length

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    total_path_length = find_all_paths_and_lengths(edges, 1, n)
    print(total_path_length % MOD)

if __name__ == "__main__":
    main()




#include <iostream>
#include <vector>

const int MAX_LEVELS = 100000; 

void explorePaths(int current, int dest, std::vector<int> graph[], 
                  std::vector<bool>& visited, int pathLength, int& totalLength) {
    if (visited[current]) return;

    pathLength++; 

    if (current == dest) {
        totalLength += pathLength; 
    } else {
        visited[current] = true;
        for (int next : graph[current]) {
            explorePaths(next, dest, graph, visited, pathLength, totalLength);
        }
        visited[current] = false;
    }
}

int main() {
    int n, m;
    std::cin >> n >> m;
    std::vector<int> graph[MAX_LEVELS];
    std::vector<bool> visited(MAX_LEVELS, false);

    for (int i = 0; i < m; ++i) {
        int u, v;
        std::cin >> u >> v;
        graph[u - 1].push_back(v - 1);  
    }

    int totalLength = 0;
    explorePaths(0, n - 1, graph, visited, 0, totalLength);

    std::cout << totalLength << std::endl;  

    return 0;
}
