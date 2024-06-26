import os
os.system('cls')

import pandas as pd

data_1 =['ali','6']
data_2 = ['abu', '4']

df= pd.DataFrame([data_1,data_2], columns = ['name', 'age'])
print (df)