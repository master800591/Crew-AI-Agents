import json
import re
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import hashlib
import base64
from flask import Flask, render_template, request
import csv
import os
import uuid

def get_uuid():
    new_uuid = uuid.uuid4()
    return new_uuid


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
    with open(f"{full_name}_private_key.pem", "w") as f:
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



def get_country_info():
    file_path = os.path.join("CSV", "data", "Regions.csv")
    
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        data_list = list(reader)
    
    code_input = input("Enter the three-letter country code: ").upper()
    
    print("Debug: Input code:", code_input)
    
    for country, region, iso_alpha3 in data_list:
        print("Debug: Checking entry -", iso_alpha3, country, region)
        if iso_alpha3 == code_input:
            return region, country
    
    return None, "Country not found"

# Test the function
region, country = get_country_info()
print("Region:", region)
print("Country:", country)



def signup():

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
    


app = Flask(__name__)

# Existing route for signup
@app.route('/signup', methods=['GET', 'POST'])
def signup_view():
    if request.method == 'POST':
        signup()
    return render_template('signup.html')

# Existing route for login
@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        user = login()
        if user:
            return render_template('profile.html', user=user)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)