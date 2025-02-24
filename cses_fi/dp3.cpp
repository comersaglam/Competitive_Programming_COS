#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n >> x;

    vector<int> coins(n);
    for(int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    vector<int> dp(x + 1, 0);
    dp[0] = 1;
    int modulo = 1e9 + 7;

    for(int i = 1; i <= x; i++) {
        for(auto c : coins) {
            if(i >= c) {
                dp[i] = (dp[i] + dp[i - c]) % modulo;
            }
        }
    }

    cout << dp[x] % modulo;

    return 0;
}