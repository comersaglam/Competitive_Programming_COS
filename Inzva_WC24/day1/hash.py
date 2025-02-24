 #! STR HASH
#* str boyutları büyük
#* str leri integera çeviriyoruz
#* lineer hashing yapacğız(çok fazla yöntem var)

#^ harflerin konumlarının basamak değeri olsun. abcd p^3, p^2, p^1, p^0 ve her harfin bir değeri olsun a=1, b=2, c=3, d=4
#^ sonuç p^4 + 2p^3 + 3p^2 + 4p + 5. tersine çevirirken de her turda p ye bölüp kalanı yazarız o basamağa. Geri döndürülebilir HASH fonksiyonu
#^ p>=27 olmalı ki basamak toplamları tek anlama gelsin
#^ p 27 iken 100 harfli bir str 27^100 olur ve bu saklanabilecek bir boyut değil(2^64 max)
#^ büyük bir sayıyla(asal zorunlu değil) modunu alarak saklayacağım. bu sayıya m diyelim
#^ çakışma ihtimali için p1 m1 ile hashlemenin yanısıra p2 m2 ile de eşleyerek ihtimal çok düşürülebilir.


#? n uzunluğundaki bir str nin k uzunluklu substr lerini bir gezmede hashleyelim

def fp(a,b, modulo = 10**9 +7):
    if b== 0: return 1
    if b%2 == 1: return a*fp(a,b-1)%modulo
    else:
        half = fp(a,b/2)
        return half*half %modulo

n, k = list(map(int,input("n,k ").split()))
s = input("str ")
p = 29
modulo = 10**9 + 7
hashset = set()
hashdict = {"a":1, "b":2, "c":3, "d":4}

for i in range(k):
    myhash = (fp(p, i) * hashdict[s[k-i-1]]) % modulo
    hashset.add(myhash)
#first k long str hash
    
for i in range(n-k):
    #s[i]#ilk elemnti çıkar
    myhash -= fp(p, k-1) * hashdict[s[i]] % modulo
    myhash = myhash*p % modulo
    #s[i+k]#yeni elementi ekle
    myhash += hashdict[s[i+k-1]]% modulo
    hashset.add(hashset)

print(len(myhash))
####################!