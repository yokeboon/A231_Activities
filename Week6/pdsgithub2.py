import pandas as pd

# Create a sample DataFrame

Student_ID = [1001, 1002, 1003, 1004, 1005]
Name = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']

datalist =[Student_ID, Name]

df = pd.DataFrame(datalist)
print(df)