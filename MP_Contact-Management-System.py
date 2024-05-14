#Task 1
import re
import os
contacts = {}

def add_contact(contacts):
    email = input('\nEnter email: ')
    name = input('\nEnter name: ')
    phone_number = input('\nEnter phone number: ')
    address = input('\nEnter address (optional): ')
    notes = input('\nEnter any relevant notes (optional): ')
    contacts[email] = [name, phone_number, address, notes]
    if re.search(email, )

def edit_contact():
    pass

def delete_contact():
    pass

def search_contact():
    pass

def display_contacts():
    pass

def export_contacts():
    pass

def import_contacts():
    pass



while True:
    print('\nWelcome to the Contact Management System!')
    print('Menu:')
    print('1. Add a new contact')
    print('2. Edit an existing contact')
    print('3. Delete a contact')
    print('4. Search for a contact')
    print('5. Display all contacts')
    print('6. Export contacts to a text file')
    print('7. Import contacts from a text file')
    print('8. Quit')
    choice = input("\nPlease enter your choice: ")

    if choice == '1':
        add_contact(contacts)
    elif choice == '2':
        edit_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        export_contacts()
    elif choice =='7':
        import_contacts()
    elif choice == '8':
        print("\nClosing Contact Management System!")
        break
    else:
        print("\nInvalid option please try again")