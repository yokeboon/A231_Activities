import os
os.system('cls')

loop = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = 1  # Start with the first odd index position

while index < len(loop):
    print(loop[index])
    index += 2  # Move to the next odd index position
    if index ==7:
        break