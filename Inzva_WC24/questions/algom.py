# Function to calculate the maximum number of chocolate packs
def max_chocolate_packs(x, y, a, b):
    if x < y:
        x, y = y, x
    if a < b:
        a, b = b, a

    # Calculate x/a and y/b and find the minimum
    if x // a >= y // b:
        return y // b
    else:
        c = x // a
        packs_for_other_type = c

        # Find the overflowing candies in that type
        extra_a_chocolates = x - c * a
        extra_b_chocolates = y - c * b
        
        extrapacks = c
        while extra_a_chocolates > 0:  # Use a while loop here
            extra_a_chocolates -= b  # Fix this line, subtract b from extra_a_chocolates
            extrapacks += 1
            
        # Calculate the result by dividing the overflow into the other type
        if a <= b:
            new_packs_for_y = packs_for_other_type + (extra_a_chocolates * b) // a
            result = max(c, new_packs_for_y)
        else:
            new_packs_for_x = packs_for_other_type + (extra_b_chocolates * a) // b
            result = max(c, new_packs_for_x)

        return result

# Input number of test cases
t = int(input())
for _ in range(t):
    # Input x, y, a, and b for each test case
    x, y, a, b = map(int, input().split())
    
    # Calculate and print the maximum number of packs
    print(max_chocolate_packs(x, y, a, b))
