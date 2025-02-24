n,d = list(map(int, input().split()))
vectors = []
for i in range(n):
    vectors.append(tuple(map(int, input().split())))

target = tuple(map(int, input().split()))

def sum_vectors(v1, v2):
    for i in range(len(v1)):
        v1[i] += v2[i]
    return v1

is_possible = False
for i in range(2**n):
    subset_sum = [0] * d
    for j in range(n):
        if (i & (1 << j)) != 0:
            subset_sum = sum_vectors(subset_sum, vectors[j])
    if tuple(subset_sum) == target:
        is_possible = True
        break

if is_possible:
    print("YES")
else:
    print("NO")

