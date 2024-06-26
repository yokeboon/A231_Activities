import os
os.system('cls')

menu_info = [{'food': 'chicken', 'Price': 10},
             {'food': 'fish', 'Price': 15},
             {'food': 'beef', 'Price': 20}]

for i in menu_info:
    price =i['Price'] 
    print(price)

#values = [entry[list(entry.keys())[1]] for entry in menu_info]
#print (values)