#include <iostream>
#include <vector>
using namespace std;

long long fexp(long long base, long long exp, long long p) {
    long long result = 1;
    while (exp > 0) {
        if (exp & 1)
            result = (result * base) % p;
        exp = exp >> 1;
        base = (base * base) % p;
    }
    return result;
}

pair<vector<long long>, vector<bool>> sieve(long long limit) {
    vector<long long> primes(limit + 1, 0);
    vector<bool> squares(limit + 1, false);

    for (long long p = 2; p <= limit; ++p) {
        if (primes[p] == 0) {
            for (long long i = p; i <= limit; i += p)
                primes[i] += 1;

            if (p * p <= limit) {
                for (long long i = p * p; i <= limit; i += p * p)
                    squares[i] = true;
            }
        }
    }
    return make_pair(primes, squares);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, p, a, lee;
    cin >> n;
    cin >> p >> a;
    cin >> lee;

    auto result = sieve(n);
    auto& primes = result.first;
    auto& squares = result.second;

    long long zombies = 1;

    for (long long i = 2; i <= n; ++i) {
        if (!squares[i]) {
            long long us = primes[i];
            long long agg = fexp(a, us, p);
            if (agg > p / 2)
                agg -= p;
            if (us % 2 != 0)
                zombies -= agg;
            else
                zombies += agg;
        }
    }

    if (zombies >= lee)
        cout << "Lee needs a better plan!" << endl;
    else
        cout << "Lee will kill them all!" << endl;

    return 0;
}
