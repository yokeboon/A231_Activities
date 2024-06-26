import os
os.system("cls")

def categorize_age(name, age):
    if age < 13:
        age_group = "Kid"
    elif age >= 13 and age <= 17:
        age_group = "Teenage"
    elif age > 17 and age <= 55:
        age_group = "Adult"
    else:
        age_group = "Elderly"

    print(f"{name} is {age} years old and belongs to the {age_group} group.")

# Example usage:
name = input("Enter the person's name: ")
age = int(input("Enter the person's age: "))
categorize_age(name, age)
