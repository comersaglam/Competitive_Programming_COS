n, k = list(map(int, input().split()))
stocks = list(map(int, input().split()))

prefixdmi = [0] * (n)
for i in range(1, n):
    prefixdmi[i] = stocks[i] - stocks[i-1]

def calc_dmi(loss,gain):
    if gain + loss == 0:
        return 0
    dmi = (100*gain)/(loss + gain)
    return dmi

loss = 0
gain = 0

for i in range(1, k):
    if prefixdmi[i] > 0:
        gain += prefixdmi[i]
    else:
        loss -= prefixdmi[i]
dmi = calc_dmi(loss, gain)

if dmi < 35: signal = 1
elif dmi > 65: signal = 2
else: signal = 0

print("{:.1f}".format(dmi) , signal)


for i in range(2, n-k+2):
    if prefixdmi[i-1] > 0:
        gain -= prefixdmi[i-1]
    else:
        loss += prefixdmi[i-1]
    if prefixdmi[i+k-2] > 0:
        gain += prefixdmi[i+k-2]
    else:
        loss -= prefixdmi[i+k-2]
    dmi = calc_dmi(loss, gain)

    if dmi < 35: signal = 1
    elif dmi > 65: signal = 2
    else: signal = 0

    print("{:.1f}".format(dmi), signal)