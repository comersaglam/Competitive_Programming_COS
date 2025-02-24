def isprime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

n, m = map(int, input().strip().split(" "))
berat = 0
sura = list(map(int,input().split()))
lensura = len(sura)
maxage = max(sura) + m



for age in sura:
    for range_ in range(age, age+m+1):
        if isprime(range_):
            berat += 1
            lensura -= 1
            break
if berat <= lensura:
    print("Sura")
    print(lensura)
else:
    print("Berat")
    print(berat)