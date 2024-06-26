import numpy as np
import os
os.system("cls")

a= np.array ([1,2,3,4,5,6,7,8,9])

b= a.reshape((3,3))
b= b*10+4

print(b)