#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

#define endl '\n'
#define INF __LONG_LONG_MAX__
using namespace std;


int32_t main() {
    fastio
    int n, k;
    cin >> n >> k;
    long long  ans = (n-1) * (k-1) + 1;
    cout << ans << "\n";
    
    return 0;
}