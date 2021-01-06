#!/usr/bin/env python3

class Contact:
    def __init__(self):
        self.book = []
        self.names = []
        self.numbers = []

    def create(self, name, number, email):
        self.book.append([name, number, email])
        self.names.append(name)
        self.numbers.append(number)
        print(name, 'Contact created successfully!')

    def update(self, name=False, number=False): #update using names
        if name:
            if name in self.names:
                inames = [i for i, x in enumerate(self.names) if x == name]
                print('No.of contacts found: ', len(inames), inames)
                c = 1
                for iname in inames:
                    print(c, 'name: ', self.names[iname],
                          'details: ', self.book[iname], '\n')
                    c += 1
                d = 'y'
                while d:
                    inp = input(
                        "Press 'y' to continue or exit to 'n': ").lower()
                    if inp == 'y':
                        nm_i = int(
                            input('Enter index of listed contact above: '))

                        try:
                            data = inames[nm_i-1]
                            print('\nDetails: ', self.book[data])
                            print(1, '- Name: ', self.book[data][0])
                            print(2, '- Number: ', self.book[data][1])
                            print(3, '- Email: ', self.book[data][2])
                            print(0, '- Exit')

                            v = 'y'
                            while v:
                                ch = int(
                                    input('Enter index of listed contact above: '))
                                if ch == 1:
                                    ch_name = input('Enter name to update: ')
                                    self.book[data][0] = ch_name
                                    self.names[data] = ch_name

                                elif ch == 2:
                                    ch_number = input(
                                        'Enter Number to update: ')
                                    self.book[data][1] = ch_number
                                    self.numbers[data] = ch_number
                                elif ch == 3:
                                    ch_email = input('Enter Email to update: ')
                                    self.book[data][2] = ch_email
                                elif ch == 0:
                                    v = False
                                else:
                                    v = False

                            print('#---------------- Updated contact -------------#')
                            print(self.book[data])
                            print(self.names[data])
                            print(self.numbers[data])

                        except:
                            print('Index not found..!')

                    else:
                        break
            else:
                print('No contact found..!')

    # -------------------------------- Update Using Numbers ----------------------#
        elif number:
            if number in self.numbers:

                inumbers = [i for i, x in enumerate(
                    self.numbers) if x == number]
                print('No.of contacts found: ', len(inumbers))
                c = 1
                for inumber in inumbers:
                    print(
                        c, 'Number: ', self.numbers[inumber], 'details: ', self.book[inumber], '\n')
                    c += 1

                d = 'y'
                while d:
                    inp = input("Press 'y' to continue or exit to 'n': ")
                    if inp == 'y':
                        nm_i = int(
                            input('Enter index of listed contact above: '))

                        try:
                            data = inumbers[nm_i-1]
                            print('\nDetails: ', self.book[data])
                            print(1, '- Name: ', self.book[data][0])
                            print(2, '- Number: ', self.book[data][1])
                            print(3, '- Email: ', self.book[data][2])
                            print(0, '- Exit')

                            v = 'y'
                            while v:
                                ch = int(
                                    input('Enter index of listed contact above: '))
                                if ch == 1:
                                    ch_name = input('Enter name to update: ')
                                    self.book[data][0] = ch_name
                                    self.names[data] = ch_name

                                elif ch == 2:
                                    ch_number = input(
                                        'Enter Number to update: ')
                                    self.book[data][1] = ch_number
                                    self.numbers[data] = ch_number
                                elif ch == 3:
                                    ch_email = input('Enter Email to update: ')
                                    self.book[data][2] = ch_email
                                elif ch == 0:
                                    v = False
                                else:
                                    v = False

                            print('#---------------- Updated contact -------------#')
                            print(self.book[data])
                            print(self.names[data])
                            print(self.numbers[data])

                        except:
                            print('Index not found..!')

                    else:
                        break
            else:
                print('No contact found..!')
        else:
            print('No conatact Found..!')

    #------------------------------ DELETE Contacts --------------------------#
    def delete(self, name=False, number=False):

        if name:
            if name in self.names:
                d = 'y'
                while d:
                    inames = [i for i, x in enumerate(self.names) if x == name]
                    if len(inames) > 0:
                        print('No.of contacts found: ', len(inames), inames)
                        c = 1
                        for iname in inames:
                            print(
                                c, 'name: ', self.names[iname], 'details: ', self.book[iname], '\n')
                            c += 1

                        inp = input("Press 'y' to continue or exit to 'n': ")

                        if inp == 'y':
                            nm_i = int(
                                input('Enter index of listed CONTACT above: '))

                            try:
                                data = inames[nm_i-1]
                                print('\nDetails: ', self.book[data])

                                f = input(
                                    'Are you sure want to DELETE..? (y/n): ').lower()
                                if f == 'y':
                                    del self.book[data]
                                    del self.numbers[data]
                                    del self.names[data]

                                print(
                                    '#---------------- Updated contact Book -------------#')
                                print('\nDetails: ', self.book)
                                print('\nName Entries: ', self.names)
                                print('\nNumber Entries: ', self.numbers)
                            except:
                                print('\nIndex not found..!')
                        else:
                            break
                    else:
                        print('0 contacts found..!')
                        break
            else:
                print('Contact not found..!')

        elif number:
            if number in self.numbers:
                d = 'y'
                while d:
                    inumbers = [i for i, x in enumerate(
                        self.numbers) if x == number]
                    if len(inumbers) > 0:
                        c = 1
                        for inumber in inumbers:
                            print(
                                c, 'number: ', self.numbers[inumber], 'details: ', self.book[inumber], '\n')
                            c += 1

                        inp = input("Press 'y' to continue or exit to 'n': ")
                        if inp == 'y':
                            nm_i = int(
                                input('Enter index of listed CONTACT above: '))

                            try:
                                data = inumbers[nm_i-1]
                                print('\nDetails: ', self.book[data])

                                f = input(
                                    'Are you sure want to DELETE..? (y/n): ').lower()
                                if f == 'y':
                                    del self.book[data]
                                    del self.numbers[data]
                                    del self.names[data]

                                print(
                                    '#---------------- Updated contact Book -------------#')
                                print('\nDetails: ', self.book)
                                print('\nName Entries: ', self.names)
                                print('\nNumber Entries: ', self.numbers)
                            except:
                                print('\nIndex not found..!')
                        else:
                            break
                    else:
                        print('0 contacts found..!')
                        break

            else:
                print('No contact Found..!')

        else:
            print('No conatact Found..!')

    #------------------------- PhoneBook ---------------------------#
    def phonebook(self):
        print('\nTotal Contacts found: ', len(self.book))
        for contact in self.book:
            print('\nName: ', contact[0])
            print('Phone Number: ', contact[1])
            print('Email: ', contact[2])

    #-------------------------------------- Search Contact -----------------------------#
    def search(self, number=False, name=False):

        if name:
            if name in self.names:
                inames = [i for i, x in enumerate(self.names) if x == name]

                c = 1
                for iname in inames:
                    print(c, 'name: ', self.names[iname],
                          'details: ', self.book[iname], '\n')
                    c += 1
            else:
                print('No contact found..!')

        elif number:
            if number in self.numbers:
                inumbers = [i for i, x in enumerate(
                    self.numbers) if x == number]
                c = 1
                for inumber in inumbers:
                    print(
                        c, 'number: ', self.numbers[inumber], 'details: ', self.book[inumber], '\n')
                    c += 1

            else:
                print('No contact found..!')
        else:
            print('No contact found..!')


menu = '''
          1.Create
          2.Update
          3.List Contacts
          4.Search
          5.Delete
          6.Exit
'''

if __name__ == "__main__":

    c = Contact()

    a = True
    while a:
        print('\n', menu, '\n')
        choice = int(input('\nEnter your Choice: '))
        if choice == 1:
            name = input('Name: ')
            phone = input('Phone No.: ')
            email = input('E-mail Address: ')
            c.create(name, phone, email)
        elif choice == 2:
            k = True
            while k:
                print(
                    '''
                    1. Update through name
                    2. Update through number
                    3. Exit
                    '''
                )
                inp = int(input('Enter input: '))

                if inp == 1:
                    name = input('Enter name: ')
                    c.update(name=name)
                elif inp == 2:
                    number = input('Enter Number: ')
                    c.update(number=number)
                else:
                    k = False
        elif choice == 3:
            c.phonebook()

        elif choice == 4:
            k = True
            while k:
                print(
                    '''
                    1. Search through name
                    2. Search through number
                    3. Exit
                    '''
                )
                inp = int(input('Enter input: '))

                if inp == 1:
                    name = input('Enter name: ')
                    c.search(name=name)
                elif inp == 2:
                    number = input('Enter Number: ')
                    c.search(number=number)
                else:
                    k = False

        elif choice == 5:
            k = True
            while k:
                print(
                    '''
                    1. Delete through name
                    2. Delete through number
                    3. Exit
                    '''
                )
                inp = int(input('Enter input: '))

                if inp == 1:
                    name = input('Enter name: ')
                    c.delete(name=name)
                elif inp == 2:
                    number = input('Enter Number: ')
                    c.delete(number=number)
                else:
                    k = False
        elif choice == 6:
            a = False
        else:
            break
