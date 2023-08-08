# version 3.0

import pickle

start = True

while start:
    menu = input('\nWhat do you want to do:\n(Add, Delete, View, To find, Stop, Help) --> ')
    f = open('Addressbook.txt', 'rb')
    ab = pickle.load(f)

    if menu == "Add":
        key = input('\nNew contact.\nName: ')
        value = input('Address: ')
        ab[key] = value
        f = open('Addressbook.txt', 'wb')
        pickle.dump(ab, f)

    elif menu == "View":
        f = open('Addressbook.txt', 'rb')
        ab = pickle.load(f)
        print('\nThere are {} contacts in the address-book'.format(len(ab)))
        for name, address in ab.items():
            print('Contact {} at {}'.format(name, address))

    elif menu == "Delete":
        name = input('\nEnter the name of contact you want to delete --> ')
        if name in ab:
            f = open('Addressbook.txt', 'wb')
            del ab[name]
            pickle.dump(ab, f)
        else:
            print('Contact does not exist.')

    elif menu == "To find":
        name = input('\nSearch: Enter name --> ')
        if name in ab:
            print('Contact {} at {}'.format(name, ab[name]))
        else:
            print('Contact does not exist.')

    elif menu == "Stop":
        print('\nProgram completed')
        start = False

    elif menu == "Help":
        print('\nCommand:'
              '\nAdd - create new contact\nDelete - delete contact'
              '\nView - view the entire address book\nTo find - to find contact'
              '\nStop - stop the program')

    else:
        print('\nInvalid command entered.')

    f.close()
    del ab
