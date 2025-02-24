#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const long long INF = 1LL << 60;

long long dijkstra(int start, const vector<vector<pair<int, int>>>& graph,
                     int n, const vector<bool>& thetaMark) {
    vector<long long> distances(n + 1, INF);
    vector<bool> visited(n + 1, false);
    distances[start] = 0;

    priority_queue< pair<long long, int>,
                    vector<pair<long long, int>>,
                    greater<pair<long long, int>> > pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [currDistance, currNode] = pq.top();
        pq.pop();

        if (visited[currNode])
            continue;
        visited[currNode] = true;

        if (thetaMark[currNode]) {
            return distances[currNode];
        }

        for (const auto& edge : graph[currNode]) {
            int neighbor = edge.first;
            int weight = edge.second;
            if (distances[currNode] + weight < distances[neighbor]) {
                distances[neighbor] = distances[currNode] + weight;
                pq.push({distances[neighbor], neighbor});
            }
        }
    }

    return -1;
}

int main() {
    int N, E;
    scanf("%d %d", &N, &E);
    vector<vector<pair<int, int>>> graph_total(N + 1);
    for (int i = 0; i < E; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        graph_total[u].push_back({v, w});
        graph_total[v].push_back({u, w});
    }

    int t;
    scanf("%d", &t);
    vector<bool> thetaMark(N + 1, false);
    for (int i = 0; i < t; i++) {
        int node;
        scanf("%d", &node);
        thetaMark[node] = true;
    }

    int o;
    scanf("%d", &o);
    vector<bool> omegaMark(N + 1, false);
    vector<int> omegaNodes;
    for (int i = 0; i < o; i++) {
        int node;
        scanf("%d", &node);
        omegaMark[node] = true;
        omegaNodes.push_back(node);
    }

    vector<vector<pair<int, int>>> graph(N + 1);
    for (int u = 1; u <= N; u++) {
        for (const auto &edge : graph_total[u]) {
            int v = edge.first, w = edge.second;
            if (thetaMark[u] && thetaMark[v])
                continue;
            if (omegaMark[u] && omegaMark[v])
                continue;
            graph[u].push_back({v, w});
        }
    }

    long long maxShortest = -1;
    for (int start : omegaNodes) {
        long long distance = dijkstra(start, graph, N, thetaMark);
        if (distance > maxShortest)
            maxShortest = distance;
    }

    printf("%lld\n", maxShortest);
    return 0;
}
