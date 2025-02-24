 #*!
from math import sqrt

def mo_algorithm(arr, queries):
    n = len(arr)
    block_size = int(sqrt(n)) + 1
    answers = [0] * len(queries)
    
    # Sort queries by block and then by R value
    queries.sort(key=lambda x: (x[0] // block_size, x[1]))
    
    freq = [0] * (max(arr) + 1)
    distinct = 0
    currentL, currentR = 0, -1
    
    for i, (L, R) in enumerate(queries):
        # Expand to the right
        while currentR < R:
            currentR += 1
            freq[arr[currentR]] += 1
            if freq[arr[currentR]] == 1:
                distinct += 1
        
        # Contract from the right
        while currentR > R:
            freq[arr[currentR]] -= 1
            if freq[arr[currentR]] == 0:
                distinct -= 1
            currentR -= 1
        
        # Expand to the left
        while currentL < L:
            freq[arr[currentL]] -= 1
            if freq[arr[currentL]] == 0:
                distinct -= 1
            currentL += 1
        
        # Contract from the left
        while currentL > L:
            currentL -= 1
            freq[arr[currentL]] += 1
            if freq[arr[currentL]] == 1:
                distinct += 1
        
        answers[i] = distinct
    
    return answers

# Example usage
arr = [1, 2, 1, 3, 4, 3, 3, 4]
queries = [(0, 4), (1, 3), (2, 5)]  # Queries are 0-indexed
answers = mo_algorithm(arr, queries)
for ans in answers:
    print(ans)