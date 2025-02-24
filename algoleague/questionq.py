import math

def calculate_variance(lst):
    if len(lst) == 0:
        return 0
    mean = math.fsum(lst) / len(lst)
    squared_diffs = [(x - mean) ** 2 for x in lst]
    variance = math.fsum(squared_diffs) / len(lst)

    return variance

n, q = map(int, input().strip().split(" "))
query = list(map(int,input().split()))
for i in range(q):
    command = list(map(int,input().split()))
    if command[0] == 2:
        print(int(calculate_variance(query[command[1]-1:command[2]])))
    else:
        query[command[1]-1] = command[2]


import math

class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.tree = [0] * (4 * self.n)
        self.squared_tree = [0] * (4 * self.n)  # To store squares of elements
        self.build(array, 0, 0, self.n - 1)

    def build(self, array, v, tl, tr):
        if tl == tr:
            self.tree[v] = array[tl]
            self.squared_tree[v] = array[tl] ** 2
        else:
            tm = (tl + tr) // 2
            self.build(array, v * 2 + 1, tl, tm)
            self.build(array, v * 2 + 2, tm + 1, tr)
            self.tree[v] = self.tree[v * 2 + 1] + self.tree[v * 2 + 2]
            self.squared_tree[v] = self.squared_tree[v * 2 + 1] + self.squared_tree[v * 2 + 2]

    def update(self, index, value, v, tl, tr):
        if tl == tr:
            self.tree[v] = value
            self.squared_tree[v] = value ** 2
        else:
            tm = (tl + tr) // 2
            if index <= tm:
                self.update(index, value, v * 2 + 1, tl, tm)
            else:
                self.update(index, value, v * 2 + 2, tm + 1, tr)
            self.tree[v] = self.tree[v * 2 + 1] + self.tree[v * 2 + 2]
            self.squared_tree[v] = self.squared_tree[v * 2 + 1] + self.squared_tree[v * 2 + 2]

    def query(self, left, right, v, tl, tr):
        if left > right:
            return (0, 0)
        if left == tl and right == tr:
            return (self.tree[v], self.squared_tree[v])
        tm = (tl + tr) // 2
        left_sum, left_squared_sum = self.query(left, min(right, tm), v * 2 + 1, tl, tm)
        right_sum, right_squared_sum = self.query(max(left, tm + 1), right, v * 2 + 2, tm + 1, tr)
        return (left_sum + right_sum, left_squared_sum + right_squared_sum)

def calculate_variance(sum_, squared_sum, length):
    if length == 0:
        return 0
    mean = sum_ / length
    variance = (squared_sum / length) - mean ** 2
    return variance

# Main function
def main():
    N, Q = map(int, input().split())
    array = list(map(int, input().split()))

    # Initialize Segment Tree
    seg_tree = SegmentTree(array)

    # Process queries
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            # Update operation
            seg_tree.update(query[1] - 1, query[2], 0, 0, N - 1)
        elif query[0] == 2:
            # Variance calculation
            left, right = query[1] - 1, query[2] - 1
            sum_, squared_sum = seg_tree.query(left, right, 0, 0, N - 1)
            var = calculate_variance(sum_, squared_sum, right - left + 1)
            print(int(var))

if __name__ == "__main__":
    main()
