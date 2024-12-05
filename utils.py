import re

def validate_name(name):
    return name.isalpha()

def validate_phone(phone):
    return phone.isdigit()

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)
