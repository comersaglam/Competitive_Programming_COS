#include <vector>
#include <queue>
#include <climits>

using namespace std;

typedef pair<int, int> Edge;
typedef vector<Edge> AdjacencyList;
typedef vector<AdjacencyList> Graph;

void dijkstra(Graph &graph, int start) {
    vector<int> distances(graph.size(), INT_MAX / 2);
    vector<bool> visited(graph.size(), false);
    distances[start] = 0;

    // The queue stores pairs of (distance, vertex)
    priority_queue<Edge, vector<Edge>, greater<Edge>> queue;
    queue.push({0, start});

    while (!queue.empty()) {
        int currentVertex = queue.top().second;
        int currentDistance = queue.top().first;
        queue.pop();

        // Skip this vertex if it has already been visited
        if (visited[currentVertex]) continue;
        visited[currentVertex] = true;

        // Iterate over all edges from the current vertex
        for (auto edge : graph[currentVertex]) {
            int nextVertex = edge.first;
            int weight = edge.second;

            // Relax the edge if possible
            if (distances[currentVertex] + weight < distances[nextVertex]) {
                distances[nextVertex] = distances[currentVertex] + weight;
                queue.push({distances[nextVertex], nextVertex});
            }
        }
    }
}