#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>
#include <cstdio>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    scanf("%d %d", &n, &m);

    vector<string> grid(n);
    for (int i = 0; i < n; ++i) {
        char buffer[n + 1];
        scanf("%s", buffer);
        grid[i] = buffer;
    }

    vector<pair<int, int>> coordinates(m);
    for (int i = 0; i < m; ++i) {
        scanf("%d %d", &coordinates[i].first, &coordinates[i].second);
    }

    int query;
    scanf("%d", &query);

    vector<vector<int>> min_m_grid_id(n, vector<int>(n, INT_MAX));
    vector<vector<int>> min_m_grid_dist(n, vector<int>(n, INT_MAX));
    vector<vector<int>> max_m_grid_id(n, vector<int>(n, INT_MIN));
    vector<vector<int>> max_m_grid_dist(n, vector<int>(n, INT_MIN));

    vector<vector<bool>> visited(n, vector<bool>(n, false));
    queue<tuple<int, int, int>> q;

    for (int index = 0; index < m; ++index) {
        int x = coordinates[index].first;
        int y = coordinates[index].second;
        int instrument_id = index + 1;

        q.push({x, y, 0});
        visited.assign(n, vector<bool>(n, false));
        visited[x][y] = true;

        if (min_m_grid_dist[x][y] > 0) {
            min_m_grid_id[x][y] = instrument_id;
            min_m_grid_dist[x][y] = 0;
        }
        if (max_m_grid_dist[x][y] < 0) {
            max_m_grid_id[x][y] = instrument_id;
            max_m_grid_dist[x][y] = 0;
        }

        while (!q.empty()) {
            auto [cx, cy, d] = q.front();
            q.pop();

            for (auto [dx, dy] : vector<pair<int, int>>{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
                int nx = cx + dx;
                int ny = cy + dy;

                if (nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] == '.' && !visited[nx][ny]) {
                    visited[nx][ny] = true;

                    if (min_m_grid_dist[nx][ny] > d + 1) {
                        min_m_grid_id[nx][ny] = instrument_id;
                        min_m_grid_dist[nx][ny] = d + 1;
                    }
                    if (max_m_grid_dist[nx][ny] < d + 1) {
                        max_m_grid_id[nx][ny] = instrument_id;
                        max_m_grid_dist[nx][ny] = d + 1;
                    }

                    q.push({nx, ny, d + 1});
                }
            }
        }
    }

    for (int i = 0; i < query; ++i) {
        int x, y;
        scanf("%d %d", &x, &y);

        if (min_m_grid_id[x][y] == INT_MAX) {
            printf("-1 -1\n");
        } else {
            printf("%d %d\n", min_m_grid_id[x][y], max_m_grid_id[x][y]);
        }
    }

    return 0;
}
