#include <bits/stdc++.h>
using namespace std;
// #define ll long long
// #define int long long

// const int MAX = 2e5;
// const int MOD = 1e9+7;
// const int INF = 1e18;

int n, m, v;

signed main() {
    // ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    cin >> n >> m;
    int ans=0;
    for (int i=0;i<=n;++i) {
        for (int j=0;j<=m;++j) {
            if (i+j==0) {
                continue;
            }
            if (i==0) {
                ans += n/j;
            } else if (j==0) {
                ans += m/i;
            } else {
                v=min((n-i)/j, (m-j)/i);
                if (v) {
                    ans += 2*v-1;
                }
            }
        }
    }
    cout << ans-(min(n,m));
}