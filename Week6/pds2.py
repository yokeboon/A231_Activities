import pandas as pd
import numpy as np

#using lists
data_list = [[1, 'ALice'],[2, 'Bob'], [3, 'Carlie' ]]
df_list = pd. DataFrame ( data_list , columns =['ID', 'Name'])
print ('DataFrame from Lists:')
print (df_list. head())