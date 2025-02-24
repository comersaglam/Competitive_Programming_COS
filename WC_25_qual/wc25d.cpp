#include <iostream>
#include <vector>
using namespace std;

vector<int> sum_vectors(vector<int> v1, const vector<int>& v2) {
    for (size_t i = 0; i < v1.size(); ++i) {
        v1[i] += v2[i];
    }
    return v1;
}

int main() {
    int n, d;
    cin >> n >> d;

    vector<vector<int>> vectors(n, vector<int>(d));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < d; ++j) {
            cin >> vectors[i][j];
        }
    }

    vector<int> target(d);
    for (int i = 0; i < d; ++i) {
        cin >> target[i];
    }

    bool is_possible = false;

    for (int i = 0; i < (1 << n); ++i) {
        vector<int> subset_sum(d, 0);
        for (int j = 0; j < n; ++j) {
            if (i & (1 << j)) { 
                subset_sum = sum_vectors(subset_sum, vectors[j]);
            }
        }
        if (subset_sum == target) {
            is_possible = true;
            break;
        }
    }

    if (is_possible) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
