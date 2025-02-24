import random

def generate_random_string(length=1000):
    return ''.join(random.choice('OE') for _ in range(length))

random_string = generate_random_string()
print(random_string)