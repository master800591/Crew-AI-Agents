import json
import re
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import hashlib
import base64
from flask import Flask, render_template, request
import csv
import os
import string
import uuid
import random
from datetime import datetime
import pyttsx3


# ANSI escape codes for text colors

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[30m'
    GRAY = '\033[90m'
    LIGHT_RED = '\033[31m'
    LIGHT_GREEN = '\033[32m'
    LIGHT_YELLOW = '\033[33m'
    LIGHT_BLUE = '\033[34m'
    LIGHT_MAGENTA = '\033[35m'
    LIGHT_CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    WARNING = '\033[93m'
    INFO = '\033[96m'
    TITLE = '\033[95m'
    MENU = '\033[94m'
    BACKGROUND_YELLOW = '\033[43m'
    BACKGROUND_CYAN = '\033[46m'
    END = '\033[0m'


engine = pyttsx3.init()

def get_uuid():
    new_uuid = uuid.uuid4()
    return new_uuid



def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux
    else:
        _ = os.system('clear')



def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096
    )
    public_key = private_key.public_key()
    
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()
    
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
    
    return pem_private, pem_public

def load_credentials():
    try:
        with open("credentials.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def hash_password(password):
    salt = b'salt_'
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_password

def verify_password(password, hashed_password):
    return hashed_password == hash_password(password)

def check_names(first_name, last_name, stored_names):
    full_name = f"{first_name} {last_name}"
    new_name = full_name
    while new_name in stored_names:
        new_name += "1"
    return new_name

def save_private_key(full_name, private_key):
    private_key_str = private_key
    with open(f"keys\{full_name}_private_key.pem", "w") as f:
        f.write(private_key_str)

def save_credentials(credentials_data):
    with open("credentials.json", "w") as f:
        json.dump(credentials_data, f, indent=4)


def get_user_full_name(user):
    return f"{user['full_name']}"

def get_user_email(user):
    return f"{user['email']}"

def get_user_public_key(user):
    return f"{user['public_key']}"

def print_ct(text, color):
    print(f"{color}{text}{colors.END}")
    #engine.say(text)     #disabled for speed and testing
    #engine.runAndWait()   #disabled for speed and testing


def verify_password(password, hashed_password):
    return hashed_password == hash_password(password)


def encrypt_data(data, public_key):
    public_key = serialization.load_pem_public_key(public_key)
    encrypted_data = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data

def decrypt_data(encrypted_data, private_key):
    private_key = serialization.load_pem_private_key(private_key, password=None)
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()
    return decrypted_data


def print_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print_ct(content, colors.RED)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")


def accept_or_exit():
    print_text_file("terms_of_service.txt")
    print_text_file("copyright.txt")
    choice = input("Do you accept these Terms of Service and policies? (Type 'accept' to proceed or 'exit' to leave): ")
    
    if choice.lower() == 'accept':
        print("Thank you for accepting the Terms of Service. Enjoy using [Your Company/Platform Name]!")
        # Add your main program logic here
    elif choice.lower() == 'exit':
        print("You have chosen to exit. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please type 'accept' to proceed or 'exit' to leave.")
        accept_or_exit()



def get_country_info():
    file_path = os.path.join("CSV", "data", "Regions.csv")
    
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        data_list = list(reader)
    
    code_input = input("Enter the three-letter country code: ").upper()
    
    #print("Debug: Input code:", code_input)      #debug code 
    
    for country, region, iso_alpha3 in data_list:
        #print("Debug: Checking entry -", iso_alpha3, country, region)    #debug code
        if iso_alpha3 == code_input:
            return region, country
    
    return None, "Country not found"


# Test the function and to see if how sets the information for the vars. 
#region, country = get_country_info()
#print("Region:", region)
#print("Country:", country)


def calculate_age(dob):
    today = datetime.date.today()
    print(today)
    dob = datetime.strptime(dob, "%Y/%m/%d").date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def signup(account_type):

    Account_ID = str(get_uuid())
    first_name = input("Enter first name: ").title()
    last_name = input("Enter last name: ").title()
    email = input("Enter email address: ").lower()
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        print("Invalid email address format. Please try again.")
        return
    
    dob = input("Enter date of birth (YYYY/MM/DD): ")
    if not re.match(r"\d{4}/\d{2}/\d{2}", dob):
        print("Invalid date of birth format. Please use YYYY/MM/DD.")
        return
    age = calculate_age(dob)
    if age < 18:
        print("You must be at least 18 years old to register on this platform.")
        return
    # gets region and country of the user. 
    region, country = get_country_info()

    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        private_key, public_key = generate_key_pair()
        hashed_password = hash_password(pwd)
        hashed_password_base64 = base64.b64encode(hashed_password).decode()

        with open("credentials.json", "r") as f:
            credentials_data = json.load(f)

        stored_emails = [user["email"] for user in credentials_data]  # corrected variable name

        if email in stored_emails:
            print("Email is already in use. Please try with a different email.")
            return

        full_name = check_names(first_name, last_name, stored_emails)  # corrected variable name

        credentials_data.append({
        
            "account_id": Account_ID,
            "account_type": account_type,
            "full_name": full_name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "date_of_birth": dob,
            "region":region,
            "country":country,
            "hashed_password": hashed_password_base64,
            "public_key": public_key
        })

        with open("credentials.json", "w") as f:
            json.dump(credentials_data, f, indent=4)

        save_private_key(full_name, private_key)

        print("You have registered successfully!")
    else:
        print("Passwords do not match.\n")




def login():
    credentials_data = load_credentials()

    email = input("Enter email address: ").lower()
    password = input("Enter password: ")

    for user in credentials_data:
        if user["email"] == email:
            hashed_password = base64.b64decode(user["hashed_password"])
            if verify_password(password, hashed_password):
                print("Login successful.")
                return user
            else:
                print("Login Failled.")
                return None

    print("User not found.")
    

    return None


def create_batch_government_accounts_from_csv(csv_file):
    #Domain name,Domain type,Agency,Organization name,City,State,Security contact email
    credentials_data = load_credentials()

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            domain_name, domain_type, agency, org_name, city, state, security_email = row

            print("domain_name", domain_name, "domain_type", domain_type,"agency", agency, org_name, city, state, security_email )

            Account_ID = str(get_uuid())
            email = security_email.lower()
            contact_person = security_email
            region, country = "North America", "United States"   # Assuming this function provides region and country based on location

            pwd = generate_password()  # You may define a function to generate a random password
            private_key, public_key = generate_key_pair()
            hashed_password = hash_password(pwd)
            hashed_password_base64 = base64.b64encode(hashed_password).decode()

            stored_emails = [user["email"] for user in credentials_data]

            if email in stored_emails:
                print(f"Email '{email}' is already in use. Skipping this agency.")
                continue

            credentials_data.append({
                "account_id": Account_ID,
                "agency_name": org_name,
                "contact_person": contact_person,
                "city": city,
                "city": state,
                "email": email,
                "region": region,
                "country": country,
                "hashed_password": hashed_password_base64,
                "public_key": public_key
            })

            save_private_key(org_name, private_key)

            with open('agencies.csv', mode='a', newline='') as agencies_file:
                writer = csv.writer(agencies_file)
                writer.writerow([agency, pwd])  # Write agency name and plain text password to agencies.csv

    save_credentials(credentials_data)

    print("Batch government agency account creation from CSV completed.")

# Example usage of create_batch_government_accounts_from_csv()
csv_file_path = os.path.join("CSV", "data", "us_gov_Domains.csv")
#create_batch_government_accounts_from_csv(csv_file_path)




#### MENU OPERATIONS!!!! ######

def individual_menu(user):
    print("Individual ussers Menu Options:")
    # Add options specific to individual accounts

def government_agency_menu(user):
    print("Government Agency Menu Options:")
    # Add options specific to government agency accounts

def company_menu(user):
    print("Company Menu Options:")
    # Add options specific to company accounts






def display_menu():
    print_ct("Welcome to the registration portal.", colors.TITLE)
    print_ct("Please select your account type:", colors.MENU)
    print_ct("1. Individual NOT a PUBLIC OFFICIAL ", colors.MENU)
    print_ct("2. Government OFFICIAL", colors.MENU)
    print_ct("4. return to main menu", colors.MENU)
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        signup("individual")
    elif choice == '2':
        signup("gov_Official")
    elif choice == '4':
        main()
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    clear_screen()
    accept_or_exit()
    clear_screen()
    print_ct("Welcome to the TBD.", colors.TITLE)
    user = None
    while not user:
        choice = input("Do you want to login,sign up or exit? (login/signup/exit): ")
        if choice.lower() == "login":
            user = login()
        elif choice.lower() == "signup":
            display_menu()  # Display account type selection menu
        elif choice.lower() == "exit":
            exit()
        else:
            print_ct("Invalid choice. Please try again.", colors.WARNING)

    # Add code here to execute other programs that require authentication
    print(get_user_full_name(user))
    account_type = user.get("account_type")  # Get user's account type
    print(f"Welcome, {get_user_full_name(user)}!")
    
    if account_type == "individual":
        individual_menu(user)
    elif account_type == "government agency":
        government_agency_menu(user)
    elif account_type == "company":
        company_menu(user)
    else:
        print("Invalid account type. Please contact support.")
if __name__ == "__main__":
    main()