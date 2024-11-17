from addressbook import contacts 


def main():

    print("Welcome to AdressBook")

    while True:
        print("\n Select an option from the below")
        print("1. Add a contact")
        print("2. Remove a contact")
        print("3. list a contact")
        print("4. find a contact")
        print("5. Exit")

        choice = input("Enter your Choice : ")

        if choice == '5':
            print("Exiting from the Address Book.")
            break

        if choice == '1':
            name = input("Enter your name: ")
            phone  = input("Enter your Phone Number")
            contacts.add_contact(name,phone)
        elif choice == '2':
            name = input("Enter your name: ")
            contacts.remove_contact(name)
        elif choice == '3':
            contacts.list_contacts()
        elif choice == '4':
            name = input("Enter your name: ")
            contacts.find_contact(name)
        else:
            print("Invalid Choice Please enter a number between 1 and 5")





if __name__ == "__main__":
    main()