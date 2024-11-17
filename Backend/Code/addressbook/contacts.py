contacts = [] # Phone Book
# Dictionary of Contacts that basically has name, Phone, email
# if adding a contact, I can append the dictionary of new values to contact(i.e my phone Book)
def add_contact(name,phone):

    contact = {
        "name":name,
        "phone":phone,
    }
    contacts.append(contact)

    print(f"Contact {name} added Successfully")


def remove_contact(name):
    """
    Removes a contact by name
    """

    global contacts
    contacts = [i for i in contacts if i['name'] != name ]
    print(f"Contact {name} removed Successfully")


def list_contacts():

    if len(contacts)>0:
        print("Below are the List of contacts in the Adressbook")
        for c in contacts:
            print(f"Name: {c['name']} \nphone: {c['phone']}")
    else:
        print("No contacts available")


def find_contact(name):
    """
    Find a contact by name
    """

    for c in contacts:
        if c['name'] == name:
            print(f"Contact Found {c['name']}")
            break
    else:
        print("Contact not found")

    



