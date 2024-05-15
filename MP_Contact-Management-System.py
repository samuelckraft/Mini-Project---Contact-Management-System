#Task 1
import re

contacts = {}

def add_contact(contacts):
    email = input('\nEnter email (example@example.com): ')
    name = input('\nEnter name: ')
    phone_number = input('\nEnter phone number (000-000-0000): ')
    address = input('\nEnter address (optional): ')
    notes = input('\nEnter any relevant notes (optional): ')
    email_check = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email)
    name_check = re.search(r"[A-Za-z]", name)
    phone_check = re.search(r"\d{3}-\d{3}-\d{4}", phone_number)
    problems = []

    if email_check == None:
        problems.append('Invalid email format')
    
    if name_check == None:
        problems.append('Invalid name')

    if phone_check == None:
        problems.append('Invalid phone number format')

    if problems:
        print('\nThe following errors have prevented this contact being added: ')
        for problem in problems:
            print(f"- {problem}")
    else:
        contacts[email] = [name.capitalize(), phone_number, address, notes]

def edit_contact(contacts):
    email = input('Please enter email for contact you wish to edit: ')
    if email in contacts:
        print('What would you like to edit?')
        print('1. Name')
        print('2. Email')
        print('3. Phone number')
        print('4. Address')
        print('5. Notes')
        edit_choice = input("Please enter your choice: ")
        if edit_choice == '1':
            new_name = input("Please enter the new name: ")
            if re.search(r"[A-Za-z]", new_name):
                contacts[email][0] = new_name
            else:
                print('Invalid name format')
        elif edit_choice == '2':
            new_email = input("Please enter new email: ")
            contacts[new_email] = contacts.pop(email)
        elif edit_choice == '3':
            new_number = input('Please enter new phone number (000-000-0000): ')
            if re.search(r"\d{3}-\d{3}-\d{4}", new_number):
                contacts[email][1] = new_number
            else:
                print('Invalid phone number format')
        elif edit_choice == '4':
            new_address = input('Please enter new address: ')
            contacts[email][2] = new_address
        elif edit_choice == '5':
            new_notes = input('Enter new notes for contact: ')
            contacts[email][3] = new_notes
    else:
        print(f"Contact with email '{email}' not found")


def delete_contact(contacts):
    email = input('Please enter email for contact you wish to delete: ')
    if email in contacts:
        contacts.pop(email)
        print(f"Contact with email '{email}' deleted")
    else:
        print(f"Contact with email '{email}' not found")
    print(contacts)

def search_contact(contacts):
    email = input('Please enter email for contact you wish to search: ')
    if email in contacts:
        print(f"\nInfo for contact '{email}': \n")
        print(f'Name - {contacts[email][0]}')
        print(f'Phone Number - {contacts[email][1]}')
        if contacts[email][2]:
            print(f'Address - {contacts[email][2]}')
        else:
            pass

        if contacts[email][3]:
            print(f'Notes - {contacts[email][3]}')
        else:
            pass
    else:
        print(f"Contact with email '{email}' not found")


def display_contacts(contacts):
    for email, info in contacts.items():
        if contacts[email][2]:
            pass
        else:
            contacts[email][2] = 'N/A'

        if contacts[email][3]:
            pass
        else:
            contacts[email][3] = 'N/A'

        print(f'\nEmail - {email}\nName - {info[0]}\nPhone Number - {info[1]}\nAddress - {info[2]}\nNotes - {info[3]}')

def export_contacts(contacts):
    file_name = input('Please enter the name of the text file you would like to export to (do not type .txt or allow any whitespaces): ') + '.txt'
    with open(file_name, 'w') as file:
        for email, info in contacts.items():
            if contacts[email][2]:
                pass
            else:
                contacts[email][2] = 'N/A'

            if contacts[email][3]:
                pass
            else:
                contacts[email][3] = 'N/A'
            file.write(f'\nEmail - {email}\nName - {info[0]}\nPhone Number - {info[1]}\nAddress - {info[2]}\nNotes - {info[3]}\n')

def import_contacts(contacts):
    file_name = input('Please enter the name of the text file you would like to import from (do not type .txt or allow any whitespaces): ') + '.txt'
    with open(file_name, 'r') as file:
        for line in file:
            email = re.findall(r"Email - [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", line)
            name = re.findall(r"Name - \w+\s\w+", line)
            number = re.findall(r"Phone Number - \d{3}-\d{3}-\d{4}", line)
            address = re.findall(r"Address - ", line)
            notes = re.findall(r"Notes - ", line)


        


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
        edit_contact(contacts)
    elif choice == '3':
        delete_contact(contacts)
    elif choice == '4':
        search_contact(contacts)
    elif choice == '5':
        display_contacts(contacts)
    elif choice == '6':
        export_contacts(contacts)
    elif choice =='7':
        import_contacts(contacts)
    elif choice == '8':
        print("\nClosing Contact Management System!")
        break
    else:
        print("\nInvalid option please try again")