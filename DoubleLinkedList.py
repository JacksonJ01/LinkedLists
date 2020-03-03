from random import *


class Data:

    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None


class DoubleLinks:

    def __init__(self):
        self.head = None

    def add_head(self, add):
        new = Data(add)
        new.next = self.head
        if self.head is not None:
            self.head.previous = new
        else:
            new.previous = None
        self.head = new
        return

    def add_end(self, add):
        new = Data(add)
        if self.head is None:
            self.head = new
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new
        new.previous = current
        return new.previous.data

    def remove_head(self):
        gone = self.head
        self.head = self.head.next
        self.head.previous = None
        return f'{gone.data} has been removed'

    def remove_end(self):
        if self.head is None:
            return 'No value to remove'
        gone = self.head
        previous = self.head
        while gone.next is not None:
            previous = gone
            gone = gone.next
        previous.next = None
        return f'{gone.data} has been removed'

    def remove(self, remove):
        gone = self.head
        previous = self.head
        if self.head.data == remove and self.head.next is None:
            self.head = None
            return
        elif self.head.data == remove:
            self.head = self.head.next
            self.head.previous = None
            return f'{gone.data} has been removed'
        while gone.next is not None or gone.data == remove:
            if gone.next is None and gone.data == remove:
                previous.next = None
                return f'{gone.data} has been removed'
            if gone.data == remove:
                previous.next = previous.next.next
                gone.next = previous
            previous = gone
            gone = gone.next
        else:
            return 'No data to remove'

    def display(self):
        elements = []
        current = self.head
        if self.head is None:
            return elements
        while current.next is not None:
            elements.append(current.data)
            current = current.next
        elements.append(current.data)
        return elements

    def display_bw(self):
        elements = []
        current = self.head
        while current.next is not None:
            current = current.next
        elements.append(current.data)
        while current.previous is not None:
            elements.append(current.previous.data)
            current = current.previous
        return elements

    def search1(self, search):
        if self.head.data == search:
            return True
        current = self.head
        while current.next is not None or current.data == search:
            if current.data == search:
                return True
            current = current.next
        return False

    def search2(self, search):
        elements = self.display()
        for element in elements:
            if element == search:
                return True
        return False

    def clear_all(self):
        self.head = None
        return

    #
    #
    #
    #

    def interface(self):
        rand = randint(1, 20)
        do = input("\n\nTYPE WHAT YOU WISH TO DO"
                   "\n- ADD HEAD"
                   "\n- ADD END"
                   "\n- REMOVE HEAD"
                   "\n- REMOVE END"
                   "\n- REMOVE"
                   "\n- DISPLAY LIST"
                   "\n- DISPLAY LIST BACKWARDS"
                   "\n- SEARCH LIST"
                   "\n- CLEAR ALL"
                   "\n- EXIT"
                   "\n\n>>>").title()

        if do == "Add Head" or do == "Ah":
            add = input("What value do you wish to add"
                        "\n>>>")
            self.add_head(add)
            self.interface()
            return

        elif do == "Add End" or do == "Ae":
            add = input("What value do you wish to add"
                        "\n>>>")
            print(self.add_end(add))
            self.interface()
            return

        elif do == "Remove Head" or do == "Rh":
            self.remove_head()
            self.interface()
            return

        elif do == "Remove End" or do == "Re":
            self.remove_end()
            self.interface()
            return

        elif do == "Remove" or do == "R":
            remove = input("What value do you wish to remove"
                           "\n>>>")
            if self.search2(remove) is True:
                self.remove(remove)
            else:
                print('Value not in the list')
            self.interface()
            return

        elif do == "Display List" or do == "Dl":
            print(self.display())
            self.interface()
            return

        elif do == 'Display List Backwards' or do == 'Dlb':
            print(self.display_bw())
            self.interface()
            return

        elif do == "Search List" or do == "Sl":
            search = input("What value do you wish to search for"
                           "\n>>>")
            if rand <= 10:
                self.search1(search)
            else:
                self.search2(search)
                self.interface()
            return

        elif do == "Clear All" or do == "Ca":
            self.clear_all()
            self.interface()
            return

        elif do == "Exit" or do == "E":
            print('Bye')
            exit()

        else:
            while do != 'Add Head' or do != "Ah" or do != 'Add End' or do != 'Ae' \
                    or do != 'Remove Head' or do != 'Rh' or do != 'Remove End' or do != 'Re' or do != 'Remove' or do != 'R'\
                    or do != 'Display List' or do != 'Dl' or do != 'Display List Backwards' or do != 'Dlb' or do != 'Search List' or do != 'Sl'\
                    or do != 'Clear All' or do != 'Ca' or do != 'Exit' or do != 'E':
                do = input("Sorry, I didn't catch that..."
                           "\nRepeat that for me"
                           "\n>>>").title()

                if do == "Add Head" or do == "Ah":
                    add = input("What value do you wish to add"
                                "\n>>>")
                    self.add_head(add)
                    self.interface()
                    return

                elif do == "Add End" or do == "Ae":
                    add = input("What value do you wish to add"
                                "\n>>>")
                    self.add_end(add)
                    self.interface()
                    return

                elif do == "Remove Head" or do == "Rh":
                    self.remove_head()
                    self.interface()
                    return

                elif do == "Remove End" or do == "Re":
                    self.remove_end()
                    self.interface()
                    return

                elif do == "Remove" or do == "R":
                    remove = input("What value do you wish to remove"
                                   "\n>>>")
                    if self.search2(remove) is True:
                        self.remove(remove)
                    else:
                        print('Value not in the list')
                    self.interface()
                    return

                elif do == "Display List" or do == "Dl":
                    self.display()
                    self.interface()
                    return

                elif do == 'Display List Backwards' or do == 'Dlb':
                    print(self.display_bw())
                    self.interface()
                    return

                elif do == "Search List" or do == "Sl":
                    search = input("What value do you wish to search for"
                                   "\n>>>")
                    if rand <= 10:
                        self.search1(search)
                    else:
                        self.search2(search)
                        self.interface()
                    return

                elif do == "Clear All" or do == "Ca":
                    self.clear_all()
                    self.interface()
                    return

                elif do == "Exit" or do == "E":
                    print('Bye')
                    exit()
