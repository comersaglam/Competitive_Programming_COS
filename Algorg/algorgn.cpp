#include <iostream>
#include <cmath>

const long long MOD = 1e9 + 7;

long long pow_mod(long long base, long long exp) {
    long long result = 1;
    while (exp) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

long long fib(long long n) {
    double A = (1 + sqrt(5)) / 2;
    double B = (1 - sqrt(5)) / 2;
    double fib = (std::pow(A, n) - std::pow(B, n)) / sqrt(5);
    return (long long)(fib + 0.5);
}

long long count_combinations(long long n) {
    return fib(n) % MOD;
}

int main() {
    int t;
    std::cin >> t;
    while (t--) {
        long long n;
        std::cin >> n;
        std::cout << (count_combinations(n + 2) - 1 + MOD) % MOD << "\n";
    }
    return 0;
}