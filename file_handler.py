import csv

FILE_NAME = "contacts.csv"

def load_contacts():
    contacts = []
    try:
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            contacts = [row for row in reader]
    except FileNotFoundError:
        pass  # No file exists initially
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["Name", "Phone", "Email", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
    print("Contacts saved to file.")
