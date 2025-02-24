n = int(input())
chars = list(input())

net_charge_freq = {0: 1}
net_charge = 0
result = 0

for char in chars:
    if char == "p":
        net_charge += 1
    elif char == "e":
        net_charge -= 1
    net_charge_freq[net_charge] = net_charge_freq.get(net_charge, 0) + 1

for freq in net_charge_freq.values():
    result += freq * (freq - 1) // 2 
print(result)
