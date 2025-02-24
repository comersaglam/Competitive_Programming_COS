letters = "abcdefghijklmnopqrstuvwxyz"
prime = 29
MOD = 1000000007
dp = [1] * 26
for i in range(1, 26):
    dp[i] = (dp[i-1] * prime) % MOD
valOfLetters = {letters[i]: dp[i] for i in range(26)}

def hash(strng):
    h = 0
    for c in strng:
        h += valOfLetters[c]
        h %= MOD
    return h

l, s =map(int, input().split())
long = input()
short = input()
hashShort = hash(short)
hashLong = 0
for i in range(s):
    hashLong += valOfLetters[long[i]]
    hashLong %= MOD

anagram_index = []
for i in range(l-s+1):
    if hashLong == hashShort:
        anagram_index.append(i)
    if i < l-s:
        hashLong = (hashLong - valOfLetters[long[i]] + valOfLetters[long[i+s]])%MOD

print(*anagram_index) if anagram_index else print(-1) # -1 