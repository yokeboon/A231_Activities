import random

def generate_integer_array(size):
    return [random.randint(0, 500) for _ in range(size)]

# Example usage:
array_size = 10  # You can change the size as needed
integer_array = generate_integer_array(array_size)
print("Generated Integer Array:", integer_array)
