# Phonebook program

# Initialize an empty dictionary to store contacts
phonebook = {}

# Function to display all contacts in alphabetical order
def display_contacts():
    if not phonebook:
        print("Your phonebook is empty.")
    else:
        # Sort the contacts by name and display them
        for name in sorted(phonebook.keys()):
            print(f"{name}: {phonebook[name]}")

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    if name in phonebook:
        print(f"{name} already exists in your phonebook.")
    else:
        phone_number = input("Enter the contact's phone number: ")
        phonebook[name] = phone_number
        print(f"Contact {name} added successfully.")

# Function to search for a contact by name
def search_contact():
    name = input("Enter the name of the contact you want to search for: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"No contact found for {name}.")

# Function to update a contact's phone number
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in phonebook:
        new_number = input(f"Enter the new phone number for {name}: ")
        phonebook[name] = new_number
        print(f"Contact {name} updated successfully.")
    else:
        print(f"No contact found for {name}.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found for {name}.")

# Main menu function
def menu():
    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Display all contacts")
        print("2. Add a new contact")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")

        choice = input("Please choose an option (1-6): ")

        if choice == '1':
            display_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the phonebook program.")
            break
        else:
            print("Invalid choice, please try again.")

# Start the phonebook program
menu()
