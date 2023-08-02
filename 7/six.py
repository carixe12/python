contacts = {}

while True:
    action = int(input("Enter action number:\n1. Add contact.\n2. Find a person.\n"))

    if action == 1:
        name = tuple(input("Enter the first and last name of the new contact (separated by a space):\n").split())
        phone = input("Enter phone number:\n")
        if name in contacts:
            print("Such a person is already in the contacts.")
        else:
            contacts[name] = phone
        print("Current contact dictionary:", contacts)

    elif action == 2:
        lastname = input("Enter last name to search:\n")
        found = False
        for name, phone in contacts.items():
            if name[1].lower() == lastname.lower():
                print(name[0], name[1], phone)
                found = True
        if not found:
            print("No contacts with the last name", lastname)

    else:
        print("Invalid action number. Please choose again.")