# Define a function named 'sum_numbers' which takes multiple arguments
def sum_numbers(*args):
    total = 0
    for num in args:
        total =total+ num
    return total

# Call the function 'sum_numbers' with different numbers of arguments
result1 = sum_numbers(1, 2, 3, 4, 5)
print("Result 1:", result1)  # Output: Result 1: 15

result2 = sum_numbers(10, 20, 30)
print("Result 2:", result2)  # Output: Result 2: 60

result3 = sum_numbers(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
print("Result 3:", result3)  # Output: Result 3: 110
