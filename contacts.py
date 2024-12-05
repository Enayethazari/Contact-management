from utils import validate_name, validate_email, validate_phone

def add_contact(contacts):
    print("\nAdd a New Contact")
    name = input("Name: ")
    if not validate_name(name):
        print("Invalid name. Must be alphabetic.")
        return

    phone = input("Phone Number: ")
    if not validate_phone(phone):
        print("Invalid phone number. Must be numeric.")
        return

    if phone in [contact['Phone'] for contact in contacts]:
        print("Phone number already exists!")
        return

    email = input("Email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return

    address = input("Address: ")
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    print("\nContact List:")
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['Name']} | {contact['Phone']} | {contact['Email']} | {contact['Address']}")

def search_contact(contacts):
    print("\nSearch Contact")
    query = input("Enter name, phone, or email to search: ").strip().lower()
    results = [c for c in contacts if query in (c['Name'].lower(), c['Phone'], c['Email'].lower())]

    if results:
        print("Search Results:")
        for contact in results:
            print(f"{contact['Name']} | {contact['Phone']} | {contact['Email']} | {contact['Address']}")
    else:
        print("No contacts found.")

def remove_contact(contacts):
    print("\nRemove a Contact")
    name = input("Enter the name of the contact to remove: ").strip()
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} removed successfully!")
            return
    print("Contact not found.")
