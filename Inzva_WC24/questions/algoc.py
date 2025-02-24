import heapq

def find_median(N, sequence):
    left_heap = []  # Max heap for the left half
    right_heap = []  # Min heap for the right half

    medians = []  # List to store medians after each number

    for i in range(N):
        num = sequence[i]

        # Add the number to the appropriate heap
        if not left_heap or num <= -left_heap[0]:
            heapq.heappush(left_heap, -num)
        else:
            heapq.heappush(right_heap, num)

        # Balance the heaps
        if len(left_heap) > len(right_heap) + 1:
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
        elif len(right_heap) > len(left_heap):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))

        # Calculate the median
        if i % 2 == 0:
            medians.append(-left_heap[0])
        else:
            medians.append((-left_heap[0] + right_heap[0]) // 2)

    return medians

# Input
N = int(input())
sequence = list(map(int, input().split()))

medians = find_median(N, sequence)

# Print the medians
for median in medians:
    print(median)
