N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

for r in range(N):
    for c in range(M):
        if grid[r][c] == 'i':
            start_r, start_c = r, c
            break

# Initialize prefix sums for 'a' and 'b'
prefix_a = [[0] * (M + 1) for _ in range(N + 1)]
prefix_b = [[0] * (M + 1) for _ in range(N + 1)]

# Compute prefix sums
for r in range(N):
    for c in range(M):
        prefix_a[r + 1][c + 1] = prefix_a[r + 1][c] + prefix_a[r][c + 1] - prefix_a[r][c] + (1 if grid[r][c] == 'a' else 0)
        prefix_b[r + 1][c + 1] = prefix_b[r + 1][c] + prefix_b[r][c + 1] - prefix_b[r][c] + (1 if grid[r][c] == 'b' else 0)

def get_sum(prefix, r1, c1, r2, c2):
    return prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]

max_diff = float('-inf')

# right down
for r in range(start_r, N):
    for c in range(start_c, M):
        num_a = get_sum(prefix_a, start_r, start_c, r + 1, c + 1)
        num_b = get_sum(prefix_b, start_r, start_c, r + 1, c + 1)
        max_diff = max(max_diff, num_a - num_b)

# left up
for r in range(start_r, -1, -1):
    for c in range(start_c, -1, -1):
        num_a = get_sum(prefix_a, r, c, start_r + 1, start_c + 1)
        num_b = get_sum(prefix_b, r, c, start_r + 1, start_c + 1)
        max_diff = max(max_diff, num_a - num_b)

# right up
for r in range(start_r, N):
    for c in range(start_c, -1, -1):
        num_a = get_sum(prefix_a, start_r, c, r + 1, start_c + 1)
        num_b = get_sum(prefix_b, start_r, c, r + 1, start_c + 1)
        max_diff = max(max_diff, num_a - num_b)

# left down
for r in range(start_r, -1, -1):
    for c in range(start_c, M):
        num_a = get_sum(prefix_a, r, start_c, start_r + 1, c + 1)
        num_b = get_sum(prefix_b, r, start_c, start_r + 1, c + 1)
        max_diff = max(max_diff, num_a - num_b)

print(max_diff)

