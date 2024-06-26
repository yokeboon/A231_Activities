import os
os.system('cls')

def login(user_id, password):
    # Remove whitespace
    user_id = user_id.replace(" ", "")

    # Check if user ID has at least 12 characters and contains only capital letters
    if len(user_id) < 12 or not user_id.isupper():
        return False, "Invalid user ID"

    # Check if password contains at least 6 characters from user ID
    count = sum(1 for char in password if char in user_id)
    if count < 6:
        return False, "Weak password"

    # Successful login
    return True, "Welcome to ABC Analytics system"


# Example usage
user_id = input("Enter your user ID: ")
password = input("Enter your password: ")

success, message = login(user_id, password)
if success:
    print(message)
else:
    print("Login failed:", message)
