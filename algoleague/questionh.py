a, b = map(int, input().strip().split(" "))
arraya = list(map(int,input().split()))
arrayb = list(map(int,input().split()))
commons = set()
commons = set(arraya).intersection(set(arrayb))
maxa = []
maxb = []
partialtotal = 0
for a in arraya:
    partialtotal += a
    if a in commons:
        maxa.append(partialtotal)
        partialtotal = 0
maxa.append(partialtotal)
partialtotal = 0
for b in arrayb:
    partialtotal += b
    if b in commons:
        maxb.append(partialtotal)
        partialtotal = 0
maxb.append(partialtotal)

sum_of_larger_elements = sum(max(pair) for pair in zip(maxa, maxb))
print(sum_of_larger_elements % (10**9 + 7))