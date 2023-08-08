# v.1

class AddressBook:
    def __init__(self, name, details):
        self.name = name
        self.details = details
        print('Added new contact.\nName: {}\nContacted details: {}'.format(self.name, self.details))


number = 0
while True:
    command = input('Create new contact ("Yes" or "No"): ')

    if command == "No":
        futher = input('What you want to do ("Crate" or "View"): ')
        if futher == "View":
            list_ = open('AddressBook.txt', 'r')
            print(list_.read())
            list_.close()

    elif command == "Yes":
        name = input('Enter a name for the new contact: ')
        if len(name) > 0:
            details = input('Enter address data: ')
        command = "no"
        number += 1
        inf = "Contact #{}.\nName: {}\nContacted details: {}".format(number, name, details)
        list_ = open('AddressBook.txt', 'w')
        list_.write(inf)
        list_.close()

        p = AddressBook(name, details)
    else:
        print('Entered wrong command.')
