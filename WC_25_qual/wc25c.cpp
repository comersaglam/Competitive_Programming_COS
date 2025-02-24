#include <iostream>
using namespace std;

const int MOD = 1000000007;

inline long long fexp(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b % 2 == 1) {
            res = (res * a) % MOD;
        }
        a = (a * a) % MOD;
        b /= 2;
    }
    return res;
}

inline long long mod_inv(long long a) {
    return fexp(a, MOD - 2);
}

int main() {
    const long long n = 93623149;
    long long k;
    cin >> k;
    k += 1;
    k = min(k, n - k);
    long long res = 1;

    for (long long i = 0; i < k; ++i) {
        res = (res * (n - i) % MOD) * mod_inv(i + 1) % MOD; 
    }

    cout << res << endl;

    return 0;
}
