import hashlib
import time
import sys

import string


# A text file to store all the usernames and their respective passwords
PASSWORD_FILE = "Passwords.txt"

# A OTP generator that refreshes every 15 secs
def generate_otp(username, password, interval=15):
    # time.time() returns the current time in seconds and dividing by the interval of 15 secs
    time_window = int(time.time() / interval)
    # A formatted string is created by combining username, password, and time_window
    data = f"{username}{password}{time_window}".encode()
    # Generates a SHA-256 hash of the input data
    hash_digest = hashlib.sha256(data).hexdigest()
    # The modulo operation % 10**6 reduces this large integer to a 6-digit number.
    otp = int(hash_digest, 16) % 10**6
    return f"{otp:06d}"

'''
Cryptographic hash functions like SHA-256 are designed to be one-way functions. 
his means that even if someone knows the resulting hash or OTP, they cannot feasibly reverse-engineer it to find the original input 
'''

# To check if the otp matches 
def validate_otp(username, password, otp):
    expected_otp = generate_otp(username, password)
    return expected_otp == otp

# To open the PASSWORD_FILE and check if the user exists
def validate_user(username, password):
    with open(PASSWORD_FILE, "r") as file:
        credentials = file.readlines()
    for line in credentials:
        stored_username, stored_password = line.strip().split(":")
        if stored_username == username and stored_password == password:
            return True
    return False

# Adding a password requirement
def password_criteria(password):
    counter = 0 

    counter += any(c.isupper() for c in password)  # Check for uppercase
    counter += any(c.islower() for c in password)  # Check for lowercase
    counter += any(c.isdigit() for c in password)   # Check for digits
    counter += any(c in string.punctuation for c in password)  # Check for symbols

    return (len(password)>= 8 and counter == 4)

# Using the file.write to add the user:password into the txt file
def save_user(username, password):
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{username}:{password}\n")

# To prevent exisiting user to be added
def user_exists(username):
    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if stored_username == username:
                return True
    return False


def authenticate_user(username, password, otp):
    if not validate_user(username, password):
        print("Authentication failed. Invalid username or password.")
        return
    if validate_otp(username, password, otp):
        print("Authentication successful.")
    else:
        print("Authentication failed. Invalid OTP.")

def register_user(username):
    if user_exists(username):
        print("Username already exists. Choose a different username.")
        return
    
    # Loop to ensure that user meet the password requirements
    continuous_loop = True
    while continuous_loop:
        password = input("Enter password: ")

        if not password_criteria(password):
            print("Password must be at least 8 characters long, contain letters and numbers.")
            continue

        confirm_password = input("Confirm password: ")

        if password != confirm_password:
            print("Passwords do not match.")
            continue
        
        save_user(username, password)
        print("User registered successfully.")
            
        continuous_loop = False


    

    

def connect_main():
    if len(sys.argv) < 3:
        print("Usage: python connect.py <username> <new|password pin>")
        return

    username = sys.argv[1]
    action_or_password = sys.argv[2]

    if action_or_password.lower() == "new":
       register_user(username)
    elif len(sys.argv) == 4:
        password = action_or_password
        otp = sys.argv[3]
        authenticate_user(username, password, otp)
    else:
        print("Invalid command format. Use 'new' for registration or provide 'password pin' for authentication.")

if __name__ == "__main__":
    connect_main()