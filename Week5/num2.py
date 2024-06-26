import os

try:

     # Attempt to clear the screen for Windows if the first try fails
    os.system('cls')
except:
    # Output an error message if both attempts fail
    print("Unable to clear the screen.")


import numpy as np  # Import the NumPy library for numerical operations

# Create 1D NumPy arrays
# Initializing 1-dimensional arrays 
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

print(arr1 + arr2)
