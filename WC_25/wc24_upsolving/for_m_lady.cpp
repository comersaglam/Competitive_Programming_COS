#include <bits/stdc++.h>
#define int long long
int fact[10000002];
int sf[10000002];
using namespace std;
int fastpow(int base, int exp, int m)
{
    int result = 1 % m;
    base %= m;
    while (exp > 0)
    {
        if (exp & 1)
            result = (result * base) % m;
        base = (base * base) % m;
        exp >>= 1;
    }
    return result;
}
int inverse(int a, int MOD)
{
    int result = 1;
    int us = MOD - 2;
    while (us >= 1)
    {
        if (us % 2 == 1)
            result = (result * a) % MOD;
        a = (a * a) % MOD;
        us /= 2;
    }
    return result;
}

int findmaxnumberprime(int n, int p)
{   
    if(p == 0 ){
        return 0 ; 
    }
    int a = p;

    int result = 0;
    while (a <= n)
    {
        int x = n / a;
        int m = n % a;
        result= (result+(a * (x - 1) * x / 2 + x * (m + 1)));
        a *= p;
    }
    return (result);
}

int32_t main()
{
    
    fact[0] = 1;
    for (int i = 1; i <= 10000001; i++)
    {
        fact[i] = (fact[i - 1] * i) % 1000000007;
    }
    sf[0] = 1;
    for (int i = 1; i <= 10000001; i++)
    {
        sf[i] = (sf[i - 1] * fact[i]) % 1000000007;
    }

    vector<int> spf(10000002, 0);
    for (int i = 2; i * i <= 10000001; i++)
    {
        if (!spf[i])
        {
            for (int j = i * i; j <= 10000001; j += i)
            {
                if (!spf[j])
                    spf[j] = i;
            }
        }
    }

    for (int i = 2; i <= 10000001; i++)
    {
        if (!spf[i])
            spf[i] = i;
    }
    int temp;
    int divisor;
    int a;
    int n;
    cin >> n;
    int sampleX, sampleY, sampleZ;
    for (int i = 0; i < n; i++)
    {
        cin >> sampleX >> sampleY >> sampleZ;

        a = sampleZ;
        int pmax = 1;
        while (a > 1)
        {
            int p = spf[a];
            pmax = max(pmax, p);
            while (a % p == 0)
            {
                a /= p;
            }
        }

        int S = findmaxnumberprime(sampleY, pmax) - findmaxnumberprime(sampleX - 1, pmax);
        temp = (sf[sampleY] * inverse(sf[sampleX - 1], 1000000007)) % 1000000007;
        int inv = fastpow(sampleZ % 1000000007, S , 1000000007);
        // https://math.stackexchange.com/questions/4592623/finding-the-inverse-modulo-of-a-large-exponent-that-has-a-large-modulo
        temp = (temp * inverse(inv,1000000007)) % 1000000007;
        cout << temp << "\n";
    }
    return 0 ;
    
}