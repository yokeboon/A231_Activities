import os
os.system ("cls")

import pandas as pd
a = ['saya', 'suka','makan']

b = pd.Series(a,index =['world1', 'world2', 'world3'])

print(b)
print(b['world2'])