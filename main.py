from contacts import add_contact, view_contacts, search_contact, remove_contact
from file_handler import load_contacts, save_contacts

def main():
    print("Welcome to the Contact Book Management System!")
    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            remove_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
